#!/usr/bin/env python3
"""
Regenerate explorer JSON files from current codex CSVs.
Produces: equations.json, symbols.json, stats.json
"""

import csv
import json
import sys
from datetime import date

CODEX_DIR = "/home/user/workspace/PCI-Framework/codex"
EXPLORER_DIR = "/home/user/workspace/PCI-Framework/explorer"

EQ_CSV = f"{CODEX_DIR}/pci_equation_partition_index_v71_core_frontier.csv"
SYM_CSV = f"{CODEX_DIR}/pci_symbol_partition_index_v53_core_frontier.csv"

def load_equations():
    """Load equation CSV and convert to explorer JSON format."""
    rows = []
    with open(EQ_CSV, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Strip whitespace and \r from all fields
            row = {k.strip(): v.strip() if v else "" for k, v in row.items()}
            eq_num = row.get("eq_num", "").strip()
            if not eq_num:
                continue
            entry = {
                "eq_num": eq_num,
                "eq_name": row.get("eq_name", ""),
                "partition": row.get("partition", ""),
                "module_family": row.get("module_family", ""),
                "frontier_priority": row.get("frontier_priority", ""),
                "equation": row.get("equation", ""),
                "description": row.get("description", ""),
            }
            rows.append(entry)
    return rows

def load_symbols():
    """Load symbol CSV and convert to explorer JSON format."""
    rows = []
    with open(SYM_CSV, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, restkey='_overflow')
        for row in reader:
            # Drop None keys and overflow, handle only string values
            row = {k.strip(): (v.strip() if isinstance(v, str) else "") 
                   for k, v in row.items() if k is not None and k != '_overflow'}
            sym_id = row.get("sym_id", "").strip()
            if not sym_id:
                continue
            entry = {
                "sym_id": sym_id,
                "symbol": row.get("symbol", ""),
                "name": row.get("name", ""),
                "partition": row.get("partition", ""),
                "tier": row.get("tier", ""),
                "daemon_affinity": row.get("daemon_affinity", ""),
                "domain": row.get("domain", ""),
            }
            rows.append(entry)
    return rows

def compute_stats(equations, symbols):
    """Compute summary statistics."""
    eq_core = sum(1 for e in equations if e["partition"].lower() == "core")
    eq_frontier = sum(1 for e in equations if e["partition"].lower() == "frontier")
    eq_total = len(equations)
    
    # Count unique module families
    module_families = set(e["module_family"] for e in equations if e["module_family"])
    
    # Get equation range
    eq_nums = [e["eq_num"] for e in equations]
    eq_range = f"{eq_nums[0]} through {eq_nums[-1]}" if eq_nums else "N/A"
    
    sym_core = sum(1 for s in symbols if s["partition"].lower() == "core")
    sym_frontier = sum(1 for s in symbols if s["partition"].lower() == "frontier")
    sym_total = len(symbols)
    
    # Count unique tiers
    tiers = set(s["tier"] for s in symbols if s["tier"])
    
    return {
        "equations": {
            "total": eq_total,
            "core": eq_core,
            "frontier": eq_frontier,
            "module_families": len(module_families),
            "range": eq_range,
            "version": "v77"
        },
        "symbols": {
            "total": sym_total,
            "core": sym_core,
            "frontier": sym_frontier,
            "tiers": len(tiers),
            "version": "v56"
        },
        "last_updated": str(date.today())
    }

def main():
    print("Loading equations...")
    equations = load_equations()
    print(f"  → {len(equations)} equations loaded")
    
    print("Loading symbols...")
    symbols = load_symbols()
    print(f"  → {len(symbols)} symbols loaded")
    
    print("Computing stats...")
    stats = compute_stats(equations, symbols)
    
    # Write equations.json
    eq_path = f"{EXPLORER_DIR}/equations.json"
    with open(eq_path, "w", encoding="utf-8") as f:
        json.dump(equations, f, ensure_ascii=False)
    print(f"  → {eq_path} written ({len(equations)} entries)")
    
    # Write symbols.json
    sym_path = f"{EXPLORER_DIR}/symbols.json"
    with open(sym_path, "w", encoding="utf-8") as f:
        json.dump(symbols, f, ensure_ascii=False)
    print(f"  → {sym_path} written ({len(symbols)} entries)")
    
    # Write stats.json
    stats_path = f"{EXPLORER_DIR}/stats.json"
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    print(f"  → {stats_path} written")
    
    # Summary
    print("\n=== Explorer Regeneration Complete ===")
    print(f"Equations: {stats['equations']['total']} total "
          f"({stats['equations']['core']} core, {stats['equations']['frontier']} frontier)")
    print(f"  Module families: {stats['equations']['module_families']}")
    print(f"  Range: {stats['equations']['range']}")
    print(f"Symbols:  {stats['symbols']['total']} total "
          f"({stats['symbols']['core']} core, {stats['symbols']['frontier']} frontier)")
    print(f"  Tiers: {stats['symbols']['tiers']}")
    print(f"Last updated: {stats['last_updated']}")
    
    # Validation checks
    print("\n=== Validation ===")
    if stats['equations']['total'] < 1000:
        print(f"  ⚠ WARNING: Expected ~1004 equations, got {stats['equations']['total']}")
    else:
        print(f"  ✓ Equation count looks good: {stats['equations']['total']}")
    
    if stats['symbols']['total'] < 1200:
        print(f"  ⚠ WARNING: Expected ~1232 symbols, got {stats['symbols']['total']}")
    else:
        print(f"  ✓ Symbol count looks good: {stats['symbols']['total']}")

if __name__ == "__main__":
    main()
