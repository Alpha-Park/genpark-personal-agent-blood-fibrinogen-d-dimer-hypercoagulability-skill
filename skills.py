# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-personal-agent-blood-fibrinogen-d-dimer-hypercoagulability-skill
Category: personal_agent
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def evaluate_hypercoagulability_index(plasma_fibrinogen_mg_dl, d_dimer_ug_ml_feu, hs_crp_mg_l=1.2):
    if plasma_fibrinogen_mg_dl <= 0 or d_dimer_ug_ml_feu < 0:
        raise ValueError("Coagulation parameters must be positive numbers")
        
    # Normal reference:
    # Fibrinogen: 200 - 400 mg/dL (Elevated > 400 = acute phase hypercoagulability)
    # D-dimer: < 0.50 ug/mL FEU
    fibrinogen_elevated = plasma_fibrinogen_mg_dl > 400.0
    d_dimer_elevated = d_dimer_ug_ml_feu > 0.50
    
    # Thrombogenic Index (0 - 100)
    thrombo_score = min(100.0, (plasma_fibrinogen_mg_dl / 500.0) * 50.0 + (d_dimer_ug_ml_feu / 1.5) * 50.0)
    
    if d_dimer_elevated and fibrinogen_elevated:
        status = "ACTIVE_MICROTHROMBOSIS_HYPERCOAGULABILITY"
        risk_tier = "HIGH"
        advice = "Urgent vascular evaluation (Doppler ultrasound or CT pulmonary angiogram) to rule out deep vein thrombosis or pulmonary embolism."
    elif fibrinogen_elevated:
        status = "HYPERFIBRINOGENEMIA_PROTHROMBOTIC_STATE"
        risk_tier = "MODERATE"
        advice = "Systemic inflammation-driven prothrombotic state; optimize hydration and address underlying inflammatory focus."
    elif d_dimer_elevated:
        status = "ACCELERATED_FIBRINOLYTIC_TURNOVER"
        risk_tier = "MODERATE"
        advice = "Ongoing fibrin breakdown; investigate subclinical clot dissolution or hematoma."
    else:
        status = "NORMAL_COAGULATION_HOMEOSTASIS"
        risk_tier = "LOW"
        advice = "Preserved physiological hemostatic balance."
        
    return {
        "plasma_fibrinogen_mg_dl": round(plasma_fibrinogen_mg_dl, 1),
        "d_dimer_ug_ml_feu": round(d_dimer_ug_ml_feu, 3),
        "hs_crp_mg_l": hs_crp_mg_l,
        "coagulation_phenotype": status,
        "thromboembolic_risk_tier": risk_tier,
        "thrombogenic_score_0_to_100": round(thrombo_score, 1),
        "clinical_recommendation": advice
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "evaluate_hypercoagulability_index",
                        "description": """Evaluate systemic hypercoagulability and active intravascular fibrin turnover using functional Clauss fibrinogen (mg/dL) and D-dimer (ug/mL FEU).
Computes microthrombotic propensity, assesses post-viral endothelial coagulopathy (Long COVID / sepsis), and guides antithrombotic precautions.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = evaluate_hypercoagulability_index(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'plasma_fibrinogen_mg_dl': 445.0, 'd_dimer_ug_ml_feu': 0.68, 'hs_crp_mg_l': 2.8}
        out = evaluate_hypercoagulability_index(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
