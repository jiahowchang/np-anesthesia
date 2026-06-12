#!/usr/bin/env python3
"""
Enhance each practice question's explanation with:
- mechanism (physiological/pharmacological detail)
- options (per-option analysis)
- guidelines (clinical guideline citations)
- expanded summary
- more specific source citation
"""
import json

# Map question ID -> enhanced fields. Each enhancement deepens the explanation.
# Fields added: mechanism, options (per-option rationale), guidelines (specific cited guidelines)
E = {

# ============ BASIC SCIENCES ============
"P-BS-001": {  # 冠狀動脈灌流壓
    "mechanism": "左心室壁張力於收縮期最高，壓迫心肌內血管使收縮期 LV 心肌血流幾乎為零；唯有舒張期主動脈壓力推動血流穿過冠脈進入心肌。LVEDP 上升 (e.g. heart failure、AS、LVH) 即代表心肌內 backpressure 上升，進一步降低 CPP。",
    "options": {
        "A": "錯誤。LV 收縮期心肌內壓過高，血流反而最少；CVP 與冠脈灌流關係小。",
        "B": "正確。Aortic diastolic − LVEDP 為左心室冠脈淨驅動壓；維持 diastolic BP ≥ 60 mmHg 為基本目標。",
        "C": "錯誤。Systolic BP 與心率呈關鍵變數；冠脈灌流確實與心率呈逆相關 (HR↑ → diastole↓ → CPP↓)。",
        "D": "錯誤。ICP 與冠脈灌流無直接關聯；該式為腦灌流壓。",
    },
    "guidelines": [
        "ACC/AHA 2014：穩定型心絞痛麻醉維持 HR < 80、避免 hypotension、Hct 維持以保有 O₂ delivery。",
        "ESC/ESA 2014 Non-cardiac Surgery：高心臟風險病人術中目標 MAP ≥ baseline 80%。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 25 Cardiovascular Physiology, pp. 624-628",
},
"P-BS-002": {  # alveolar gas equation
    "mechanism": "Alveolar gas equation 將 alveolar O₂ tension 與 inspired O₂ tension、CO₂ 與代謝比連結。R (respiratory quotient) 反映 CO₂ 產生 / O₂ 消耗，平均 0.8。PH₂O (47 mmHg at 37°C) 為飽和水蒸氣壓。",
    "options": {
        "A": "錯誤。60 mmHg 已屬 hypoxemia 範圍；若 PaO₂ < 60 應啟動 troubleshoot。",
        "B": "錯誤。80 mmHg 為 mild A-a gradient 異常時實測 PaO₂；非預期 PAO₂。",
        "C": "正確。PAO₂ = 0.21 × 713 − 40/0.8 ≈ 150 − 50 = 100 mmHg。",
        "D": "錯誤。150 mmHg 為 inspired O₂ tension (PIO₂)，未扣除 CO₂ 之影響。",
    },
    "guidelines": [
        "ARDS Berlin definition：依 PaO₂/FiO₂ ratio 分 mild (≤300)、moderate (≤200)、severe (≤100)。",
        "ATS/ESICM 2017：嚴重 ARDS 建議 prone position ≥ 16 hr/day。",
    ],
    "source": "West JB. Respiratory Physiology: The Essentials 10/e, Ch. 5; Barash Clinical Anesthesia 8/e, Ch. 13",
},
"P-BS-003": {  # oxyhemoglobin curve
    "mechanism": "Hb 與 O₂ 之結合具 cooperative binding (Hill coefficient ~2.8)。右偏代表給定 PaO₂ 下 Hb saturation 較低、P50↑、組織釋氧↑；左偏相反。",
    "options": {
        "A": "錯誤。低體溫使曲線「左偏」，O₂ 不易釋出組織。",
        "B": "錯誤。鹼血症 (pH↑) 為左偏 (Bohr effect 反向)。",
        "C": "正確。2,3-DPG 上升使 P50 上升 → 右偏 (慢性貧血、高山適應、Thyrotoxicosis)。",
        "D": "錯誤。CO 結合 Hb 親和力為 O₂ 的 230 倍，造成功能性 anemia 且使曲線「左偏」。",
    },
    "guidelines": [
        "Massive transfusion：儲存血 2,3-DPG 下降，可暫時影響 O₂ 釋放，但臨床意義通常有限。",
        "CO poisoning：100% O₂ via NRM、嚴重者考慮 HBO₂ (CarbOxy Hb > 25% 或 LOC、孕婦)。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 27 Respiratory Function pp. 663-668",
},
"P-BS-004": {  # 腎血流
    "mechanism": "腎臟為 high flow / low extraction 器官，RBF 約 1000-1200 mL/min。Cortical RBF >> medullary，但 medulla 因 countercurrent exchange 與 high tubular work 仍 vulnerable to ischemia。",
    "options": {
        "A": "錯誤。5% 為腦或肝動脈占比區間，非腎臟。",
        "B": "錯誤。10% 為運動時骨骼肌占比典型。",
        "C": "正確。腎臟占 CO 約 20-25%；GFR ≈ 125 mL/min；filtration fraction 約 20%。",
        "D": "錯誤。35% 超過所有器官；脾臟與肝臟合計約 25%。",
    },
    "guidelines": [
        "KDIGO 2012 AKI：血壓目標個體化；高血壓病人術中維持 MAP > 80 較 65 mmHg 減少 AKI (INPRESS trial 2017)。",
        "ASA：避免長時間 MAP < 55-60 mmHg 連續 ≥ 10 分鐘 (POISE-2、Salmasi 2017)。",
    ],
    "source": "Stoelting's Pharmacology & Physiology 5/e, Ch. Renal pp. 712-720",
},
"P-BS-005": {  # 腦灌流壓
    "mechanism": "Cerebral autoregulation 透過 myogenic、metabolic、neurogenic 機制維持 CBF。MAP < 50 或 > 150 mmHg autoregulation 失效，CBF 直接隨壓力變化。慢性高血壓病人曲線右移，需更高 MAP 才能維持。",
    "options": {
        "A": "錯誤。MAP + ICP 不合邏輯；ICP 是 backpressure 應扣除。",
        "B": "正確。CPP = MAP − ICP (or CVP, whichever higher)；目標 60-70 mmHg。",
        "C": "錯誤。CVP 反映 systemic venous return，非腦循環 backpressure。",
        "D": "錯誤。Systolic BP 代表 peak pressure，autoregulation 與 MAP 較相關。",
    },
    "guidelines": [
        "Brain Trauma Foundation 4/e (2016)：嚴重 TBI CPP 目標 60-70 mmHg；ICP 治療閾值 > 22 mmHg。",
        "Lund concept：早期積極控制 ICP 而不過度提升 CPP，減少 cerebral edema。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 70 Neurosurgical Anesthesia pp. 2158-2163",
},
"P-BS-006": {  # 肝血流
    "mechanism": "Hepatic Artery Buffer Response (HABR)：肝動脈經 adenosine washout 機制感知 portal flow，當門靜脈血流下降時，腺苷濃度上升使肝動脈擴張、補償氧供。Hypotension、PEEP、pneumoperitoneum、surgical traction 都會降低肝血流。",
    "options": {
        "A": "錯誤。肝動脈僅占血流 25%。",
        "B": "正確。肝動脈：血流 25%、氧供 50% (high O₂ content)；門靜脈：血流 75%、氧供 50%。",
        "C": "錯誤。門靜脈為 low pressure (8-10 mmHg)、含氧低 (混合靜脈血加 GI tract metabolism)。",
        "D": "錯誤。所有揮發性麻醉藥、Propofol infusion 都會降低肝血流 (尤其與 splanchnic constriction、CO↓ 相關)。",
    },
    "guidelines": [
        "Child-Pugh / MELD 評估：MELD ≥ 15 手術死亡率顯著上升；MELD ≥ 20 建議延後 elective surgery。",
        "美國肝病學會 (AASLD)：肝硬化病人術前評估血小板、凝血、albumin、bilirubin、encephalopathy。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e, Ch. Liver pp. 281-296",
},
"P-BS-007": {  # α1 receptor
    "mechanism": "α₁ 經 Gq protein → PLC → IP₃/DAG → 細胞內 Ca²⁺ 上升 → 平滑肌收縮。分布主要於 vascular smooth muscle (skin、splanchnic、renal)、bladder neck、iris radial muscle。",
    "options": {
        "A": "錯誤。心跳加快與收縮力增加為 β₁ effect (cAMP-mediated)。",
        "B": "錯誤。支氣管擴張與子宮鬆弛為 β₂ effect。",
        "C": "正確。α₁ → vasoconstriction + mydriasis (radial muscle 收縮)；Phenylephrine 為純 α₁。",
        "D": "錯誤。β₂ 促進 insulin secretion；α₂ 抑制 insulin secretion。",
    },
    "guidelines": [
        "Surviving Sepsis 2021：敗血性休克首選 Norepinephrine (α₁ + β₁)；MAP 目標 ≥ 65 mmHg。",
        "ASRA：spinal anesthesia 引起 hypotension 首選 Phenylephrine (尤其 obstetric)，減少 fetal acidosis。",
    ],
    "source": "Stoelting's Pharmacology 5/e, Ch. Autonomic Nervous System pp. 226-260",
},
"P-BS-008": {  # surgical stress response
    "mechanism": "手術組織損傷激活 HPA axis (CRH→ACTH→cortisol) + 交感神經 → catecholamines↑。Counterregulatory hormones (cortisol、glucagon、GH、epinephrine) 拮抗 insulin → hyperglycemia、protein catabolism、negative N balance。",
    "options": {
        "A": "錯誤。Cortisol 為 stress response 標誌，顯著上升。",
        "B": "錯誤。Epinephrine、norepinephrine 均上升 5-10 倍。",
        "C": "正確。Insulin 相對減少 + insulin resistance → hyperglycemia 為 stress response 經典特徵。",
        "D": "錯誤。ADH 受 hypovolemia、pain、surgery 刺激明顯上升，造成 SIADH-like 狀態。",
    },
    "guidelines": [
        "Society of Thoracic Surgeons 2009：心臟手術術中血糖 < 180 mg/dL 改善預後。",
        "NICE-SUGAR 2009：ICU 嚴格血糖控制 (80-110) 增加死亡率，目標 < 180 較安全。",
        "ERAS Society：multimodal opioid-sparing、regional anesthesia 可抑制 stress response。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 24 Endocrine Function pp. 580-595",
},
"P-BS-009": {  # septic shock
    "mechanism": "敗血症觸發 cytokine storm (TNF-α、IL-1、IL-6) → endothelial dysfunction、NO 過度產生 → systemic vasodilation。早期 SVR↓ 引起 reflex tachycardia、CO compensatory ↑ (hyperdynamic state)。晚期心肌抑制因子使 EF↓。",
    "options": {
        "A": "正確。Warm shock：CO↑、SVR↓、暖週邊。早期表現。",
        "B": "錯誤。為 hypovolemic / cardiogenic shock 表現。",
        "C": "錯誤。Septic shock SVR 為「下降」。",
        "D": "錯誤。低 CO 不符早期；雖晚期可能出現心肌抑制。",
    },
    "guidelines": [
        "Surviving Sepsis Campaign 2021：1h bundle (lactate、blood culture、broad-spectrum AB、crystalloid 30 mL/kg、vasopressor for MAP ≥ 65)。",
        "Sepsis-3 (2016)：Septic shock 定義 = vasopressor 維持 MAP ≥ 65 + lactate > 2 mmol/L 雖足量輸液。",
        "首選 vasopressor：Norepinephrine；refractory 加 Vasopressin、Hydrocortisone (300 mg/day)。",
    ],
    "source": "Barash Clinical Anesthesia 8/e, Ch. 53 Critical Care pp. 1530-1545",
},
"P-BS-010": {  # MH
    "mechanism": "RYR1 mutation 使 sarcoplasmic reticulum Ca²⁺ release channel 過度開啟 → cytosolic Ca²⁺ 持續高 → 肌肉持續收縮、ATP 大量消耗 → heat、CO₂、lactate 生成；rhabdomyolysis、hyperkalemia、DIC 接踵。",
    "options": {
        "A": "錯誤。Mitochondrial uncoupling 為 thyrotoxicosis、salicylate poisoning 機轉。",
        "B": "正確。RYR1 (chromosome 19q13.1) 為主要 MH 基因；少數為 CACNA1S。常染色體顯性遺傳。",
        "C": "錯誤。AChE deficiency 引起 organophosphate-like 表現。",
        "D": "錯誤。Pseudocholinesterase (BChE) 缺乏延長 succinylcholine 作用，非 MH。",
    },
    "guidelines": [
        "MHAUS Protocol 2018：Dantrolene 2.5 mg/kg IV bolus，可至 10 mg/kg cumulative；新型 Ryanodex (溶解更快) 取代傳統 Dantrium。",
        "停揮發劑、改 TIVA、Hyperventilation FiO₂ 1.0、控制體溫、處理 hyperkalemia、metabolic acidosis、DIC。",
        "MHAUS Hotline：1-800-MH-HYPER (24h)。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 43 Malignant Hyperthermia pp. 1287-1304",
},
"P-BS-011": {  # MAC
    "mechanism": "MAC 反映 anesthetic potency；脂溶性愈高、potency 愈高、MAC 愈低 (Meyer-Overton 假說)。MAC 受 CNS depressant 加成 (1 MAC + 60% N₂O ≈ 1.5 effective MAC)。",
    "options": {
        "A": "正確。每 10 歲 MAC 降約 6%；新生兒到 6 個月 MAC 反而上升。",
        "B": "正確。懷孕 MAC 降低 30-40%；progesterone-mediated。",
        "C": "正確。急性酒精中毒降低 MAC；慢性酒精 induce CYP 反而提高 MAC。",
        "D": "錯誤。Hyperthermia 每升 1°C 升 MAC 約 5%；Hypothermia 才會降低。",
    },
    "guidelines": [
        "ASA Practice Advisory：MAC-aware (清醒記憶閾值) ≈ 0.3 MAC；末期手術維持 ≥ 0.7 MAC 可降低 awareness。",
        "End-tidal monitoring：MAC ≥ 0.7 為 awareness 預防主要指標。",
    ],
    "source": "Stoelting's Pharmacology 5/e, Ch. Inhaled Anesthetics pp. 32-58",
},
"P-BS-012": {  # propofol
    "mechanism": "Propofol 增強 GABA-A receptor 作用，使 Cl⁻ 內流、神經元 hyperpolarization。心血管效應：SVR↓ (vasodilation)、myocardial depression、baroreflex blunting；呼吸：dose-dependent apnea、tidal volume↓、CO₂ response curve 鈍化。",
    "options": {
        "A": "錯誤。Propofol 一般造成 hypotension + bradycardia (vagal tone 增加)。",
        "B": "錯誤。Propofol 反而有支氣管擴張作用，COPD/Asthma 病人首選。",
        "C": "正確。Hypotension (15-40% MAP 下降) + apnea 為最常見。",
        "D": "錯誤。Propofol 為 anticonvulsant，可治療 status epilepticus。",
    },
    "guidelines": [
        "ASA 2018：嚴重 LV dysfunction、aortic stenosis、hypovolemia 應減量 (25-50%) 並合併 vasopressor。",
        "FDA：Propofol Infusion Syndrome (PRIS) 風險 > 4 mg/kg/h × 48h；兒童尤其。",
    ],
    "source": "Nagelhout Nurse Anesthesia 6/e, Ch. 11 IV Anesthetics pp. 110-115",
},
"P-BS-013": {  # remifentanil
    "mechanism": "Remifentanil 結構含 ester linkage，由 nonspecific tissue + plasma esterases 水解 (非 pseudocholinesterase)。其 context-sensitive half-time 3-4 min 不隨輸注時間延長 — 此性質源自小 Vd 與 fast clearance。",
    "options": {
        "A": "錯誤。Morphine 透過 glucuronidation 代謝，M3G、M6G 主要由腎排出。",
        "B": "錯誤。Fentanyl 為 CYP3A4 代謝；context-sensitive half-time 隨輸注時間顯著延長。",
        "C": "正確。Remifentanil esterase metabolism、肝腎衰竭可用，可預測之快速 offset。",
        "D": "錯誤。Meperidine 經 CYP 代謝為 normeperidine (具神經毒性)，腎衰積聚。",
    },
    "guidelines": [
        "TIVA Society：Remifentanil + Propofol 為 TIVA 經典組合，BIS 監測下可達 deep anesthesia。",
        "停藥前 30 min 應建立 multimodal analgesia (e.g. Morphine 0.1 mg/kg、Ketamine、regional)，避免 rebound pain + hyperalgesia。",
    ],
    "source": "Stoelting's Pharmacology 5/e, Ch. Opioids pp. 87-122",
},
"P-BS-014": {  # pseudocholinesterase deficiency
    "mechanism": "Plasma cholinesterase (butyrylcholinesterase, BChE) 由肝合成、normaly 快速水解 succinylcholine 與 mivacurium。BCHE gene 變異 → 異常酵素 → succinylcholine 半衰期延長 4-8 小時。",
    "options": {
        "A": "錯誤。MH 表現為 hypermetabolic state (ETCO₂↑、體溫↑、僵直)，非單純 prolonged paralysis。",
        "B": "正確。Dibucaine number = % BChE 活性被 dibucaine 抑制；正常 ≥ 80、heterozygous ~50、homozygous ~20。",
        "C": "錯誤。Hyperkalemia 不會延長 succinylcholine paralysis (反而會引起 cardiac arrest)。",
        "D": "錯誤。Rocuronium 殘餘可用 sugammadex 反轉、TOF 確認；非延長 succinylcholine 原因。",
    },
    "guidelines": [
        "MHAUS：所有 prolonged paralysis 均應通報並建議家屬基因諮詢。",
        "處置：mechanical ventilation + 鎮靜直到 TOF 恢復；通常 4-8 小時自行恢復。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 35 Neuromuscular Blockers pp. 985-987",
},
"P-BS-015": {  # sugammadex
    "mechanism": "Sugammadex 為 γ-cyclodextrin 修飾物，疏水核心 encapsulate steroidal NMBA (1:1 complex)，再由腎排出。對 benzylisoquinolinium 結構 (atracurium、cisatracurium、mivacurium) 無作用。",
    "options": {
        "A": "錯誤。Succinylcholine 為 depolarizing，無 reversal；自然代謝。",
        "B": "錯誤。Cisatracurium 由 Hofmann elimination + ester hydrolysis 代謝。",
        "C": "正確。Steroidal NMBA：Rocuronium > Vecuronium > Pancuronium 親和力。",
        "D": "錯誤。Pancuronium 親和力較低、臨床上 sugammadex 對其效果不佳。",
    },
    "guidelines": [
        "Anaesthesia Reversal Guidelines (AAGBI 2016)：moderate block (TOF count 2-3) 2 mg/kg；deep block (PTC ≥ 1) 4 mg/kg；immediate (RSI failure) 16 mg/kg。",
        "FDA：含 progesterone 口服避孕藥失效 7 天，需告知病人。",
        "罕見但重要：Bradycardia (考慮 atropine pre-treat)、anaphylaxis (0.039%)。",
    ],
    "source": "Barash Clinical Anesthesia 8/e, Ch. 21 NMBA pp. 561-565",
},
"P-BS-016": {  # LAST
    "mechanism": "Local anesthetic systemic toxicity 機轉：阻斷 cardiac Na⁺ channel + mitochondrial dysfunction。Bupivacaine 因高 lipid solubility、long binding → 心毒性高、復甦困難。Lipid emulsion 透過 lipid sink theory 加 metabolic shuttle 機轉，將藥物從心肌移除。",
    "options": {
        "A": "錯誤。Amiodarone 為 Na/K channel blocker，恐加重 toxicity；ACLS 中應避免。",
        "B": "正確。20% Intralipid 1.5 mL/kg bolus + 0.25 mL/kg/min infusion + 高品質 CPR。",
        "C": "錯誤。Vasopressin 在動物實驗中惡化 LAST 預後，不建議使用。",
        "D": "錯誤。Lidocaine 為 LAST 一員，不可加重；ACLS 中應減量 / 避免。",
    },
    "guidelines": [
        "ASRA 2018 LAST Checklist：求救、停藥、保護氣道、抽搐用 Benzo、Lipid emulsion、Epinephrine ≤ 1 µg/kg。",
        "預防：超音波導引、incremental injection (每 5 mL 抽吸)、總劑量計算 (Bupivacaine ≤ 2 mg/kg、Lidocaine ≤ 4.5 mg/kg w/o epi、7 mg/kg w/ epi)。",
        "成功復甦後 ICU 觀察 ≥ 12 小時。",
    ],
    "source": "ASRA Practice Advisory on LAST 2018; Barash 8/e Ch. 22",
},
"P-BS-017": {  # norepinephrine
    "mechanism": "Norepinephrine 對 α₁ > β₁ > β₂ 親和力遞減。低劑量 (< 0.1 µg/kg/min) β₁ effect 較明顯；高劑量 α₁ 主導。靜脈 extravasation 致 vasoconstriction-induced ischemic necrosis，需 phentolamine local infiltration。",
    "options": {
        "A": "錯誤。Norepinephrine 有顯著 β₁ inotropic effect (與 epinephrine 比較少 β₂)。",
        "B": "正確。α₁ + β₁ 雙重作用：升 SVR + 心搏量、輕微提高 HR；為敗血性休克首選。",
        "C": "錯誤。Anaphylactic shock 首選 Epinephrine (α + β₁ + β₂ mast cell stabilization)。",
        "D": "錯誤。長時間周邊靜脈 NE 輸注有 extravasation + ischemic necrosis 風險，建議中心靜脈。",
    },
    "guidelines": [
        "Surviving Sepsis 2021：First-line vasopressor = Norepinephrine；MAP target ≥ 65。",
        "ESC 2015：Cardiogenic shock 若 hypotension 顯著，NE 較 Dopamine 死亡率低 (SOAP II trial)。",
        "Peripheral NE 短期使用 (< 24h、< 0.1 µg/kg/min) 經 18-20G 大靜脈被視為可接受 (Cardenas-Garcia 2015)。",
    ],
    "source": "Stoelting's Pharmacology 5/e, Ch. Sympathomimetics pp. 286-310",
},
"P-BS-018": {  # context-sensitive half-time
    "mechanism": "傳統 t½ 假設 single-compartment、bolus dosing；但 continuous infusion 因 redistribution、peripheral compartment saturation，停藥後濃度下降速率非線性。CSHT 將此複雜性量化，是 TIVA 管理核心。",
    "options": {
        "A": "錯誤。完全清除為 5 個 elimination half-life；非 CSHT 概念。",
        "B": "錯誤。Steady state 為 4-5 個 half-life；非 CSHT 概念。",
        "C": "正確。CSHT = 停止輸注後血中濃度下降 50% 之時間，隨輸注時間 (context) 變化。",
        "D": "錯誤。Bioavailability 為 PO 與 IV AUC 比值；與 CSHT 無關。",
    },
    "guidelines": [
        "Society for Intravenous Anaesthesia (SIVA)：TIVA 應使用 target-controlled infusion (TCI) 模型 (Schnider、Marsh)。",
        "BIS 監測對 TIVA 特別有用，因無 end-tidal 直接讀數。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 29 Pharmacokinetics pp. 638-654",
},
"P-BS-019": {  # Poiseuille
    "mechanism": "Hagen-Poiseuille 描述 Newtonian fluid 於 rigid tube 之 laminar flow。流量 Q ∝ ΔP × r⁴ / (η × L)。半徑因 4 次方影響最顯著；長度與黏度為線性。",
    "options": {
        "A": "錯誤。長度減半使流量加倍 (×2)，遠不及半徑加倍。",
        "B": "正確。半徑加倍使流量增 2⁴ = 16 倍，最顯著。",
        "C": "錯誤。壓力加倍 → 流量加倍。",
        "D": "錯誤。黏度減半 → 流量加倍。",
    },
    "guidelines": [
        "ATLS 10/e：大量失血急救建立 ≥ 2 條 16-18G peripheral IV (= 大口徑短管路) > central line for rapid resuscitation。",
        "Cordis (8.5 Fr 短管) 流速 > 三腔 central line (細長腔)。",
        "Pressure bag 加壓可進一步提升流速 (但對小管路提升有限)。",
    ],
    "source": "Pocket Anesthesia 3/e, Physics; West Respiratory Physiology",
},
"P-BS-020": {  # Compound A
    "mechanism": "Sevoflurane 與 soda lime 之 strong base (NaOH/KOH) 反應產生 fluoromethyl-2,2-difluoro-1-(trifluoromethyl)-vinyl ether (Compound A)。低流速 + 乾燥 + 高溫 + NaOH/KOH 條件下產量最大。動物實驗具腎毒性，人類臨床意義尚有爭議。",
    "options": {
        "A": "正確。Low flow、dry、strong base、high temp 全為高 Compound A 條件。",
        "B": "錯誤。高流速會 dilute、wet absorbent 反而減少 Compound A。",
        "C": "錯誤。Desflurane 與乾燥 strong base 反應產生 CO (尤其周末後第一台)，非 Compound A。",
        "D": "錯誤。Amsorb (Ca(OH)₂ + CaCl₂) 不含 strong base，幾乎不產生 Compound A 或 CO。",
    },
    "guidelines": [
        "FDA Sevoflurane label：Low-flow (< 2 L/min) 建議 ≤ 2 MAC-hr；fresh gas flow ≥ 1 L/min。",
        "ASA Recommendation：使用新型 absorbent (Amsorb、Litholyme、Drägersorb 800+) 較安全。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 30 Inhaled Anesthetics pp. 712-718",
},

# ============ EQUIPMENT ============
"P-EQ-021": {  # fail-safe valve
    "mechanism": "Fail-safe valve (pressure-sensor shut-off valve) 連動 O₂ pipeline pressure 與 N₂O / 其他氣體 flow control。當 O₂ pressure < 25-30 psi，valve 關閉或 proportional reduction 其他氣體流量。",
    "options": {
        "A": "錯誤。N₂O 中斷不應觸發 O₂ 自動補給；fail-safe 是反向 (O₂↓ → 切 N₂O)。",
        "B": "正確。標準功能：O₂ supply pressure failure → 自動切斷或降低其他氣體。",
        "C": "錯誤。CO₂ absorbent 監測由 capnography (re-breathing CO₂) 與 color indicator，非 fail-safe。",
        "D": "錯誤。Disconnection 由 ventilator low pressure alarm、capnography 偵測。",
    },
    "guidelines": [
        "ASA Guidelines for Anesthesia Workstation Checkout 2008：每日 daily checkout 包含 fail-safe valve test (關 O₂、確認 N₂O 流量降至 0)。",
        "Hypoxic guard (Link 25, Ohmeda) 額外保證 FiO₂ ≥ 21-25% 不論 N₂O 流量。",
        "O₂ analyzer 為最後一道防線 (法定要求)，必須每次校正 21% (room air) 與 100%。",
    ],
    "source": "Dorsch Understanding Anesthesia Equipment 5/e, Ch. 3 pp. 56-89",
},
"P-EQ-022": {  # leak test
    "mechanism": "High-pressure system (氣瓶到 pressure regulator) 主要漏氣由壓力錶判讀；low-pressure system (vaporizer、common gas outlet) 漏氣需 negative pressure 測試 — 因 positive pressure test 可能被 check valve 遮蔽。",
    "options": {
        "A": "錯誤。Negative pressure test 用於 low-pressure system，非 high-pressure。",
        "B": "錯誤。O₂ flush test 檢查 common gas outlet 與 breathing circuit，非 leak test。",
        "C": "錯誤。Sodalime 顏色變化 (ethyl violet → 紫) 反映 absorbent 耗盡，非 leak。",
        "D": "正確。關氣瓶觀察壓力錶下降速率為標準 high-pressure leak test。",
    },
    "guidelines": [
        "FDA Pre-Use Checkout (1993 updated 2008)：14 items；ASA 簡化為 daily + between-case。",
        "Between-case abbreviated check：vaporizer、breathing system、ventilator function、scavenging。",
        "Pre-use checklist 失敗：禁止使用，呼叫工程；不可 'override'。",
    ],
    "source": "ASA 2008 Anesthesia Apparatus Checkout Recommendations",
},
"P-EQ-023": {  # circle system valve
    "mechanism": "Inspiratory valve 防止吐氣回流至 inspiratory limb；expiratory valve 防止吸氣 short-circuit absorbent。Valve sticky (wet、debris、condensation) → rebreathing → ETCO₂ baseline ≠ 0 + 漸升 PaCO₂。",
    "options": {
        "A": "錯誤。肺水腫無關 unidirectional valve；通常為 cardiac、ARDS 原因。",
        "B": "正確。Rebreathing → hypercapnia、capnograph 出現 inspired CO₂。",
        "C": "錯誤。FiO₂ alarm 與 valve 無直接關聯。",
        "D": "錯誤。Compound A 為 sevoflurane + strong base 反應，與 valve 無關。",
    },
    "guidelines": [
        "Capnogram phase III (alveolar plateau) 抬高 + baseline ≠ 0 為 rebreathing 特徵。",
        "處置：立即改 Mapleson D 或 bag-mask、手動 ventilation，呼叫 BME。",
        "預防：每日 valve 視覺檢查、防潮、定期 calibration。",
    ],
    "source": "Dorsch Understanding Anesthesia Equipment 5/e, Ch. 8 pp. 218-235",
},
"P-EQ-024": {  # capnography
    "mechanism": "ETCO₂ 急降至接近 0 + 呼吸音消失，通常代表沒有氣體交換：(1) ETT 脫至食道；(2) Circuit disconnection；(3) Cardiac arrest (cessation of pulmonary blood flow)；(4) Massive PE (drop but not to 0)；(5) Severe bronchospasm。",
    "options": {
        "A": "錯誤。Right mainstem intubation 不會使 ETCO₂ 顯著下降，但 peak airway pressure 上升、單側肺音。",
        "B": "正確。Esophageal intubation / circuit disconnect 為最危急且最常見之 ETCO₂ 急降原因。",
        "C": "錯誤。Hypercapnia 使 ETCO₂ 上升。",
        "D": "錯誤。Massive PE 使 ETCO₂ 下降但通常較緩、伴循環不穩；不到接近 0。",
    },
    "guidelines": [
        "ASA Closed Claims Analysis：Esophageal intubation 為麻醉死亡主要原因之一；capnography 為 gold standard。",
        "Difficult Airway Society (DAS) 2015：Two consecutive expired CO₂ waveforms 確認 tracheal intubation。",
        "PALS、ACLS：CPR 期間 ETCO₂ < 10 mmHg 預後差；> 10 提示 ROSC。",
    ],
    "source": "Hagberg Airway Management 4/e; ASA Closed Claims Project",
},
"P-EQ-025": {  # LMA
    "mechanism": "LMA 坐落 hypopharynx，cuff 環繞 laryngeal inlet。Classic LMA 之 seal pressure 平均 20 cmH₂O，無法阻止 regurgitated gastric content。",
    "options": {
        "A": "錯誤。短期手術正是 LMA 適應症。",
        "B": "正確。Full stomach / 腸阻塞為相對至絕對禁忌；regurgitation + aspiration 風險高。",
        "C": "錯誤。OSA 病人可用 LMA，但須謹慎；非絕對禁忌。",
        "D": "錯誤。BMI 25 不算特殊風險；嚴重肥胖 (BMI > 35) 才需謹慎。",
    },
    "guidelines": [
        "DAS Guidelines 2015：LMA 為 difficult airway rescue device (Plan B)。",
        "Second-generation SAD (LMA ProSeal、Supreme、i-gel) 含 drain tube，可吸引胃內容物，部分降低 aspiration 風險。",
        "Aspiration risk factors：full stomach、obstruction、GERD、pregnancy、obesity、urgent surgery → 避免 LMA、使用 ETT + RSI。",
    ],
    "source": "Hagberg Airway Management 4/e, Ch. 22 Supraglottic Devices",
},
"P-EQ-026": {  # VL
    "mechanism": "Video laryngoscope hyperangulated blade 提供良好 glottic view，但 ETT 推進需大角度 turn — 直 stylet 難進入。Pre-shaped stylet (60° curve, 'hockey stick') 配合 blade 設計可改善成功率。",
    "options": {
        "A": "錯誤。GlideScope 與 hyperangulated VL 之 blade tip 通常置於 vallecula 中央，類似 Macintosh，但不需深入會厭谷。",
        "B": "正確。專用 stylet (60° curve) 必須使用；硬塞造成 palatal、pharyngeal、tonsillar laceration。",
        "C": "錯誤。VL 不能完全取代 DL；停電、camera fog、blood 都需備 DL。",
        "D": "錯誤。VL 為困難呼吸道 first-line 工具之一；DAS 2015 Plan A 之選項。",
    },
    "guidelines": [
        "DAS 2015：困難氣道 Plan A (best attempt = 3 tries with VL + 適當 stylet)。",
        "FDA reports：GlideScope 相關 oropharyngeal injury 多源自不正確 ETT 推進技術。",
        "MACOCHA score：predictor for difficult intubation in ICU (Mallampati、OSA、cervical mobility 等)。",
    ],
    "source": "Hagberg Airway Management 4/e, Ch. 25 Video Laryngoscopy",
},
"P-EQ-027": {  # CICO
    "mechanism": "CICO 為 anesthesia 急症之一，O₂ saturation 下降可於 1-2 分鐘內導致 anoxic brain injury。Front of neck access (FONA) 透過 cricothyroid membrane 建立 emergency airway，繞過聲門阻塞。",
    "options": {
        "A": "錯誤。失敗 DL 再嘗試多次只增加損傷；應快速進展到下一步。",
        "B": "正確。CICO → 立即 FONA (scalpel-bougie-tube)，不延誤。",
        "C": "錯誤。Awake fiberoptic 需配合醒著的病人；CICO 時病人已麻醉、低氧。",
        "D": "錯誤。Sugammadex reverse rocuronium 仍需時間 (1-3 min)，CICO 必須同步 FONA。",
    },
    "guidelines": [
        "DAS 2015 Algorithm：Plan A (face mask + 3 attempt intubation)、Plan B (SAD)、Plan C (face mask)、Plan D (FONA)。",
        "Project for Universal Management of Airways (PUMA)：宣告 CICO、明確角色 (誰做 FONA、誰準備裝備)。",
        "兒童 < 12 歲：cricothyroid membrane 小，建議 needle cricothyroidotomy + jet ventilation 或 emergency rigid bronchoscopy。",
    ],
    "source": "DAS 2015 Difficult Airway Guidelines; Hagberg 4/e Ch. 31",
},
"P-EQ-028": {  # ASA monitor
    "mechanism": "ASA Standards for Basic Anesthetic Monitoring 自 1986 起持續更新；定義 anesthesia provider 必須在場 + 持續評估 oxygenation、ventilation、circulation、temperature。",
    "options": {
        "A": "錯誤。持續 EKG 為 standard。",
        "B": "錯誤。SpO₂ 為 standard，所有麻醉都需。",
        "C": "正確。Invasive A-line 非 standard，依手術病人決定 (心臟、神經外科、嚴重 hemodynamic instability)。",
        "D": "錯誤。體溫於 anticipated clinically significant 改變時需測 (general anesthesia > 30 min 通常需要)。",
    },
    "guidelines": [
        "ASA Standards (revised 2015)：Oxygenation (FiO₂ + SpO₂)、Ventilation (capnography quantitative ≥ 15 min)、Circulation (EKG + BP ≥ q5 min + 持續心跳)、Temperature。",
        "Capnography 為 ASA mandatory，且必須 quantitative。",
        "MAC sedation 亦需 ASA standards；不可降低監測標準。",
    ],
    "source": "ASA Standards for Basic Anesthetic Monitoring (2015 revision)",
},
"P-EQ-029": {  # pulse contour
    "mechanism": "Pulse contour analysis 以動脈波形之 area under systolic ejection 推算 stroke volume，乘 HR 得 CO。Mechanical ventilation 時 intrathoracic pressure 變化引起 SVV (stroke volume variation)；SVV > 13% 預示 fluid responsiveness。",
    "options": {
        "A": "錯誤。Standard EKG 不提供 CO 數值。",
        "B": "正確。FloTrac、PiCCO、LiDCO、Vigileo 等系統皆使用此原理。",
        "C": "錯誤。Pulse oximeter 提供 SpO₂、PI、(PVI on Masimo)；非 CO。",
        "D": "錯誤。Capnography ETCO₂ 與 CO 有相關 (尤其 CPR 中)，但非主要 CO monitor。",
    },
    "guidelines": [
        "ESA Perioperative Hemodynamic Monitoring 2015：高風險手術建議 advanced hemodynamic monitoring (cardiac output + dynamic indicators)。",
        "FloTrac 適用條件：sinus rhythm、controlled ventilation TV ≥ 8 mL/kg、無 RV failure、無嚴重 arrhythmia。",
        "TEE 為心臟手術金標準；POCUS (LV function、IVC) 普及為非侵入評估。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 45 Cardiovascular Monitoring",
},
"P-EQ-030": {  # BIS
    "mechanism": "BIS 透過 frontal EEG 之 frequency analysis、bispectral analysis 演算法 (專利) 衍生 0-100 scale。可作為 anesthesia depth 替代指標，與 anesthetic concentration 大致相關，但 ketamine、N₂O 不影響。",
    "options": {
        "A": "錯誤。0-20 為 burst suppression、過深；可能延長甦醒、增加 POD。",
        "B": "正確。40-60 為 general anesthesia 適當範圍。",
        "C": "錯誤。70-90 為 light sedation 至 moderate sedation，全麻不夠。",
        "D": "錯誤。90-100 為清醒。",
    },
    "guidelines": [
        "B-Aware (2004) & B-Unaware (2008) trials：BIS 監測可降低 awareness 風險 (高風險族群 e.g. cardiac、obstetric、TIVA)。",
        "ASA Practice Advisory 2006：BIS 為 'may be useful'；非 mandatory；不替代 end-tidal MAC 監測。",
        "Limits：肌電干擾、體溫低、ketamine、N₂O、年齡。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 50 Awareness Under Anesthesia",
},
"P-EQ-031": {  # TOF
    "mechanism": "TOF count 反映 nicotinic AChR 占有率 (T4 disappear ~75%、T3 80%、T2 85%、T1 90-95% blockade)。TOF ratio (T4/T1) 反映 fade — 殘餘 NMB 之敏感指標。",
    "options": {
        "A": "錯誤。0.4 仍為嚴重 residual block，極危險。",
        "B": "錯誤。0.6 已有顯著 risk of upper airway obstruction、hypopharyngeal dysfunction。",
        "C": "錯誤。0.7 為早期建議閾值，近年研究顯示不夠。",
        "D": "正確。TOF ratio ≥ 0.9 為 adequate recovery 公認標準。",
    },
    "guidelines": [
        "ASA Practice Advisory on Neuromuscular Blockade 2015：使用客觀 quantitative monitor (acceleromyography、electromyography)。",
        "TOF count ≥ 2 才能用 neostigmine 反轉；deep block (PTC < 1) 改用 sugammadex 4 mg/kg。",
        "Residual NMB 與 PACU respiratory complications、reintubation、aspiration 相關。",
    ],
    "source": "Barash Clinical Anesthesia 8/e, Ch. 21 NMBA pp. 554-560",
},
"P-EQ-032": {  # US probe
    "mechanism": "超音波頻率與解析度、穿透深度反向相關。高頻 (10-15 MHz) 解析度好但僅 1-4 cm 深；低頻 (1-5 MHz) 可達 20+ cm 深度但解析度低。",
    "options": {
        "A": "錯誤。Phased array 用於心臟 (small footprint between ribs)，非週邊神經。",
        "B": "正確。6-15 MHz linear probe 為 vascular access、peripheral nerve block 標準。",
        "C": "錯誤。Curvilinear 用於 abdomen、TAP block、deep nerve (e.g. lumbar plexus)。",
        "D": "錯誤。Endocavitary 為 TEE、TRUS、TVUS。",
    },
    "guidelines": [
        "ASRA 2014：超音波導引降低 LAST 發生率、提高 success rate、降低 onset time。",
        "ANZCA、ASRA：超音波培訓建議至少 50 procedures supervised practice 達 competency。",
        "ASA Practice Advisory：central venous access 建議使用 ultrasound guidance。",
    ],
    "source": "Brown's Atlas of Regional Anesthesia 5/e, Ch. 1 Ultrasound Basics",
},

# ============ GENERAL PRINCIPLES ============
"P-GP-033": {  # informed consent
    "mechanism": "Informed consent 法律與倫理基礎為 autonomy。Decision-making capacity 須評估：(1) 理解資訊；(2) 評估利弊；(3) 推理；(4) 表達意願。",
    "options": {
        "A": "錯誤。簽名僅為記錄；無充分 disclosure + understanding 即無效。",
        "B": "正確。四要素：disclosure、understanding、voluntariness、capacity 均須具備。",
        "C": "錯誤。精神病史不等於失能；須個別評估 decision-making capacity。",
        "D": "錯誤。緊急 + life-threatening 可援用 implied consent，但應記錄、事後盡早補告知。",
    },
    "guidelines": [
        "AMA Code of Medical Ethics 2.1.1：Informed consent。",
        "ASA Statement on Informed Consent for Anesthesia 2018：anesthesia consent 應與外科分開，特別告知 anesthesia 特有風險。",
        "Jehovah's Witness：必須術前明確記錄輸血選擇 (whole blood vs. fractions)。",
    ],
    "source": "Barash Clinical Anesthesia 8/e, Ch. 1; AMA Ethics Code",
},
"P-GP-034": {  # DNR
    "mechanism": "DNR 反映病人 end-of-life preference；手術環境中 anesthetic intervention (insertion of airway、vasopressor) 與 'resuscitation' 重疊，須明確協商。",
    "options": {
        "A": "錯誤。DNR 病人可接受手術 (e.g. palliative debulking、fracture fix for comfort)。",
        "B": "錯誤。自動暫停違反病人 autonomy。",
        "C": "正確。Required Reconsideration：與病人/家屬討論 + 三選一 (Full、Procedure-directed、Goal-directed) + 明確記錄。",
        "D": "錯誤。單方面決定違反倫理；應與病人/family/手術醫師共同決定。",
    },
    "guidelines": [
        "ASA Ethical Guidelines for the Anesthesia Care of Patients With Do-Not-Resuscitate Orders 2018：Required Reconsideration。",
        "ACS Statement on Advance Directives by Patients 2014：類似立場。",
        "PACU 後重新評估 DNR 是否恢復原狀；明確時程 (e.g. 24 小時)。",
    ],
    "source": "ASA Standards & Practice Parameters; Miller's 8/e Ch. 14",
},
"P-GP-035": {  # WHO checklist
    "mechanism": "WHO Surgical Safety Checklist (2008) 由 Atul Gawande 主導，三階段確認手術正確性與安全準備。研究顯示可降低死亡率、併發症 30%+。",
    "options": {
        "A": "正確。Sign In (麻醉前)：身分、手術部位、同意書、過敏、airway 評估、bleeding risk。",
        "B": "正確。Time Out (切皮前)：所有人停下確認三項 (病人、手術、部位) + 抗生素時機 + 影像。",
        "C": "正確。Sign Out (病人離室前)：手術名稱、計數 (gauze、instrument)、檢體標籤、設備問題、術後重點。",
        "D": "錯誤。Stop-the-line authority 是 checklist 文化的核心，任何成員均可暫停。",
    },
    "guidelines": [
        "WHO Safe Surgery Saves Lives Campaign 2009。",
        "Joint Commission Universal Protocol：site marking、time-out。",
        "Closed-loop communication：sender 表達、receiver 重複、sender 確認。",
    ],
    "source": "WHO Surgical Safety Checklist Manual 2009",
},
"P-GP-036": {  # OR fire
    "mechanism": "Operating Room Fire 三角：oxidizer + fuel + ignition。Face/neck/upper chest surgery 在 oxygen-enriched atmosphere 下使用 electrocautery 為最高風險組合。",
    "options": {
        "A": "正確。Fire triangle 元素：oxidizer、fuel、ignition。",
        "B": "錯誤。Water 是滅火物，非 fire triangle。",
        "C": "錯誤。混淆 risk factors 與 triangle elements。",
        "D": "錯誤。Wind 為 outdoor fire 因素，非 OR。",
    },
    "guidelines": [
        "ASA Fire Algorithm 2013：預防 (低 FiO₂ < 30% in face/neck、避免 alcohol pool、laser-ETT)；處置 (停 ventilation、拔 ETT、停 gas、saline)。",
        "ECRI Institute Top 10 Health Technology Hazards：OR fire 多年在榜。",
        "Joint Commission Sentinel Event Alert #29：OR fire prevention。",
    ],
    "source": "Barash Clinical Anesthesia 8/e, Ch. 17; ASA Fire Algorithm",
},
"P-GP-037": {  # ASA classification
    "mechanism": "ASA Physical Status 為 1941 年制訂，目的標準化術前風險溝通；不直接預測手術死亡率，但作為 risk stratification 工具。",
    "options": {
        "A": "錯誤。ASA I 為健康 + 無任何 systemic disease。",
        "B": "錯誤。ASA II 為 mild systemic disease 無功能限制 (如控制良好高血壓單一)。",
        "C": "正確。ASA III：severe systemic disease + functional limitation but not life-threatening (多重慢性病、控制中)。",
        "D": "錯誤。ASA IV：嚴重失能且持續威脅生命 (e.g. unstable angina、severe HF)。",
    },
    "guidelines": [
        "ASA Physical Status Classification System (2020 updated definitions + examples)。",
        "Pediatric examples 已 ASA 補充 (2014)。",
        "Emergency (E) 加註：手術延誤即增加 morbidity；非 elective。",
    ],
    "source": "ASA Physical Status Classification System (2020)",
},
"P-GP-038": {  # NPO
    "mechanism": "NPO 目的減少 gastric content 與 pulmonary aspiration 風險。胃排空時間：清液 < 2 小時；母乳 3-4 小時；formula 4-6 小時；固體脂肪含量越高越久。",
    "options": {
        "A": "正確。Clear liquids 2h (e.g. water、apple juice、clear tea、black coffee w/o milk)。",
        "B": "正確。母乳 4h。",
        "C": "正確。Infant formula / non-human milk 6h。",
        "D": "錯誤。Light meal (toast + clear liquid) 須 6h；4h 不夠。Heavy/fried/fatty meal ≥ 8h。",
    },
    "guidelines": [
        "ASA Practice Guidelines for Preoperative Fasting 2017 update。",
        "ERAS：術前 2h carbohydrate-rich clear drink (e.g. Nutricia preOp)，減少 insulin resistance + 改善舒適。",
        "Diabetes、GERD、pregnancy、bowel obstruction、emergency → 延長禁食或 RSI。",
    ],
    "source": "ASA Practice Guidelines for Preoperative Fasting 2017",
},
"P-GP-039": {  # cardiac risk
    "mechanism": "ACC/AHA stepwise approach：(1) emergency?；(2) active cardiac condition?；(3) low risk surgery?；(4) functional capacity ≥ 4 METs？；(5) RCRI + biomarkers + further test only if changes management。",
    "options": {
        "A": "錯誤。Left axis deviation 為 nonspecific finding，不主導 risk。",
        "B": "正確。RCRI (Lee 1999) 加 METs assessment 為標準 framework。",
        "C": "錯誤。Cholesterol 非急性 perioperative risk indicator。",
        "D": "錯誤。腦波無 cardiac risk 評估角色。",
    },
    "guidelines": [
        "ACC/AHA 2014 Guidelines on Perioperative Cardiovascular Evaluation。",
        "ESC/ESA 2014：類似，加入 biomarkers (BNP、troponin)。",
        "DAPT after stent：DES 6-12 月、BMS 1 月之內 elective surgery 應延後。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e",
},
"P-GP-040": {  # DOAC
    "mechanism": "DOACs 短 t½ (8-15h)，停藥後 24-48h 內凝血恢復。腎排泄比例不同：Dabigatran 80%、Rivaroxaban 35%、Apixaban 25%、Edoxaban 50%。",
    "options": {
        "A": "錯誤。8h 不足以代謝、出血風險高。",
        "B": "錯誤。24h 適用於 low bleeding risk surgery (e.g. skin、cataract)。",
        "C": "正確。Hip replacement 為 high bleeding risk → 48-72h；neuraxial 需 72h。",
        "D": "錯誤。7 天為 ASA、clopidogrel 範圍，不適用 DOACs。",
    },
    "guidelines": [
        "ASRA Anticoagulation Guidelines 4/e (2018)：細節停藥時程 by drug + procedure risk。",
        "ESA Perioperative Anticoagulation 2018。",
        "Reversal：Dabigatran → Idarucizumab；Apixaban/Rivaroxaban → Andexanet alfa 或 PCC。",
    ],
    "source": "ASRA Anticoagulation Guidelines 4/e (2018)",
},
"P-GP-041": {  # Holliday-Segar
    "mechanism": "Holliday-Segar (1957) 基於代謝率與體重關係：第一個 10 kg 需 100 mL/kg/day；第二個 10 kg 需 50 mL/kg/day；> 20 kg 需 20 mL/kg/day。對應 4-2-1 hourly rule。",
    "options": {
        "A": "錯誤。1000 mL 為 10 kg child。",
        "B": "錯誤。1300 mL 為計算錯誤。",
        "C": "正確。1000 + 500 + 100 = 1600 mL/day = 65 mL/hr。",
        "D": "錯誤。2000 mL 過高，相當於 35 kg。",
    },
    "guidelines": [
        "APA 2013：Pediatric maintenance fluid 應使用 isotonic fluid (e.g. 0.9% NaCl 或 LR)，避免 hyponatremia。",
        "Hypotonic fluid (D5 0.45% NS) 已不建議常規使用，引起多例 fatal hyponatremia。",
        "ABC fluid: 4-2-1 maintenance + replacement of deficit + ongoing losses。",
    ],
    "source": "Coté and Lerman's A Practice of Anesthesia for Infants and Children 6/e",
},
"P-GP-042": {  # transfusion
    "mechanism": "Restrictive transfusion strategy 證據基於多項 RCT (TRICC、TRISS、FOCUS)。Hb 7-8 為 trigger 不增 morbidity、減少輸血併發症 (TRALI、TACO、TRIM)。",
    "options": {
        "A": "錯誤。Hb < 10 過度寬鬆，不符合最新指引。",
        "B": "正確。穩定 Hb < 7；ACS、心臟手術 < 8。",
        "C": "錯誤。一律 9 g/dL 不符 evidence-based。",
        "D": "錯誤。Hct < 35% 為過時且過嚴標準。",
    },
    "guidelines": [
        "AABB 2016 Red Blood Cell Transfusion Guidelines：restrictive (Hb 7-8) for stable hospitalized adults。",
        "TRICC trial 1999：restrictive non-inferior。",
        "Massive Transfusion Protocol：1:1:1 (RBC:FFP:Plt) 或 goal-directed by TEG/ROTEM。",
    ],
    "source": "AABB Guidelines 2016; Stoelting's 7/e",
},
"P-GP-043": {  # fluid responsiveness
    "mechanism": "Mechanical ventilation 引起 cyclic intrathoracic pressure 變化 → preload 變化 → SV 變化 (僅在 Frank-Starling 上升斜率時)。SVV > 13% (with 8+ mL/kg TV、sinus、closed chest、controlled vent) 預示 volume responsive。",
    "options": {
        "A": "錯誤。CVP 多年研究證實預測 fluid responsiveness 差 (AUC ~0.55)。",
        "B": "錯誤。PCWP 同樣 poor predictor，且需 PA catheter。",
        "C": "正確。SVV > 13% (dynamic) 為最可靠之預測指標 (限定條件)。",
        "D": "錯誤。Urine output 受多因素影響 (e.g. surgical stress、ADH、diuretic)。",
    },
    "guidelines": [
        "ESA 2015 Perioperative Hemodynamic：dynamic indicators preferred over static。",
        "Passive Leg Raise (PLR)：抬腿 45° × 1 min；CO ↑ ≥ 10% 預示 responsive；適用 spontaneous breathing。",
        "Fluid challenge：250 mL crystalloid 10-15 min；SV ↑ ≥ 10%。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 59 Fluid Management",
},
"P-GP-044": {  # positioning
    "mechanism": "Lithotomy 病人下肢 hip flexion + abduction + external rotation → common peroneal nerve (繞 fibular head) 易受壓迫；compartment syndrome 風險隨時間累積。",
    "options": {
        "A": "錯誤。Prone position 主要為 ulnar nerve at elbow、brachial plexus、eye、breast。",
        "B": "正確。Lithotomy → common peroneal nerve (fibular head) 為最常見。",
        "C": "錯誤。Lateral decubitus 主要影響 brachial plexus (dependent arm)。",
        "D": "錯誤。Beach chair 主要 risk 為 cerebral hypoperfusion；nerve injury 少見。",
    },
    "guidelines": [
        "ASA Practice Advisory for Prevention of Perioperative Peripheral Neuropathies 2018。",
        "AANA Position on Patient Positioning。",
        "Compartment syndrome：lithotomy > 4 hr 高風險；下肢出現 pain、pallor、paresthesia、paralysis 須評估。",
    ],
    "source": "Miller's Anesthesia 8/e, Ch. 41 Patient Positioning",
},
"P-GP-045": {  # ABG
    "mechanism": "Acid-base 分析步驟：(1) pH 判斷 acidemia/alkalemia；(2) 主導性 disorder (resp vs metabolic)；(3) compensation 適當度 (Winter's formula、Boston rules)；(4) anion gap 計算；(5) delta-delta。",
    "options": {
        "A": "錯誤。Acute respiratory acidosis 預期 HCO₃ ↑ 1 per 10 mmHg PaCO₂↑；此題 PaCO₂ 反而降。",
        "B": "正確。Metabolic acidosis (HCO₃ 12) + respiratory compensation (PaCO₂ 30，符合 Winter's 26-28)，數據略高代表 mild superimposed respiratory acidosis 或 inadequate compensation。",
        "C": "錯誤。Chronic respiratory acidosis HCO₃ ↑ 3-4 per 10 mmHg；此題 HCO₃ 降低。",
        "D": "錯誤。pH 7.22 為 acidemia，非 alkalosis。",
    },
    "guidelines": [
        "Anion gap = Na − (Cl + HCO₃)；正常 8-12 (加白蛋白校正 +2.5 per g/dL)。",
        "AG metabolic acidosis (MUDPILES)：Methanol、Uremia、DKA、Propylene glycol、Iron/INH、Lactic、Ethylene glycol、Salicylate。",
        "Non-AG (HARDUP)：Hyperalimentation、Acetazolamide、RTA、Diarrhea、Ureteroenteric fistula、Pancreatic fistula。",
    ],
    "source": "Pocket Anesthesia 3/e; Stewart Acid-Base approach",
},
"P-GP-046": {  # TURP syndrome
    "mechanism": "Monopolar TURP 需 nonconductive irrigation (glycine 1.5%、sorbitol、mannitol)，當 prostatic venous sinuses 開放 + 高壓沖洗 + 長時間手術，大量低渗液體吸收 → 急性 hyponatremia + glycine toxicity (visual、ammonia)。",
    "options": {
        "A": "錯誤。Hypoglycemia 不會引起 Na 112。",
        "B": "正確。TURP syndrome：acute hyponatremia + fluid overload + glycine toxicity。",
        "C": "錯誤。Septic encephalopathy 通常 fever + 感染源；Na 改變較緩。",
        "D": "錯誤。Air embolism 表現為突發 cardiovascular collapse + ETCO₂↓。",
    },
    "guidelines": [
        "Bipolar TURP (saline irrigation) 已大量取代 monopolar，TURP syndrome 發生率下降。",
        "Acute symptomatic hyponatremia (< 48h、seizure/coma) 可較快矯正：3% NaCl 100-150 mL × 2-3 doses 直到 Na ↑ 4-6 mEq/L。",
        "Chronic asymptomatic：避免 > 8-10 mEq/L/day 矯正 (ODS 風險)。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e",
},
"P-GP-047": {  # LEMON
    "mechanism": "Difficult airway prediction 單一指標 sensitivity 30-70%、specificity 70-90%；組合評估提升 PPV。困難呼吸道之多 axes：difficult BMV、difficult intubation、difficult SAD、difficult FONA。",
    "options": {
        "A": "錯誤。單一 Mallampati 不夠。",
        "B": "錯誤。單一 TMD 不夠。",
        "C": "正確。LEMON: Look (face features)、Evaluate 3-3-2 (mouth opening、hyoid-mental、thyroid-mouth)、Mallampati、Obstruction、Neck mobility。",
        "D": "錯誤。BMI 與 OSA 相關但單一不足。",
    },
    "guidelines": [
        "DAS 2015：困難呼吸道預測 + plan A/B/C/D。",
        "MACOCHA score：ICU 困難插管預測 (12 分制)。",
        "El-Ganzouri Risk Index：7 因素 multivariate 預測，AUC ~0.85。",
    ],
    "source": "Hagberg Airway Management 4/e",
},
"P-GP-048": {  # RSI
    "mechanism": "RSI 目的縮短 time-at-risk for aspiration (從 LOC 到 airway secure)。Pre-oxygenation 最大化 O₂ reserve；快速 induction agent + rapid-onset NMBA；避免 mask ventilation 防 gastric inflation。",
    "options": {
        "A": "正確。完整 RSI 流程：preox、induction (Etomidate 0.3 / Propofol)、Roc 1.2 / Sux 1.5、cricoid (爭議性)、直接插管。",
        "B": "錯誤。Slow induction + mask ventilation 違反 RSI 原則 (full stomach 風險)。",
        "C": "錯誤。LMA 不能可靠保護 airway，非 RSI 首選。",
        "D": "錯誤。NMBA 不可省略；自主呼吸無法確保 rapid intubation conditions。",
    },
    "guidelines": [
        "DAS 2015：Modified RSI (gentle bag ventilation if needed to prevent hypoxia)。",
        "Sellick maneuver 證據力不足，許多機構已不常規使用 (DAS allows but not mandatory)。",
        "兒童：Modified RSI with gentle PPV 防 hypoxia (兒童 FRC 小、O₂ consumption 高)。",
    ],
    "source": "Hagberg Airway Management 4/e Ch. 21",
},
"P-GP-049": {  # extubation
    "mechanism": "Extubation 是 anesthesia 高風險時段，併發症: laryngospasm、aspiration、negative pressure pulmonary edema、cardiovascular instability。",
    "options": {
        "A": "錯誤。意識清醒能執行指令是 awake extubation 標準。",
        "B": "錯誤。TOF ≥ 0.9 為前提條件。",
        "C": "正確。Deep extubation + 預期 laryngospasm 為高風險組合；應 awake extubation。",
        "D": "錯誤。穩定自主呼吸是 extubation criteria 之一。",
    },
    "guidelines": [
        "DAS Extubation Guidelines 2012：(1) Plan；(2) Prepare；(3) Perform；(4) Post-extubation care。",
        "高風險：obese、OSA、recent airway surgery、anaphylaxis、ICU 久 intubation、cervical instability。",
        "Strategies：awake、deep、bridging (e.g. exchange to LMA)、staged (with airway exchange catheter)。",
    ],
    "source": "DAS Extubation Guidelines 2012",
},
"P-GP-050": {  # laryngospasm
    "mechanism": "Laryngospasm 為 superior laryngeal nerve (internal branch) reflex 引起 vocal cords sustained closure。常於 stage 2 (delirium) 出現；secretions、surgical stimulation、light anesthesia 為誘因。",
    "options": {
        "A": "錯誤。Atropine 用於 bradycardia secondary to hypoxia，不能解 laryngospasm。",
        "B": "正確。CPAP 100% O₂ + Larson's point pressure + 加深麻醉 Propofol 0.5-1 mg/kg；持續 succinylcholine 0.1-0.5 mg/kg IV (或 IM 4 mg/kg)。",
        "C": "錯誤。氣管切開為極端 last resort，幾乎所有 laryngospasm 可藥物解除。",
        "D": "錯誤。LMA 不能解 laryngospasm，可能加重刺激。",
    },
    "guidelines": [
        "APAGBI Pediatric Difficult Airway Guidelines 2015。",
        "PALS：嚴重 desaturation → 100% O₂、bag-mask、必要時 PALS algorithm。",
        "預防：smooth induction、避免 stage 2 timing、URI 推遲 elective surgery 2-4 weeks。",
    ],
    "source": "Coté and Lerman's A Practice of Anesthesia for Infants and Children 6/e",
},
"P-GP-051": {  # neuraxial comparison
    "mechanism": "Spinal: 藥物直接進入 CSF (subarachnoid)，起效快、藥量小、密度差影響擴散。Epidural: 藥物在 epidural space，需擴散至神經根，起效慢、藥量大、可滴定。",
    "options": {
        "A": "錯誤。Spinal 起效最快 (< 5 min)、範圍由 dose + baricity + 病人姿勢決定，不易調整。",
        "B": "正確。Epidural 起效 10-20 min、catheter 可延長、滴定容易、麻醉範圍更彈性。",
        "C": "錯誤。Spinal PDPH 風險較高 (especially cutting needle、大 gauge)。",
        "D": "錯誤。兩者均有 sympathectomy；epidural 較緩 (segmental)，spinal 通常 dense 且廣泛。",
    },
    "guidelines": [
        "ASRA 2018：抗凝指引嚴格規範 neuraxial 時程。",
        "Combined Spinal-Epidural (CSE)：產科鎮痛常用，結合 spinal 起效快 + epidural 滴定。",
        "PDPH 預防：pencil-point needle (Whitacre、Sprotte) 較 cutting (Quincke) 顯著降低 PDPH。",
    ],
    "source": "Brown's Atlas of Regional Anesthesia 5/e",
},
"P-GP-052": {  # neuraxial contraindication
    "mechanism": "Epidural hematoma 為 catastrophic complication；風險因素 = uncorrected coagulopathy、抗凝藥未停。Infection at site 可入侵 epidural space → meningitis、epidural abscess。",
    "options": {
        "A": "錯誤。Mild AS 可考慮 epidural slow titration；severe AS 才是相對禁忌。",
        "B": "正確。病人拒絕、注射部位感染、未矯正 coagulopathy 為三大絕對禁忌。",
        "C": "錯誤。穩定高血壓非禁忌，反而 neuraxial 可控制 BP。",
        "D": "錯誤。Sickle cell disease 為 risk factor for vaso-occlusive crisis but not absolute contraindication。",
    },
    "guidelines": [
        "ASRA Anticoagulation 4/e (2018)：詳細時程依藥物。",
        "Aspirin 不需停 (繼續使用安全)。",
        "Clopidogrel 停 5-7 天；Prasugrel 7-10 天；Ticagrelor 5-7 天。",
        "Therapeutic LMWH 停 24h、Prophylactic 12h。",
    ],
    "source": "ASRA Anticoagulation Guidelines 4/e (2018)",
},
"P-GP-053": {  # interscalene
    "mechanism": "Interscalene block 注射部位 (C5-C6 nerve roots) 與 phrenic nerve (C3-C5) 解剖學上極接近，local anesthetic 擴散 100% block ipsilateral phrenic。",
    "options": {
        "A": "正確。Hemidiaphragmatic paresis 為 expected outcome，臨床上多無症狀，但呼吸儲備低者需注意。",
        "B": "錯誤。RLN block 為 transient hoarseness，可恢復。",
        "C": "錯誤。Pneumothorax 風險 < 1%。",
        "D": "錯誤。Cardiac arrest 罕見，但 vertebral artery injection LAST 可致命。",
    },
    "guidelines": [
        "ASRA 2018：Interscalene block 嚴重 COPD、單肺、嚴重肥胖、神經疾病為相對禁忌。",
        "Low-volume technique (10-15 mL) 可降低 phrenic block 率至 ~30%。",
        "Brachial plexus block options：interscalene (肩部)、supraclavicular (整個上肢)、infraclavicular、axillary (前臂、手)。",
    ],
    "source": "Brown's Atlas of Regional Anesthesia 5/e",
},
"P-GP-054": {  # PDPH
    "mechanism": "PDPH 因 CSF leakage 經 dural puncture site → 腦下垂、牽引 pain-sensitive structures (meninges、blood vessels、CN V/IX/X)。Postural 為特徵 (站立 CSF 壓力差最大)。",
    "options": {
        "A": "錯誤。SAH 為 thunderclap headache、不隨體位變化。",
        "B": "正確。Postural pattern 為 PDPH 特徵；conservative (床休、水分、caffeine、analgesia)；persistent → epidural blood patch 70-90% success。",
        "C": "錯誤。Cluster headache 為單側、自主神經症狀；無 dural puncture history。",
        "D": "錯誤。Meningitis 通常 fever + nuchal rigidity + 不隨姿勢明顯變化。",
    },
    "guidelines": [
        "ASRA 2010 PDPH Consensus。",
        "預防：pencil-point needle、最小 gauge、減少嘗試次數。",
        "EBP timing：症狀 24-48h 後執行成功率較佳；可重複 1-2 次。",
        "Differential：cortical vein thrombosis、subdural hematoma、preeclampsia (post-partum) 需鑑別。",
    ],
    "source": "Chestnut's Obstetric Anesthesia 6/e Ch. 30",
},
"P-GP-055": {  # sedation continuum
    "mechanism": "ASA Sedation Continuum 連續譜，任何鎮靜藥都可能引起意外深於預期 → anesthesiologist 必須具備 rescue 一階能力。",
    "options": {
        "A": "正確。Moderate sedation：對 verbal/light touch 反應；spontaneous ventilation；維持心血管。",
        "B": "錯誤。對 painful stimuli 有反應、ventilation 可能需輔助 = deep sedation。",
        "C": "錯誤。完全無反應 + intubation = general anesthesia。",
        "D": "錯誤。完全清醒非鎮靜。",
    },
    "guidelines": [
        "ASA Continuum of Depth of Sedation: Definition of General Anesthesia (2019)。",
        "TJC：Moderate sedation 由 non-anesthesiologist 執行需 credentialing。",
        "Procedural sedation common drugs：Midazolam + Fentanyl、Propofol、Ketamine、Dexmedetomidine。",
    ],
    "source": "ASA Standards & Practice Parameters",
},
"P-GP-056": {  # multimodal
    "mechanism": "Pain pathway 多階段 (transduction、transmission、modulation、perception)，每階段不同藥物作用。Combination 可協同作用、降低個別藥物副作用。",
    "options": {
        "A": "錯誤。單一高劑量 opioid 副作用大 (PONV、便秘、呼吸抑制、依賴)。",
        "B": "正確。Multimodal: paracetamol + NSAIDs/COX-2 + gabapentinoid + ketamine + dexmedetomidine + regional + opioid rescue。",
        "C": "錯誤。NSAIDs 有禁忌 (renal、bleeding、PUD、heart failure)。",
        "D": "錯誤。完全避免 opioid 不現實；rescue 適量使用。",
    },
    "guidelines": [
        "ASA Acute Pain Management Practice Guidelines 2012。",
        "ERAS Society：每個 protocol 強調 opioid-sparing multimodal。",
        "Procedure-specific PROSPECT recommendations。",
    ],
    "source": "Pocket Anesthesia 3/e Pain Management",
},

# ============ SPECIAL POPULATIONS / PROCEDURES ============
"P-SP-057": {  # AS
    "mechanism": "Severe AS LV hypertrophy、stiff、preload-dependent、CO 不能即時增加。Tachycardia 縮短 diastolic 冠脈灌流；hypotension 引發 subendocardial ischemia → arrhythmia → 惡性循環。",
    "options": {
        "A": "正確。Sinus rhythm (preserved 'atrial kick' 30% CO)、normal-slow HR 60-80、normal preload、high SVR、avoid hypotension。",
        "B": "錯誤。Tachycardia 在 AS 為災難。",
        "C": "錯誤。Afterload 降低 → systemic hypotension + 冠脈灌流降。",
        "D": "錯誤。AS preload-dependent，hypovolemia 不可。",
    },
    "guidelines": [
        "ACC/AHA 2014 Valvular Heart Disease：Severe AS AVA < 1.0、gradient > 40、velocity > 4.0。",
        "TAVR 已成為許多 high-risk AS 病人首選 (PARTNER trial)。",
        "Anesthetic：通常 GA + invasive monitoring；avoid spinal (sudden sympathectomy)。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e Ch. Cardiovascular",
},
"P-SP-058": {  # ECMO
    "mechanism": "VA-ECMO 血液從 venous (femoral vein/RA) → membrane oxygenator → arterial (femoral artery/Aorta) 提供 cardio-pulmonary support；VV-ECMO 從 vein → oxygenator → vein 僅 respiratory support。",
    "options": {
        "A": "錯誤。單純嚴重 hypoxia → VV-ECMO 足夠。",
        "B": "正確。VA-ECMO 提供 biventricular + pulmonary support。",
        "C": "錯誤。Sepsis 循環穩定不需 ECMO。",
        "D": "錯誤。輕度 hypotension 應先 medical therapy。",
    },
    "guidelines": [
        "ELSO (Extracorporeal Life Support Organization) Guidelines。",
        "ECPR：witnessed arrest + initial shockable rhythm + young + reversible cause → 5-min CPR 仍 PEA 考慮 ECPR。",
        "Anticoagulation：unfractionated heparin、ACT 180-220 sec。",
        "併發症：LV distension (need vent)、limb ischemia、bleeding、Harlequin (north-south syndrome)。",
    ],
    "source": "Miller's Anesthesia 8/e Ch. 67",
},
"P-SP-059": {  # tamponade
    "mechanism": "Pericardial fluid 累積 → intrapericardial pressure ↑ → 影響 venous return → CO ↓。Diastolic equalization of intracardiac pressures 為 hallmark。",
    "options": {
        "A": "正確。Beck's Triad: hypotension + muffled heart sounds + JVD。",
        "B": "錯誤。Hyperventilation 與 tamponade 無關。",
        "C": "錯誤。Fever/cough 與 tamponade 無關 (除非 infectious cause)。",
        "D": "錯誤。Hypoxia 非主導；初期 SpO₂ 可正常。",
    },
    "guidelines": [
        "Echo 為 diagnostic + guidance (subxiphoid 或 apical 穿刺)。",
        "Pulsus paradoxus > 10 mmHg、Kussmaul sign (神奇 JVP 隨吸氣升)。",
        "麻醉誘導：Ketamine 0.5-1 mg/kg + Etomidate；保留自主呼吸；avoid PPV until drainage。",
    ],
    "source": "Miller's Anesthesia 8/e Ch. 66",
},
"P-SP-060": {  # OLV
    "mechanism": "OLV 引發 V/Q mismatch；nonventilated lung HPV (hypoxic pulmonary vasoconstriction) 自然分流血流至 ventilated lung。Lung-protective ventilation 減少 VILI、改善 oxygenation。",
    "options": {
        "A": "錯誤。過高 PEEP 反而 overdistension、降低 venous return。",
        "B": "正確。Low TV 4-6 mL/kg IBW + moderate PEEP + FiO₂ as needed + recruitment + CPAP on non-ventilated。",
        "C": "錯誤。停止 OLV 不總是可行；應先嘗試 troubleshoot。",
        "D": "錯誤。高 TV 12 mL/kg 為過時，會引起 VILI。",
    },
    "guidelines": [
        "AAGBI Thoracic Anesthesia 2010。",
        "Hypoxia algorithm: (1) FiO₂↑；(2) confirm DLT 位置 (fiberoptic)；(3) CPAP non-ventilated；(4) recruitment ventilated；(5) PEEP；(6) clamp PA。",
        "DLT vs Bronchial blocker：DLT 較快、suction 容易；BB 適合 ETT 已 in situ、difficult airway。",
    ],
    "source": "Miller's Anesthesia 8/e Ch. 65 Thoracic",
},
"P-SP-061": {  # ETT depth
    "mechanism": "Right mainstem bronchus 與 trachea 夾角較小 (~25° vs left 45°)、較短 (2.5 vs 5 cm)，故 ETT 過深易進入右 mainstem。",
    "options": {
        "A": "錯誤。14 cm 過淺，cuff 在 vocal cords 之上。",
        "B": "正確。女 21 cm、男 23 cm at lip；對應 ETT tip 2-3 cm 上 carina。",
        "C": "錯誤。27 cm 過深，多會進右 mainstem。",
        "D": "錯誤。Tidal volume 不能判定 ETT 位置。",
    },
    "guidelines": [
        "Confirmation: bilateral breath sounds + symmetric chest rise + capnography + CXR。",
        "Neck flexion → ETT 進深 ~2 cm；extension → 退 ~2 cm。",
        "兒童 depth (cm) = age/2 + 12 (for cuffed ETT)。",
    ],
    "source": "Hagberg Airway Management 4/e",
},
"P-SP-062": {  # TBI
    "mechanism": "Secondary brain injury 由 hypotension、hypoxia、hypercarbia、hyperthermia、hyperglycemia 加重。Primary injury 不可逆，但 secondary 可預防 — 為麻醉處置核心。",
    "options": {
        "A": "錯誤。Hyperventilation (PaCO₂ 25-30) 短期可降 ICP 但長期會加重 ischemia；SBP < 90 已知增加死亡率。",
        "B": "正確。BTF 4/e：避免 hypotension (SBP > 100)、hypoxia、CPP 60-70、normocapnia 35-40。",
        "C": "錯誤。Hypercapnia 增加 CBF + ICP。",
        "D": "錯誤。Aggressive hypothermia 證據不足，治療性低溫於 TBI 已不建議常規。",
    },
    "guidelines": [
        "Brain Trauma Foundation 4/e (2016) Guidelines for Management of Severe TBI。",
        "ICP > 22 mmHg 治療；Tier 1 (head elevation、analgesia、sedation、CSF drainage)、Tier 2 (mannitol/3%、hyperventilation)、Tier 3 (barbiturate、craniectomy)。",
        "Mannitol 0.25-1 g/kg；3% saline 250 mL or 23.4% NaCl 30 mL 為 hyperosmotic options。",
        "避免 N₂O (增 CBF、可能 air embolism)、ketamine 爭議性。",
    ],
    "source": "Brain Trauma Foundation 4/e Guidelines (2016)",
},
"P-SP-063": {  # VAE
    "mechanism": "Sitting position 手術部位高於心臟 + open venous structures (e.g. 顱骨之 emissary vein、suboccipital) + 負壓 → air 吸入 → 心臟右側、肺循環 → CV collapse。",
    "options": {
        "A": "錯誤。Hypertension 非典型 sitting position 併發症。",
        "B": "正確。VAE 25-45% 發生率；TEE 為最敏感監測；ETCO₂↓、ETN₂↑、SpO₂↓、CV collapse。",
        "C": "錯誤。Hypothermia 可發生但非主要併發症。",
        "D": "錯誤。Hyperglycemia 非直接相關。",
    },
    "guidelines": [
        "Sitting Craniotomy Anesthesia：preop TEE 排除 PFO (絕對禁忌)；precordial Doppler + ETCO₂ + ETN₂ + CVP catheter (RA tip) 監測。",
        "VAE 處置：flood field with saline、bilateral jugular compression、aspirate from RA catheter、Trendelenburg + left lateral、100% O₂、stop N₂O、CV support。",
        "Quadriplegia (sitting) 罕見但悲劇性併發症 (spinal cord stretch)。",
    ],
    "source": "Miller's Anesthesia 8/e Ch. 70",
},
"P-SP-064": {  # CEA
    "mechanism": "CEA 期間 cross-clamp 同側 ICA → contralateral collateral (Circle of Willis) 維持 perfusion；20% 病人 collateral 不足需 shunt。Awake 病人最直接評估方法為神經學檢查。",
    "options": {
        "A": "錯誤。SpO₂ 不反映 cerebral perfusion。",
        "B": "正確。Awake (regional) 直接神經評估；GA 用 surrogate (NIRS、EEG、SSEP、stump pressure)。",
        "C": "錯誤。Routine CT angio 不切實際。",
        "D": "錯誤。BP cuff 不評估 cerebral perfusion。",
    },
    "guidelines": [
        "SVS (Society for Vascular Surgery) Guidelines：Awake vs GA 結果類似 (GALA trial)，依術者偏好。",
        "Post-CEA 嚴格控制 BP (避免 cerebral hyperperfusion syndrome)。",
        "Shunt 使用：選擇性 (依 monitor) vs 常規；爭議性 — selective 多數中心採用。",
    ],
    "source": "Miller's Anesthesia 8/e Ch. 71 Vascular Surgery",
},
"P-SP-065": {  # tourniquet
    "mechanism": "Tourniquet inflation 隔絕遠端循環，遠端肢體 ischemic metabolism 累積 lactate、K⁺、CO₂、ROS。Release 後 systemic washout → transient hyperkalemia + acidosis + ETCO₂ 急升。",
    "options": {
        "A": "錯誤。Release 後通常 hypotension，非 hypertension (vasodilation + reperfusion)。",
        "B": "正確。Reperfusion syndrome 經典表現。",
        "C": "錯誤。Tourniquet inflation 與 glycemic 改變無關。",
        "D": "錯誤。Inflation tourniquet pain 通常 hypertension、tachycardia，非 bradycardia。",
    },
    "guidelines": [
        "AAOS：Tourniquet 上肢 SBP+50、下肢 SBP+100 mmHg；time < 2h；每 90 min 釋放 15 min。",
        "禁忌：嚴重 PAD、recent DVT、severe crush injury、sickle cell crisis history。",
        "Tourniquet pain：充氣 45-60 min 後 deep aching；treat with deeper anesthesia or alpha-2 agonist。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e",
},
"P-SP-066": {  # fat embolism
    "mechanism": "Long bone fracture 骨髓脂肪滴釋出 → 進入 venous 循環 → pulmonary + systemic embolism。也可由 chemical mediators 啟動 inflammatory cascade。",
    "options": {
        "A": "錯誤。Hyperthermia + 發疹非特徵 (雖可有 petechiae)。",
        "B": "正確。Gurd's criteria: hypoxemia + neurologic + petechiae，24-72h 內發生。",
        "C": "錯誤。即時 cardiac arrest 較像 fat embolism syndrome 暴發型，非常見。",
        "D": "錯誤。Hematuria/血便 非典型表現。",
    },
    "guidelines": [
        "AAOS：Long bone fracture 早期 (< 24h) 固定可降低 FES 風險。",
        "處置：support care、oxygen、ventilation；類固醇證據不一致。",
        "Differential：PE、ARDS、pneumonia、TBI。",
    ],
    "source": "Pocket Anesthesia 3/e",
},
"P-SP-067": {  # tonsil bleeding
    "mechanism": "Tonsillectomy 出血 24h 內 (primary) 通常 surgical bleeding；5-10 天 (secondary) 由 eschar separation。病人吞入大量血液 → full stomach + 可能 hypovolemia。",
    "options": {
        "A": "錯誤。標準 NPO 假設不適用 — 病人吞血。",
        "B": "正確。Full stomach RSI、suction 預備、可選 lateral position、預備血品。",
        "C": "錯誤。GI 排空時間不可預測；不可等待。",
        "D": "錯誤。局部麻醉無法控制 active 出血。",
    },
    "guidelines": [
        "APAGBI Pediatric Difficult Airway 2015。",
        "麻醉誘導：Ketamine + Etomidate 維持循環。",
        "拔管：完全清醒、protective reflexes、考慮 left lateral head-down。",
    ],
    "source": "Coté and Lerman's A Practice of Anesthesia for Infants and Children 6/e",
},
"P-SP-068": {  # IOP
    "mechanism": "Succinylcholine 引起 extraocular muscle 持續強直收縮 → globe pressure ↑。Open globe 時 IOP 上升可擠出 vitreous → 永久視力喪失。",
    "options": {
        "A": "錯誤。Propofol 降低 IOP (vasodilation + relaxation)。",
        "B": "錯誤。Sevoflurane 降低 IOP。",
        "C": "正確。Succinylcholine ↑ IOP 6-8 mmHg；open globe 相對禁忌。",
        "D": "錯誤。Etomidate 降低 IOP (與 propofol 類似)。",
    },
    "guidelines": [
        "Open Globe Injury Anesthesia：RSI with rocuronium (high dose 1.2 mg/kg) for rapid intubation without succinylcholine。",
        "Oculocardiac reflex：trigeminovagal arc；發生 bradycardia 處置 (1) 停止刺激；(2) atropine 0.02 mg/kg。",
        "MAC for cataract：retrobulbar/peribulbar/sub-Tenon block + light sedation (avoid deep sedation; co-operative awake patient required)。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e",
},
"P-SP-069": {  # pregnancy physiology
    "mechanism": "Pregnancy 生理改變由 progesterone、estrogen 主導 + 機械性子宮壓迫 + 胎盤循環。MAC 下降可能與 endogenous opioid、progesterone 有關。",
    "options": {
        "A": "正確。子宮 cephalad displacement 減少 FRC 20%。",
        "B": "正確。基礎代謝率上升、O₂ 消耗 ↑ 20%、minute ventilation ↑ 50% (TV↑ > RR↑)。",
        "C": "錯誤。MAC 「下降」30-40%，非上升。",
        "D": "正確。Blood volume 增 30-50%；plasma > RBC → physiologic anemia。",
    },
    "guidelines": [
        "AAGBI/OAA Obstetric Anaesthesia：> 20 weeks 應 left uterine displacement 15-30°。",
        "Difficult airway 風險：edema (especially preeclampsia)、breast (large)、weight gain、Mallampati upgrade during labor。",
        "Rapid desaturation 需高效 pre-oxygenation。",
    ],
    "source": "Chestnut's Obstetric Anesthesia 6/e Ch. 2",
},
"P-SP-070": {  # MgSO4
    "mechanism": "MgSO₄ 作用機轉：(1) NMDA receptor 阻斷；(2) Ca²⁺ channel 阻斷；(3) 直接 vasodilation。Therapeutic range 4-8 mg/dL；> 10 mg/dL respiratory depression；> 15 cardiac arrest。",
    "options": {
        "A": "錯誤。Blood glucose 不主要受 Mg 影響。",
        "B": "正確。DTR 為 early warning (loss at 8-10 mg/dL)；RR、UO、Mg level 為核心監測。",
        "C": "錯誤。EEG 監測非常規。",
        "D": "錯誤。Ferritin 與 Mg 無關。",
    },
    "guidelines": [
        "ACOG Practice Bulletin 222 (2020)：MgSO₄ 4-6 g IV loading + 1-2 g/h infusion 至產後 24 h。",
        "Toxicity 處置：停藥 + calcium gluconate 1 g IV slow。",
        "MgSO₄ potentiate NMBA — 減量 50%；可用 cisatracurium、rocuronium with sugammadex。",
        "Antihypertensive：Labetalol IV 20 mg → 40 mg → 80 mg；Hydralazine 5-10 mg IV；Nifedipine 10 mg PO。",
    ],
    "source": "ACOG Practice Bulletin 222 (2020); Chestnut 6/e Ch. 35",
},
"P-SP-071": {  # CS anesthesia
    "mechanism": "Spinal anesthesia 為 elective CS 首選因素：起效快 (< 5 min)、可靠麻醉、母體 airway 風險低、藥物胎兒暴露少。Hypotension 為主要副作用，phenylephrine 預防。",
    "options": {
        "A": "錯誤。GA 用於 emergency、neuraxial 禁忌、failed regional。",
        "B": "正確。Single-shot spinal Bupivacaine 12 mg + Fentanyl 15 µg + Morphine 0.1 mg 為標準組合。",
        "C": "錯誤。Local infiltration 不足以 CS。",
        "D": "錯誤。Mask inhalation 不安全 (full stomach)。",
    },
    "guidelines": [
        "ACOG Practice Bulletin 209 (2019)：Anesthesia for Obstetrics。",
        "Phenylephrine prophylactic infusion 50-100 µg/min 顯著降低 hypotension + 改善 fetal acid-base。",
        "Hypotension 處置：left uterine displacement、co-load crystalloid 10 mL/kg、phenylephrine bolus。",
        "Failed spinal: CSE、epidural top-up、或 GA。",
    ],
    "source": "Chestnut's Obstetric Anesthesia 6/e Ch. 26",
},
"P-SP-072": {  # AFE
    "mechanism": "AFE 確切機轉未明；amniotic fluid + fetal antigens 進入母體循環引發類過敏反應 (anaphylactoid)。經典三聯：hypotension、hypoxemia、coagulopathy。",
    "options": {
        "A": "錯誤。AFE 突發、急性，非緩慢。",
        "B": "正確。突發 CV collapse + hypoxemia + DIC 為 hallmark。",
        "C": "錯誤。頭痛非典型。",
        "D": "錯誤。Postpartum infection 緩慢、伴 fever、與 AFE 不同。",
    },
    "guidelines": [
        "AFE Foundation：診斷為 clinical (Clark criteria 2016)：(1) acute hypotension/cardiac arrest；(2) acute hypoxia；(3) coagulopathy；(4) onset during labor/CS or within 30 min postpartum；(5) 無其他解釋。",
        "處置：(1) 高品質 CPR；(2) Perimortem CS within 5 min if no ROSC and ≥ 20 weeks；(3) Massive transfusion 1:1:1；(4) ICU + ECMO 考慮。",
        "A-OK protocol (Atropine + Ondansetron + Ketorolac)：新興、爭議性，部分中心嘗試。",
    ],
    "source": "Chestnut's Obstetric Anesthesia 6/e Ch. 38",
},
"P-SP-073": {  # pediatric airway
    "mechanism": "兒童氣道與成人差異隨年齡漸減，~8 歲後接近成人。傳統教科書說 cricoid 最狹窄、近年動態 MRI 認為 vocal cords 仍是最窄，但兒童氣道整體 funnel-shaped。",
    "options": {
        "A": "正確。Anatomical differences 經典。",
        "B": "正確。Larynx position 較高 (C3-C4 vs 成人 C5-C6)。",
        "C": "錯誤。傳統教科書 cricoid 最窄；新研究 vocal cords 最窄但 cricoid 仍 functionally critical。",
        "D": "正確。Occiput 突出，supine 自然 sniffing position 不需 shoulder roll。",
    },
    "guidelines": [
        "Modified Cole's formula: cuffed ETT 內徑 (mm) = age/4 + 3.5；uncuffed = age/4 + 4。",
        "Cuffed ETT 已 widely accepted in pediatrics (從新生兒起)；APA、AAP support。",
        "MAC by age: newborn 0.87、infant 1 mo 1.20、6 mo 1.20、3 yr 0.95、adult 0.7-0.8。",
    ],
    "source": "Coté and Lerman 6/e Ch. 14 Pediatric Airway",
},
"P-SP-074": {  # pediatric induction
    "mechanism": "嬰幼兒缺乏 IV access、合作差，sevoflurane 為理想：low blood-gas coefficient (0.65)、pleasant smell、minimal airway irritation、rapid uptake。",
    "options": {
        "A": "正確。Inhalation induction with sevoflurane 為小兒最常用。",
        "B": "錯誤。Awake IV insertion 對 1 歲嬰兒既痛苦又困難。",
        "C": "錯誤。IM ketamine 用於 uncooperative、IV 困難情境，非 elective routine。",
        "D": "錯誤。Awake intubation 兒童極困難且 traumatic。",
    },
    "guidelines": [
        "APAGBI Guidelines：Pre-medication (oral midazolam 0.5 mg/kg)、parental presence。",
        "Sevoflurane induction：8% in O₂ 或 N₂O/O₂ mix；快速 induction 約 60 sec 意識消失。",
        "Stage 2 期間 (excitement、airway irritability) laryngospasm 風險高，需 deep enough before manipulation。",
    ],
    "source": "Coté and Lerman 6/e Ch. 6",
},
"P-SP-075": {  # pediatric fluid
    "mechanism": "Pediatric dehydration 分 mild (5%)、moderate (10%)、severe (15%)。Fluid resuscitation 採 isotonic crystalloid bolus，避免 hypotonic (D5W) 引起 hyponatremia。",
    "options": {
        "A": "錯誤。D5W 為 hypotonic，引起 hyponatremia 風險。",
        "B": "正確。Isotonic crystalloid (LR / 0.9% NaCl) 20 mL/kg bolus；重新評估後可重複至 60 mL/kg 後考慮 blood、ICU。",
        "C": "錯誤。Hypertonic saline 用於 severe symptomatic hyponatremia 或 head injury。",
        "D": "錯誤。Colloid 兒童 routine 不建議。",
    },
    "guidelines": [
        "APA 2013：Pediatric maintenance and resuscitation 使用 isotonic fluid。",
        "Hypoglycemia 風險：嬰兒 IV fluid 加 D5 glucose maintenance。",
        "Shock 不改善：考慮其他原因 (sepsis、cardiac、surgical bleeding) + ICU。",
    ],
    "source": "Coté and Lerman 6/e Ch. 8 Fluid Management",
},
"P-SP-076": {  # pediatric propofol
    "mechanism": "兒童 propofol mg/kg dose 較成人高，因 (1) 較大 Vd (lipid stores)；(2) 較快 hepatic clearance；(3) 較高 CNS protection threshold。新生兒例外 (immature liver)。",
    "options": {
        "A": "錯誤。0.5 mg/kg 過低，無法 induction。",
        "B": "錯誤。1 mg/kg 為新生兒、敏感族群。",
        "C": "正確。2.5-3 mg/kg 為 healthy child induction dose。",
        "D": "錯誤。5 mg/kg 超量、心血管副作用大。",
    },
    "guidelines": [
        "PRIS (Propofol Infusion Syndrome)：dose > 4 mg/kg/h × > 48h；兒童尤其；FDA black box warning for pediatric ICU。",
        "Maintenance TIVA 兒童：propofol 100-250 µg/kg/min。",
        "Anti-emetic property：propofol bolus 10-20 mg 可治療 PONV。",
    ],
    "source": "Coté and Lerman 6/e Ch. 13",
},
"P-SP-077": {  # geriatric
    "mechanism": "老年生理：CNS atrophy、cerebral autoregulation 窄；心 reserve↓、stiff vasculature；renal/hepatic clearance↓；muscle mass↓、frailty；多重共病、polypharmacy。",
    "options": {
        "A": "錯誤。盲目用成人劑量會 overdose。",
        "B": "正確。MAC↓ 6%/decade；藥物劑量普遍下調 20-50%；謹防 polypharmacy + POD/POCD。",
        "C": "錯誤。Hypothermia 風險增加 (low BMR、 thin skin)；應主動保溫。",
        "D": "錯誤。Baroreflex 鈍化 → 易 hypotension。",
    },
    "guidelines": [
        "ASA Brain Health Initiative：Perioperative neurocognitive disorders。",
        "ESA POCD Guidelines。",
        "Avoid Beers Criteria drugs：benzodiazepine、anticholinergic、meperidine、 long-acting opioid。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e Ch. Aging",
},
"P-SP-078": {  # POD
    "mechanism": "POD 機轉複雜：neurotransmitter imbalance (acetylcholine↓、dopamine↑)、neuroinflammation、cerebral hypoperfusion、 sleep-wake disturbance。",
    "options": {
        "A": "錯誤。Benzodiazepine 為 POD 主要可避免危險因子 (deliriogenic)。",
        "B": "正確。HELP/ABCDEF bundle：multimodal opioid-sparing、normal sleep、early mobilization、reorient、family presence、glasses/hearing aids、infection control。",
        "C": "錯誤。完全鎮靜增加 ICU delirium、長期 cognition 差。",
        "D": "錯誤。Anticholinergic 加重 delirium。",
    },
    "guidelines": [
        "ESA POCD/Delirium Guidelines 2017。",
        "ASA Brain Health Initiative：Perioperative neurocognitive disorders。",
        "Three subtypes: hyperactive (~25%)、hypoactive (易漏診、~50%)、mixed (~25%)。",
        "DSM-5 diagnosis: acute、fluctuating、attention deficit、cognitive change。",
    ],
    "source": "Miller's Anesthesia 8/e Ch. 80 Geriatric Anesthesia",
},
"P-SP-079": {  # trauma
    "mechanism": "Hemorrhagic shock 病人 cardiac output 已賴 endogenous catecholamines 維持；高劑量 propofol 解除 sympathetic tone → 立即 collapse。Etomidate (hemodynamic stable, adrenal suppression caveat)、Ketamine (sympathomimetic) 為較佳選擇。",
    "options": {
        "A": "錯誤。Propofol 2.5 mg/kg 可致命。",
        "B": "正確。Etomidate / Ketamine 低劑量 + vasopressor 預備 + MTP。",
        "C": "錯誤。Pure fentanyl 不能 induction，意識仍存。",
        "D": "錯誤。Inhalation induction 太慢、不安全 (full stomach)。",
    },
    "guidelines": [
        "ATLS 10/e (2018)：ABCDE、primary/secondary survey、massive transfusion。",
        "Damage Control Resuscitation：(1) Permissive hypotension (SBP 80-90，TBI 例外 > 110)；(2) Hemostatic resuscitation 1:1:1；(3) Limit crystalloid。",
        "TXA：CRASH-2 證實 < 3h 內 1 g IV bolus + 1 g infusion 8h 降低死亡率。",
        "MTP activation criteria：ABC score、shock index > 1。",
    ],
    "source": "ATLS 10/e (2018); Pocket Anesthesia 3/e",
},
"P-SP-080": {  # burn
    "mechanism": "Burn、prolonged immobilization、denervation、severe sepsis 引起 extrajunctional AChR up-regulation (immature γ-subunit、α7)。Succinylcholine activates 大量 receptors → 大量 K⁺ efflux → hyperkalemic cardiac arrest。",
    "options": {
        "A": "錯誤。Pseudocholinesterase 與燒傷無關。",
        "B": "正確。Receptor up-regulation 從 24h 後開始，持續至傷口完全癒合 + 1-2 年。",
        "C": "錯誤。Succinylcholine 不引起 bronchospasm。",
        "D": "錯誤。癲癇非 succinylcholine + burn 主要併發症。",
    },
    "guidelines": [
        "ABA (American Burn Association) Guidelines。",
        "燒傷對 nondepolarizing NMBA 有 resistance (受體增加 + 蛋白改變)，rocuronium 劑量需 ×2-3。",
        "Parkland formula: 4 mL × kg × %TBSA over 24h (1st half in 8h、2nd half in 16h)；LR preferred。",
        "Airway: 嚴重 face/neck burn 24h 內可快速 swelling，早期 prophylactic intubation。",
    ],
    "source": "Miller's Anesthesia 8/e Ch. 81 Trauma & Burn",
},
"P-SP-081": {  # ESRD
    "mechanism": "ESRD 病人 GFR < 15、accumulation of renally-excreted drugs and metabolites。Morphine M6G 強效 active metabolite；meperidine normeperidine 神經毒；NMBA 之 some 經腎排。",
    "options": {
        "A": "錯誤。Cisatracurium 經 Hofmann elimination (organ-independent)，安全。",
        "B": "正確。Morphine、Meperidine 兩者 metabolite 蓄積為高風險。",
        "C": "錯誤。Propofol 主要肝、CNS metabolism，安全。",
        "D": "錯誤。Sevoflurane Compound A 雖理論腎毒，臨床上低流速使用安全。",
    },
    "guidelines": [
        "KDIGO Perioperative Acute Kidney Injury Guidelines。",
        "Opioid choice in ESRD: Fentanyl、Remifentanil、Hydromorphone (with caution) safer than Morphine、Meperidine。",
        "NMBA: Cisatracurium、Atracurium safer (Hofmann elimination)；Rocuronium、Vecuronium 延長作用。",
        "Avoid NSAIDs in CKD。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e Ch. Renal",
},
"P-SP-082": {  # cirrhosis
    "mechanism": "Cirrhosis 全身性影響：drug metabolism (Phase I CYP↓、Phase II glucuronidation 較 preserved)、protein binding (albumin↓)、Vd 增、coagulation abnormalities、portal hypertension complications、HE。",
    "options": {
        "A": "錯誤。肝代謝藥物 clearance 明顯下降。",
        "B": "正確。多重病理生理影響藥物選擇、劑量、監測。",
        "C": "錯誤。Coagulopathy 為 hallmark (INR↑、低 albumin、低 plt)；但近年認為亦有 prothrombotic 風險。",
        "D": "錯誤。Acetaminophen 應 ≤ 2 g/day；高劑量肝毒性。",
    },
    "guidelines": [
        "MELD score：> 15 顯著手術風險；> 20 elective surgery 延後。",
        "AASLD Guidelines for portopulmonary HTN、HRS、SBP。",
        "首選 NMBA：Atracurium / Cisatracurium (Hofmann)；fentanyl、remifentanil safer than morphine。",
        "Avoid benzodiazepine in advanced disease (precipitate HE)。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e Ch. Liver",
},
"P-SP-083": {  # bariatric
    "mechanism": "肥胖藥物動力學：(1) Lipophilic drugs (propofol、benzo、long-acting opioid)：Vd↑ with TBW；(2) Hydrophilic drugs (NMBA、antibiotics)：Vd 接近 LBW。Loading dose calculation 與 maintenance dose 須分別計算。",
    "options": {
        "A": "錯誤。盲目 TBW 計算所有藥物會 overdose。",
        "B": "正確。Propofol induction LBW、maintenance IBW；succinylcholine TBW (短作用、酵素飽和)；rocuronium IBW。",
        "C": "錯誤。Pre-oxygenation 非常重要，肥胖 FRC↓ desaturation 極快。",
        "D": "錯誤。Supine 加劇 atelectasis；ramped position 改善 laryngoscopy + FRC。",
    },
    "guidelines": [
        "Society for Obesity and Bariatric Anaesthesia (SOBA) Guidelines。",
        "Ramped position：tragus 對齊 sternal notch (耳對齊胸骨)。",
        "PEEP 5-10 cmH₂O 維持 FRC；recruitment maneuver。",
        "Multimodal analgesia (avoid opioid-induced respiratory depression in OSA)。",
        "VTE prophylaxis：mechanical + chemical (UFH or LMWH)；高 BMI 劑量可能需調整。",
    ],
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e Ch. Obesity",
},
}

# Load original questions
with open('/tmp/np-anesthesia/practice_questions.json') as f:
    questions = json.load(f)

# Merge enhancements
updated = 0
for q in questions:
    qid = q["id"]
    if qid in E:
        enh = E[qid]
        if "mechanism" in enh:
            q["explanation"]["mechanism"] = enh["mechanism"]
        if "options" in enh:
            q["explanation"]["options"] = enh["options"]
        if "guidelines" in enh:
            q["explanation"]["guidelines"] = enh["guidelines"]
        if "source" in enh:
            q["source"] = enh["source"]
        updated += 1

print(f"Enhanced {updated}/{len(questions)} questions")

# Save
with open('/tmp/np-anesthesia/practice_questions.json', 'w') as f:
    json.dump(questions, f, ensure_ascii=False, separators=(',', ':'))

import os
print(f"File size: {os.path.getsize('/tmp/np-anesthesia/practice_questions.json')/1024:.0f}KB")
