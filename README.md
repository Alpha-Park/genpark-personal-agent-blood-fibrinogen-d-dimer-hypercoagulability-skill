# genpark-personal-agent-blood-fibrinogen-d-dimer-hypercoagulability-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Plasma functional fibrinogen & D-dimer hypercoagulability/microthrombosis index & Virchow triad risk calculator.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `evaluate_hypercoagulability_index`
- **Category**: `personal_agent`

### Method Documentation
Evaluate systemic hypercoagulability and active intravascular fibrin turnover using functional Clauss fibrinogen (mg/dL) and D-dimer (ug/mL FEU).
Computes microthrombotic propensity, assesses post-viral endothelial coagulopathy (Long COVID / sepsis), and guides antithrombotic precautions.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "evaluate_hypercoagulability_index",
    "arguments": {
    "plasma_fibrinogen_mg_dl": 445.0,
    "d_dimer_ug_ml_feu": 0.68,
    "hs_crp_mg_l": 2.8
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
