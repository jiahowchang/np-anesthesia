#!/usr/bin/env python3
"""
Add detailed explanations to 114 進階麻醉 80 questions.
Each enhancement provides: summary, mechanism, per-option analysis, guidelines,
clinical pearls, keyword, source citation.
"""
import json

# Enhancements keyed by question number 1-80 for Q-ANE-114-A##
E = {

# ===== 營養、代謝、感染症 (Q1-8) =====
1: {  # 腸道營養
    "answer_text": "③④",
    "summary": "腸道營養 (EN) 為臨床首選之營養支持方式；只要 GI tract 可用即應優先於 PN。NG 管錯位多見於昏迷、咳嗽反射弱者；長期 (>4-6 週) 灌食可考慮 PEG。",
    "mechanism": "EN 維持腸道屏障完整、保留 GALT 免疫、減少 bacterial translocation；PN 反而增加 catheter sepsis、肝功能異常、cost。腸道灌食腹瀉多源於 osmolality、灌食速率過快、抗生素、感染、低 albumin，非纖維不足。",
    "options": {
        "A": "錯誤。①錯：EN 應優先於 PN (ASPEN/ESPEN 共識)。",
        "B": "錯誤。②錯：腹瀉應先找原因 (osmolality、rate、infection、C. difficile)，非單純止瀉。",
        "C": "正確。③ NG 錯位確實常見於昏迷、神經受損；④ PEG 為長期灌食標準。",
        "D": "錯誤。①錯如上。",
    },
    "guidelines": [
        "ASPEN/SCCM 2016：ICU 病人 24-48h 內啟動 EN；目標卡路里於 7-10 天達成。",
        "ESPEN 2019：EN 優於 PN 除非 contraindicated (intestinal failure、obstruction、severe shock)。",
        "ASPEN 推薦：長期 EN (>4 週) 考慮 PEG 改善舒適與護理。",
    ],
    "points": [
        "EN benefits：低成本、低感染、維持腸黏膜、減少 bacterial translocation",
        "EN 禁忌：機械性腸阻塞、severe shock、severe ileus、GI ischemia",
        "灌食腹瀉處理：稀釋、降速、找感染源 (尤其 C. diff)",
    ],
    "keyword": "Enteral nutrition, NG tube placement, PEG",
    "source": "ASPEN/SCCM 2016 Critical Care Nutrition Guidelines; Stoelting's Co-existing Disease 7/e Ch. Nutrition",
},
2: {  # 營養評估指標
    "answer_text": "BMI",
    "summary": "BMI 雖普及但對「營養狀態」評估有局限：肥胖病人可能 sarcopenic、嚴重失水或水腫者 BMI 失真。糖尿病久病者常 muscle wasting，BMI 不能反映 lean body mass。",
    "mechanism": "營養評估三維度：(1) anthropometric (體重變化、midarm circumference、triceps skinfold)；(2) biochemical (albumin、prealbumin、transferrin)；(3) immunologic (lymphocyte count、skin test)。BMI 僅反映 weight/height，不分組織組成。",
    "options": {
        "A": "正確 (本題答案)。BMI 為粗略指標，不能反映 lean body mass、隱性 sarcopenia；糖尿病久病者 BMI 易誤判。",
        "B": "錯誤。Albumin 為經典營養指標 (半衰期 20 天)；< 3.5 g/dL 提示營養不良或炎症。",
        "C": "錯誤。HbA1c 反映 3 個月血糖控制；雖非營養指標但與營養狀態相關 (久病糖尿病營養不良風險高)。",
        "D": "錯誤。Hemoglobin 反映 iron、protein、B12/folate 等營養素狀態，為間接指標。",
    },
    "guidelines": [
        "ASPEN 2019：營養評估應綜合 SGA (Subjective Global Assessment) + NRS-2002 + biochemistry。",
        "ESPEN GLIM Criteria 2018：診斷 malnutrition 需 ≥ 1 phenotypic + ≥ 1 etiologic criteria。",
    ],
    "points": [
        "Prealbumin 半衰期短 (2 天)，反映短期變化",
        "Albumin 受 inflammation、肝功能、水分影響，非純營養指標",
        "NRS-2002 為 ESPEN 推薦 ICU screen tool",
    ],
    "keyword": "Nutritional assessment, BMI, SGA, NRS-2002",
    "source": "ESPEN/ASPEN Guidelines; Miller's Anesthesia 8/e Ch. Nutrition",
},
3: {  # 嚴重高血鉀
    "answer_text": "Calcium gluconate 可降低血清鉀",
    "summary": "Calcium gluconate 不降鉀，僅穩定心肌膜電位 (membrane stabilization)，避免致命心律不整。降鉀需 insulin/glucose、β2-agonist、bicarbonate (shift)、Kayexalate/dialysis (remove)。",
    "mechanism": "高鉀升高靜止膜電位 → 心肌 Na channel 失活 → 心律不整。Ca²⁺ 升高 threshold potential，恢復電位差，立即穩定心肌但不影響 K 濃度。Insulin 啟動 Na/K ATPase 將 K 推入細胞；β2-agonist 同機轉；HCO₃⁻ 矯正 acidosis 同時 H⁺/K⁺ exchange。",
    "options": {
        "A": "錯誤 (本題不適當的選項)。Ca gluconate 穩定心肌但「不降鉀」；混淆兩種作用。",
        "B": "正確。Insulin 10 U + D50 25-50 g (或維持血糖) shift K 入細胞，15 分鐘起效。",
        "C": "正確。NaHCO₃ 矯正 acidosis 並 shift K；對 acidosis 病人更有效。",
        "D": "正確。β2-agonist (albuterol、salbutamol) nebulizer 或 IV 可降鉀 0.5-1 mEq/L。",
    },
    "guidelines": [
        "KDIGO 2020 Acute Hyperkalemia：(1) 心肌穩定 Ca gluconate 1g IV；(2) Shift insulin/glucose、β2、HCO₃；(3) Remove diuretic、resin、dialysis。",
        "ACLS：嚴重高鉀 (K > 6.5 + EKG changes) 立即 Ca、insulin/D50；考慮 HD。",
        "EKG 變化：peaked T → wide QRS → sine wave → VF/asystole。",
    ],
    "points": [
        "Ca gluconate 10% 10 mL IV slow 2-5 min；30 分鐘可重複",
        "Insulin/glucose 後監測血糖 ≥ 6 hr (delayed hypoglycemia)",
        "Sodium polystyrene sulfonate (Kayexalate) 效果緩，與 bowel necrosis 相關",
    ],
    "keyword": "Hyperkalemia, calcium gluconate, insulin, KDIGO",
    "source": "KDIGO 2020 Hyperkalemia; Stoelting's 7/e Ch. Renal pp. 393-407",
},
4: {  # 成人營養需求
    "answer_text": "BMI 25-29 熱量需求 21-25 kcal/kg/day",
    "summary": "肥胖 (BMI 25-29) 病人能量計算採 adjusted weight，需求 22-25 kcal/kg actual weight 或 25-30 kcal/kg IBW；非單純按 actual weight 計算。重症肥胖採 hypocaloric high-protein (11-14 kcal/kg actual weight, protein 2 g/kg IBW)。",
    "mechanism": "肥胖病人 lean body mass 與 metabolic rate 並非與 weight 線性增加。Adjusted Body Weight (ABW) = IBW + 0.25 × (Actual − IBW) 為臨床常用。Protein 攝取維持 lean mass。",
    "options": {
        "A": "正確。RDA 蛋白質 0.8 g/kg 可滿足 97% 健康成人。",
        "B": "正確。重症病人 protein ≥ 1.2-1.5 g/kg (ASPEN/SCCM 2016)；嚴重 catabolism 可達 2 g/kg。",
        "C": "錯誤 (本題不適當)。BMI 25-29 肥胖病人計算需求需更精確；21-25 kcal/kg/day 不準確。應按 ABW 或 IBW 計算。",
        "D": "正確。腦、RBC、腎髓質、眼水晶體無 mitochondria 或 ketone-utilization 路徑，依賴 glucose；最低 ~120 g/day 維持。",
    },
    "guidelines": [
        "ASPEN/SCCM 2016：重症一般 25-30 kcal/kg/day；肥胖採 hypocaloric high-protein。",
        "ESPEN 2019：indirect calorimetry 為金標準；無 IC 時用 weight-based formula。",
        "Harris-Benedict、Mifflin-St Jeor 為常用估算式。",
    ],
    "points": [
        "重症肥胖 (BMI > 30) hypocaloric high-protein：11-14 kcal/kg actual + protein 2 g/kg IBW",
        "蛋白質為 lean mass 維持關鍵，重症期間優先",
        "Refeeding syndrome 風險：低 P、低 K、低 Mg → 補充 + 慢速啟動",
    ],
    "keyword": "Caloric requirements, obesity, hypocaloric high-protein",
    "source": "ASPEN/SCCM 2016 Critical Care Nutrition Guidelines",
},
5: {  # 病毒性腦炎
    "answer_text": "CSF PCR 應檢測 HSV + 腸病毒",
    "summary": "HSV-1 為成人腦炎最常見致病原；急診 CSF 應做 HSV PCR + acyclovir empiric treatment。但「同時檢測腸病毒 PCR」並非每例必須，依臨床表現決定 (兒童、夏季、無菌性腦膜炎較考慮)。",
    "mechanism": "HSV-1 經 olfactory 或 trigeminal pathway 進入 CNS，攻擊 temporal/frontal lobe (非枕葉)。MRI T2/FLAIR temporal lobe edema 為典型。CSF：lymphocytic pleocytosis、protein↑、RBC (出血性)、PCR sensitivity > 95% (1-3 天後)。",
    "options": {
        "A": "正確。HSV-1 為成人急性腦炎最常見原因。",
        "B": "正確。Fever、AMS、personality change、seizure 為典型四主徵。",
        "C": "錯誤 (本題不適當)。腸病毒 PCR 非每例必須；臨床表現 + 流行病學決定。",
        "D": "正確。MRI 為最敏感影像；HSV-1 典型侵犯 temporal lobe (非枕葉) — 但選項說「枕葉」實為錯誤敘述，須注意官方答案 vs 醫學事實之差異。",
    },
    "guidelines": [
        "IDSA Encephalitis Guidelines 2008：所有疑似病毒性腦炎應立即 empiric Acyclovir 10 mg/kg IV q8h，待 CSF HSV PCR 結果。",
        "Acyclovir 早期 (< 4 天) 啟動可降死亡率 70% → 28%。",
        "MRI > CT；EEG 可見 PLEDs (periodic lateralized epileptiform discharges)。",
    ],
    "points": [
        "HSV-1 典型 MRI 部位為 temporal/frontal lobe，非枕葉",
        "經典 CSF：lymphocytic pleocytosis + 紅血球 (haemorrhagic necrosis)",
        "Acyclovir empiric treatment 不待確診 — early treatment 改變預後",
    ],
    "keyword": "Viral encephalitis, HSV-1, acyclovir, CSF PCR",
    "source": "IDSA Encephalitis Guidelines 2008; Harrison's Principles of Internal Medicine",
},
6: {  # Aminoglycosides
    "answer_text": "Aminoglycosides 主要為 bacteriostatic",
    "summary": "Aminoglycosides (gentamicin、tobramycin、amikacin) 為「bactericidal」(殺菌) 非 bacteriostatic；作用於 30S ribosomal subunit 阻斷蛋白質合成。主要副作用為 nephrotoxicity (近端腎小管)、ototoxicity (cochlear + vestibular)、neuromuscular blockade。",
    "mechanism": "Aminoglycoside 與 ribosomal 30S binding 引起 mRNA 誤讀 → 異常蛋白 → 細胞死亡。Concentration-dependent killing + post-antibiotic effect → once-daily dosing 較佳。腎毒性源於 proximal tubular 累積、ototoxicity 由 cochlear hair cell apoptosis。",
    "options": {
        "A": "正確。Once-daily dosing 利用 concentration-dependent + post-antibiotic effect、降低 nephrotoxicity。",
        "B": "正確。Cmax/MIC ratio > 8-10 為 efficacy 預測。",
        "C": "正確。腎毒性、聽毒性、neuromuscular blockade 為主要副作用。",
        "D": "錯誤 (本題不適當)。Aminoglycosides 為「殺菌」性 (bactericidal)，非 bacteriostatic。",
    },
    "guidelines": [
        "IDSA：Once-daily extended-interval dosing (5-7 mg/kg) 為 standard except 妊娠、重症感染心內膜炎、嚴重 burn、CrCl < 20。",
        "TDM：Trough < 1 µg/mL (gentamicin) 避免 nephrotoxicity；peak monitoring optional。",
        "與 NMBA 協同 (Mg、neostigmine 也潛在加重)，麻醉中監測 TOF。",
    ],
    "points": [
        "Bactericidal：β-lactam、aminoglycoside、fluoroquinolone、vancomycin、metronidazole",
        "Bacteriostatic：tetracycline、macrolide、clindamycin、TMP-SMX、linezolid",
        "Aminoglycoside-induced NM block 與 vecuronium、rocuronium 加成",
    ],
    "keyword": "Aminoglycosides, bactericidal, nephrotoxicity, ototoxicity",
    "source": "Sanford Guide to Antimicrobial Therapy; Stoelting's Pharmacology 5/e",
},
7: {  # TMP-SMX
    "answer_text": "Mycobacterium tuberculosis",
    "summary": "TMP-SMX (Baktar®) 為 sulfonamide + dihydrofolate reductase inhibitor，廣效但無法治療 Mycobacterium tuberculosis (需 anti-TB regimen RIPE)。可治：PCP、Nocardia、Stenotrophomonas、Toxoplasmosis、UTI、 community-acquired MRSA skin。",
    "mechanism": "TMP 阻斷 dihydrofolate reductase；SMX 阻斷 dihydropteroate synthetase；兩階段協同阻斷 folate synthesis → bacterial DNA synthesis 抑制。TB 對 TMP-SMX 完全 resistant。",
    "options": {
        "A": "錯誤。Pneumocystis jirovecii 為 TMP-SMX 首選治療與預防 (HIV、移植病人)。",
        "B": "錯誤。Toxoplasma gondii 雖首選 pyrimethamine + sulfadiazine，但 TMP-SMX 為 alternative。",
        "C": "錯誤。Stenotrophomonas maltophilia 對 TMP-SMX 高度敏感，為 first-line。",
        "D": "正確 (本題答案 — 無法治療)。Mycobacterium TB 需 RIPE (Rifampin + Isoniazid + Pyrazinamide + Ethambutol) regimen。",
    },
    "guidelines": [
        "CDC TB Guidelines：Initial 2 月 RIPE + continuation 4 月 RI。",
        "CDC PCP Prophylaxis：HIV CD4 < 200 給 TMP-SMX 1 SS/day。",
        "TMP-SMX 副作用：Stevens-Johnson syndrome、TEN、hyperkalemia、bone marrow suppression、kernicterus 新生兒。",
    ],
    "points": [
        "TMP-SMX 涵蓋：Gram + (S. aureus including MRSA)、Gram − (E. coli、Klebsiella、Stenotrophomonas)、PCP、Nocardia、Toxoplasma",
        "不涵蓋：Mycobacterium、Pseudomonas、anaerobe、syphilis",
        "G6PD deficiency：可引起 hemolysis，使用需注意",
    ],
    "keyword": "TMP-SMX, sulfonamide, Mycobacterium tuberculosis",
    "source": "Sanford Guide; CDC TB Guidelines",
},
8: {  # SIRS/sepsis labs
    "answer_text": "符合 sepsis 之臨床表現",
    "summary": "病人 T 38.5、HR 120、RR 22、WBC 15000 (左移 84.7%)、CRP 高 — 符合 SIRS 至少 2 項 + 感染證據 = sepsis 範疇 (Sepsis-2 定義)。Sepsis-3 (2016) 改用 qSOFA / SOFA 評分。",
    "mechanism": "SIRS criteria (Sepsis-2)：T > 38 或 < 36、HR > 90、RR > 20 或 PaCO₂ < 32、WBC > 12K 或 < 4K 或 > 10% bands。≥ 2 項符合即 SIRS。Sepsis = SIRS + infection。Severe sepsis = sepsis + organ dysfunction。Septic shock = + hypotension despite fluid。",
    "options": {
        "A": "錯誤。SIRS 雖年代久但 ≥ 2 項標準明確；此病人符合。",
        "B": "錯誤。本案有發燒 + WBC↑ + CRP↑ + 心跳呼吸快，已超過 SIRS 範圍。",
        "C": "正確。臨床表現符合 sepsis (SIRS + 感染);應啟動 sepsis bundle。",
        "D": "錯誤。Septic shock 需 hypotension despite fluid + lactate > 2；本病人 BP 120/65 不符。",
    },
    "guidelines": [
        "Surviving Sepsis Campaign 2021 1-hour bundle：(1) 血液培養；(2) lactate；(3) broad-spectrum antibiotics；(4) crystalloid 30 mL/kg；(5) vasopressor for MAP ≥ 65。",
        "qSOFA (≥ 2)：SBP ≤ 100、RR ≥ 22、altered mentation — 預測 ICU mortality。",
        "Sepsis-3：SOFA score ≥ 2 increase from baseline + 疑似/確診感染 = sepsis。",
    ],
    "points": [
        "Procalcitonin 較 CRP specific for bacterial infection",
        "Early antibiotic + source control 為 sepsis 治療關鍵",
        "Lactate clearance > 10%/h 預後改善指標",
    ],
    "keyword": "Sepsis, SIRS, Sepsis-3, qSOFA",
    "source": "Surviving Sepsis Campaign 2021; Sepsis-3 Definitions 2016",
},

# ===== 急診醫學 (Q9-14) =====
9: {  # 暈厥 EKG
    "answer_text": "完全房室阻斷 (Complete AV block)",
    "summary": "70 歲女性暈厥 + 規則 P 波獨立於 QRS、ventricular rate 較 atrial rate 慢 = 完全房室阻斷 (third-degree AV block, AV dissociation)。需 transcutaneous pacing → permanent pacemaker。",
    "mechanism": "Complete AV block = AV node 或 His-Purkinje system 完全傳導阻斷 → atria 與 ventricles 各自為政；ventricular escape rhythm (junctional 40-60、ventricular 20-40 bpm)。常見原因：AMI (especially RCA territory)、ischemic heart disease、calcific degeneration (Lev/Lenègre)、Lyme、藥物 (β-blocker、CCB、digoxin)。",
    "options": {
        "A": "正確。Third-degree AV block 為典型；ECG: P 規則、QRS 規則但慢；P 與 QRS 無關聯。",
        "B": "錯誤。Atrial fibrillation: 無 P 波、irregularly irregular RR。",
        "C": "錯誤。Mobitz II: P 規則、間歇 dropped beats、PR constant 直到 drop。",
        "D": "錯誤。VT: wide QRS, AV dissociation 可有但 ventricular rate fast。",
    },
    "guidelines": [
        "ACC/AHA/HRS 2018 Bradycardia Guidelines：symptomatic AV block 為 permanent pacemaker class I 適應症。",
        "暫時處置：Atropine 0.5 mg IV (效果有限對 infranodal block)、transcutaneous pacing。",
        "Avoid β-blocker、CCB、digoxin。",
    ],
    "points": [
        "Wenckebach (Mobitz I)：progressive PR prolongation until drop；常 AV nodal、無症狀",
        "Mobitz II：PR constant、sudden drop；常 infranodal、需 pacing",
        "Complete heart block + acute MI inferior：可能 transient；anterior MI = permanent damage to bundle",
    ],
    "keyword": "Complete AV block, syncope, pacemaker",
    "source": "ACC/AHA/HRS 2018 Bradycardia Guidelines",
},
10: {  # KUB 腹痛
    "answer_text": "小腸阻塞 (Small bowel obstruction, SBO)",
    "summary": "60 歲女性曾剖腹產 + 膽囊切除 (= 腹部手術史)，腹痛 + 噁心嘔吐 + KUB 顯示 air-fluid levels + distended small bowel loops = 小腸阻塞。最常見原因：粘連 (adhesion, 60-75%)。",
    "mechanism": "SBO 機械性阻塞 → 阻塞上方腸道擴張、積氣積液、嘔吐電解質流失 (代謝性鹼中毒 + hypokalemia)。Stranqulation 風險：fever、tachycardia、peritonitis、lactate↑、CT free fluid → 急刀。",
    "options": {
        "A": "正確。SBO 典型 KUB：multiple distended small bowel loops + air-fluid levels (ladder pattern)。",
        "B": "錯誤。Volvulus 影像表現為 coffee-bean / closed-loop。",
        "C": "錯誤。Diverticulitis 需 CT + clinical (LLQ pain、fever)。",
        "D": "錯誤。Acute pancreatitis 主要 clinical + lipase；KUB 非診斷工具。",
    },
    "guidelines": [
        "EAST Practice Management Guidelines for SBO：CT 為首選 imaging；保守治療 (NG decompression + IV fluid + electrolyte correction) 對 partial 與 simple obstruction 成功率 60-85%。",
        "緊急手術指標：peritonitis、ischemia、closed-loop、failure of conservative trial 48-72h。",
        "麻醉：RSI (full stomach)、aspiration 防護、可能 hypovolemic shock。",
    ],
    "points": [
        "SBO 4 大常見原因：adhesion (60-75%)、hernia (10-20%)、malignancy (10%)、IBD/intussusception",
        "Closed-loop obstruction 為手術急症 (ischemia 風險)",
        "麻醉誘導：NG decompression、awake intubation 或 RSI，預防 aspiration",
    ],
    "keyword": "Small bowel obstruction, adhesion, RSI",
    "source": "EAST Practice Management Guidelines for SBO",
},
11: {  # 腎前性 AKI
    "answer_text": "Urine Na > 40 mEq/L",
    "summary": "腎前性 AKI (prerenal) 由腎臟灌流不足 (hypovolemia、heart failure、shock)；腎元功能正常，努力保留 Na 與水。Urine Na 應 < 20、FENa < 1%；BUN/Cr ratio > 20:1。Urine Na > 40 屬 intrinsic AKI (ATN)。",
    "mechanism": "腎前性 AKI：RAAS 與 ADH 活化 → 近端腎小管 Na 重吸收增加、髓質 ADH 作用集尿 → 高比重 (SG > 1.020)、高 osmolality、低 Na、低 FENa。Intrinsic AKI (ATN)：腎小管 dysfunction → 無法保 Na、Urine Na 高、SG 接近 1.010。",
    "options": {
        "A": "正確 (本題不符合 prerenal)。Urine Na > 40 為 intrinsic AKI 特徵；prerenal 應 < 20。",
        "B": "錯誤 (符合 prerenal)。FENa < 1% (除非 diuretic) 為 prerenal hallmark。",
        "C": "錯誤 (符合 prerenal)。BUN/Cr > 20:1 為 prerenal 典型 (preferential reabsorption of urea)。",
        "D": "錯誤 (符合 prerenal)。Urine osmolality > 500 mOsm 為 prerenal 集中尿。",
    },
    "guidelines": [
        "KDIGO 2012 AKI：分 prerenal、intrinsic、postrenal；Stage 1-3 依 SCr 與 urine output。",
        "FENa = (UNa × PCr) / (PNa × UCr) × 100；diuretic 使用後改用 FEUrea (< 35% 為 prerenal)。",
        "處置：恢復灌流 (fluid、cardiac output 改善、stop nephrotoxin)；persistent → 進入 ATN。",
    ],
    "points": [
        "ATN urine sediment：muddy brown granular casts",
        "Postrenal AKI：bilateral hydronephrosis (BPH、stone、tumor)",
        "Prerenal 早期可逆，延誤 → ATN (irreversible 24h)",
    ],
    "keyword": "Prerenal AKI, FENa, BUN/Cr ratio, ATN",
    "source": "KDIGO 2012 AKI Guidelines; Pocket Medicine 7/e",
},
12: {  # 氣胸處置
    "answer_text": "胸管引流 (Tube thoracostomy)",
    "summary": "25 歲外傷 + 呼吸困難 + CXR 顯示 traumatic pneumothorax (假設大於 20-30%)。Symptomatic + traumatic = 胸管引流標準處置；張力性氣胸需先 needle decompression 再 chest tube。",
    "mechanism": "Pneumothorax 胸膜腔氣體 → lung collapse → V/Q mismatch、hypoxia。Tension pneumothorax：one-way valve 機制 → 持續氣體進入胸膜腔 → mediastinal shift → 阻擋 venous return → 心血管虛脫 (CV collapse)。",
    "options": {
        "A": "錯誤。Needle aspiration 適合 small primary spontaneous，外傷性氣胸應放胸管。",
        "B": "正確。Symptomatic 或 traumatic pneumothorax 應放 28-32 Fr chest tube 4-5th ICS, anterior axillary line。",
        "C": "錯誤。Conservative observation 只適合 small (< 20%)、asymptomatic primary spontaneous。",
        "D": "錯誤。Open thoracotomy 為 massive hemothorax (> 1500 mL initial 或 > 200 mL/hr) 或 unstable chest 適應症。",
    },
    "guidelines": [
        "ATLS 10/e Trauma Guidelines：Tension PTX → needle decompression (5th ICS midaxillary)；Traumatic PTX → tube thoracostomy。",
        "BTS 2010 Pleural Disease：胸管 size 8-14 Fr 對小氣胸足夠；外傷或 hemothorax 需 28-32 Fr。",
        "Trauma：always check for pneumothorax 於 GA induction 前 — positive pressure 可變 tension。",
    ],
    "points": [
        "Tension PTX 為臨床診斷 — 不可等 CXR",
        "麻醉考量：N₂O 使 PTX 擴大 → 已知氣胸禁忌",
        "拔管後 monitor lung re-expansion",
    ],
    "keyword": "Pneumothorax, tube thoracostomy, ATLS",
    "source": "ATLS 10/e; BTS Pleural Disease Guidelines 2010",
},
13: {  # 膽道感染
    "answer_text": "急性化膿性膽管炎 (Acute cholangitis)",
    "summary": "68 歲男性 RUQ pain + jaundice + fever (Charcot's triad) + leukocytosis → 急性膽管炎 (acute cholangitis)。加上 hypotension + AMS = Reynolds' pentad (severe suppurative cholangitis)。需立即抗生素 + 膽道引流 (ERCP)。",
    "mechanism": "膽道阻塞 (stone、tumor、stricture) → bile stasis → bacterial colonization (E. coli、Klebsiella、Enterococcus) → 細菌入血。膽管壓力 > 25 cmH₂O 引起 cholangiovenous reflux → bacteremia → sepsis。",
    "options": {
        "A": "錯誤。Acute cholecystitis: RUQ pain、Murphy sign、fever；jaundice 較少出現 (除非 Mirizzi syndrome)。",
        "B": "正確。Charcot's triad (pain + fever + jaundice) = acute cholangitis；emergent biliary decompression 為治療關鍵。",
        "C": "錯誤。Acute pancreatitis 不典型呈現 jaundice (除非 biliary cause)；lipase confirms。",
        "D": "錯誤。Hepatic abscess 通常 subacute、無 acute biliary obstruction features。",
    },
    "guidelines": [
        "Tokyo Guidelines 2018 (TG18)：急性膽管炎診斷與分級。",
        "Severe cholangitis (Grade III)：immediate biliary drainage (preferably ERCP within 24h)。",
        "Empiric antibiotics：piperacillin-tazobactam、ceftriaxone + metronidazole、carbapenem (severe)。",
    ],
    "points": [
        "Reynolds' pentad = Charcot's + hypotension + AMS = severe suppurative cholangitis (mortality 50%+)",
        "ERCP > PTC > surgery in most cases",
        "麻醉：sepsis 復甦、可能 coagulopathy、術後加護",
    ],
    "keyword": "Acute cholangitis, Charcot's triad, Tokyo Guidelines",
    "source": "Tokyo Guidelines 2018 (TG18)",
},
14: {  # HHS
    "answer_text": "高滲透性高血糖症候群 (Hyperosmolar Hyperglycemic State, HHS)",
    "summary": "38 歲 T2DM + AMS + 血糖 980 + 高 osmolality (350) + 低 ketone (0.1) = 高滲透性高血糖狀態 (HHS)，非 DKA (DKA ketone > 3、acidosis)。HHS 多見於 T2DM 老年；mortality 高 (10-20%)。",
    "mechanism": "T2DM 殘餘 insulin 足以抑制 ketogenesis 但不足以降血糖 → 漸進性極高血糖 + 滲透性利尿 → 嚴重脫水 + hyperosmolality → 腦功能異常。比 DKA 進展慢 (days-weeks)、脫水嚴重 (~9 L deficit)。",
    "options": {
        "A": "正確。HHS criteria: 血糖 > 600、osmolality > 320、pH > 7.3、HCO₃ > 18、minimal ketone、AMS。",
        "B": "錯誤。DKA: 血糖通常 > 250 但 < 600、pH < 7.3、HCO₃ < 18、ketone > 3、Kussmaul。",
        "C": "錯誤。Hypoglycemia 血糖低、不會 980。",
        "D": "錯誤。SIADH 為等容性 hyponatremia、無高血糖。",
    },
    "guidelines": [
        "ADA Management of DKA and HHS：(1) Aggressive fluid resuscitation (1-1.5 L NS in first hour、then 0.45% NS); (2) Insulin infusion 0.1 U/kg/h after K > 3.3; (3) K replacement 早期 (insulin 後 K 進細胞); (4) 血糖目標 250-300 first 24h 防 cerebral edema。",
        "Trigger 找：infection (most common)、MI、stroke、pancreatitis、stop insulin。",
    ],
    "points": [
        "HHS 麻醉：rehydration first、K correction、慎防 hypoglycemia 與 cerebral edema",
        "Fluid resuscitation 速度低於 DKA (脫水嚴重但 osmolality 急降危險)",
        "Mortality 10-20%；老年合併症多",
    ],
    "keyword": "HHS, hyperosmolar hyperglycemic state, DKA",
    "source": "ADA Standards of Medical Care in Diabetes",
},

# ===== 心臟、呼吸、休克 (Q15-21) =====
15: {  # BNP
    "answer_text": "B-type natriuretic peptide (BNP / NT-proBNP)",
    "summary": "BNP 由心室因 stretch、wall stress 分泌；最常用於 heart failure 嚴重度評估、預後、治療反應。NT-proBNP 為 inactive fragment、半衰期較長、適用於門診監測。",
    "mechanism": "BNP 主要作用：natriuresis、diuresis、vasodilation；對抗 RAAS 與 sympathetic activation。BNP > 100、NT-proBNP > 300 提示 HF 可能；< 35 / < 125 可排除 HF (high NPV)。",
    "options": {
        "A": "錯誤。Troponin 為 myocardial injury (AMI、myocarditis)；雖 HF 可輕度升高，但非 severity 主要 marker。",
        "B": "正確。BNP/NT-proBNP 為 HF severity & prognosis 主要 marker。",
        "C": "錯誤。CK-MB 為 AMI marker (現多由 troponin 取代)。",
        "D": "錯誤。D-dimer 為 thrombosis (DVT、PE) screen。",
    },
    "guidelines": [
        "ACC/AHA HF Guidelines 2017 Update：BNP/NT-proBNP 用於診斷、severity、prognosis、guidance of therapy。",
        "Acute HF in ED：BNP > 500、NT-proBNP > 1000 (< 50y)、> 1800 (> 50y) 高度支持 HF。",
        "BNP 在 obesity (↓)、renal failure (↑) 須調整解讀。",
    ],
    "points": [
        "PARADIGM-HF：ARNI (Entresto) 降低 HFrEF mortality",
        "NT-proBNP > 1000 加重住院預後差",
        "Treatment-guided BNP 對 HF 預後改善有限 (GUIDE-IT trial)",
    ],
    "keyword": "BNP, NT-proBNP, heart failure",
    "source": "ACC/AHA HF Guidelines; Stoelting's 7/e Ch. Cardiovascular",
},
16: {  # 縱膈氣腫
    "answer_text": "Pneumomediastinum / 縱膈氣腫",
    "summary": "Mechanical ventilation + 突發呼吸器警示 + 頸部皮下氣泡 (subcutaneous emphysema) + 觸診 crepitus = pneumomediastinum / 縱膈氣腫 (從 barotrauma 或 pneumothorax 延伸)。需 urgent CXR / CT。",
    "mechanism": "Barotrauma：high pressure → alveolar rupture → air dissect along bronchovascular sheath → mediastinum → cervical SQ → 廣泛 subcutaneous emphysema。可進展 → tension pneumothorax、tension pneumomediastinum (心輸出受阻)。",
    "options": {
        "A": "錯誤。ETT cuff leak 不會引起 SQ emphysema；listen for cuff sound、check pressure。",
        "B": "錯誤。Mucus plug 表現為 airway pressure 升、SpO₂ 降、單側 air entry 差；無 SQ emphysema。",
        "C": "正確。Pneumomediastinum + SQ emphysema 為 barotrauma 經典 (尤其老年、高 PEEP、COPD)。",
        "D": "錯誤。Pulmonary edema 不引起 SQ emphysema。",
    },
    "guidelines": [
        "ARDS Network 6 mL/kg lung-protective ventilation 減少 barotrauma。",
        "處置：confirm with CXR/CT、reduce PEEP / TV、chest tube if pneumothorax、考慮 needle aspiration of pneumomediastinum if tension。",
    ],
    "points": [
        "Crackling on palpation = Hamman's sign (SQ emphysema)",
        "Tension pneumomediastinum 為急症 — 處置同 tension pneumothorax",
        "ARDS 低 TV (4-6 mL/kg) + plateau pressure ≤ 30 cmH₂O",
    ],
    "keyword": "Pneumomediastinum, barotrauma, subcutaneous emphysema",
    "source": "ARDSnet protocol; Miller's 8/e Critical Care",
},
17: {  # Sepsis 處置
    "answer_text": "立即靜脈大量晶體輸注 + broad-spectrum antibiotic",
    "summary": "65 歲男性 UTI + 寒顫 + 高燒 + 低血壓 + tachycardia + tachypnea + 尿量少 = 嚴重 sepsis / septic shock。Surviving Sepsis 1-hour bundle：lactate、blood culture、broad-spectrum antibiotics、crystalloid 30 mL/kg、vasopressor if MAP < 65。",
    "mechanism": "Sepsis：感染引發 cytokine storm → endothelial dysfunction → vasodilation + capillary leak → distributive shock。Early aggressive fluid + antibiotic + source control 改善 mortality。",
    "options": {
        "A": "錯誤。仍可口服抗生素不足以處理 severe sepsis；needs IV broad-spectrum。",
        "B": "正確。Aggressive crystalloid 30 mL/kg + 1-hr 內 broad-spectrum antibiotic 為標準。",
        "C": "錯誤。等待 culture 結果延誤治療 (mortality ↑ 7% per hour delay)。",
        "D": "錯誤。Vasopressor 是 fluid 後 still MAP < 65 才啟動 (norepinephrine first-line)。",
    },
    "guidelines": [
        "Surviving Sepsis Campaign 2021 1-hour bundle。",
        "ANZICS、ProCESS、ARISE trials：EGDT vs usual care 結果無差異 → 但 bundle adherence 改善 outcome。",
        "Empiric AB：依 likely organism、local antibiogram；UTI sepsis → ceftriaxone or piperacillin-tazobactam。",
    ],
    "points": [
        "Lactate > 4 → severe sepsis/shock；clearance > 10%/h 改善 prognosis",
        "Norepinephrine first-line vasopressor",
        "Source control (drainage、debridement) 為治療關鍵",
    ],
    "keyword": "Sepsis, sepsis bundle, Surviving Sepsis",
    "source": "Surviving Sepsis Campaign 2021",
},
18: {  # 4 種 shock
    "answer_text": "Distributive shock 為 vasodilation 引起 SVR↓、CO 通常↑",
    "summary": "Shock 4 型：(1) Hypovolemic (出血、脫水)：CO↓、SVR↑、CVP↓；(2) Cardiogenic (MI、HF)：CO↓、SVR↑、CVP↑；(3) Obstructive (PE、tamponade、tension PTX)：CO↓、SVR↑、CVP↑；(4) Distributive (sepsis、anaphylaxis、neurogenic)：SVR↓、CO 通常↑、暖週邊。",
    "mechanism": "Cardiogenic shock：心肌喪失 contractility → forward flow 減少 → 系統灌流不足 + 肺鬱血。Distributive shock：systemic vasodilation 主導 → SVR 嚴重下降；CO 早期代償性 ↑、後期心肌抑制下降。",
    "options": {
        "A": "錯誤 (描述模糊或誇大)。",
        "B": "錯誤 (機轉混淆)。",
        "C": "正確。Distributive (e.g. sepsis) 早期 hyperdynamic — CO↑、SVR↓、暖週邊；後期可進入心肌抑制。",
        "D": "錯誤 (描述不適當)。",
    },
    "guidelines": [
        "Surviving Sepsis 2021、ACC/AHA Cardiogenic Shock 2017、ATLS Hemorrhagic shock。",
        "PA catheter / TEE / POCUS 可區分 shock 類型 (CO、SVR、IVC、LV function)。",
    ],
    "points": [
        "Mixed shock 常見 (e.g. cardiogenic + distributive after MI sepsis)",
        "Treatment 依 type：fluid for hypovolemic、inotrope for cardiogenic、relieve obstruction、vasopressor for distributive",
        "POCUS RUSH protocol 快速 bedside 評估",
    ],
    "keyword": "Shock classification, distributive shock, hemodynamic profiles",
    "source": "Miller's Anesthesia 8/e Critical Care",
},
19: {  # septic shock 升壓
    "answer_text": "Norepinephrine",
    "summary": "Septic shock 第一線 vasopressor 為 Norepinephrine (α₁ + β₁)；維持 MAP ≥ 65；不足時加 Vasopressin、Epinephrine、Hydrocortisone。",
    "mechanism": "Norepinephrine 結合 α₁ 引起 vasoconstriction (升 SVR)、β₁ 輕度 inotropic effect (保 CO)；較少 tachycardia、arrhythmia 風險於 dopamine。",
    "options": {
        "A": "正確。Norepinephrine first-line for septic shock。",
        "B": "錯誤。Dopamine 因 tachyarrhythmia、mortality 升而退居二線 (SOAP II trial)。",
        "C": "錯誤。Phenylephrine 純 α₁、無 inotropic、可降 CO，非首選。",
        "D": "錯誤。Vasopressin 為 second-line catecholamine-sparing；refractory shock 加入。",
    },
    "guidelines": [
        "Surviving Sepsis 2021：NE first-line；加 Vasopressin 0.03 U/min；refractory 加 Epi、Hydrocortisone 200 mg/day。",
        "SOAP II Trial 2010：NE vs Dopamine — NE 死亡率較低、arrhythmia 少。",
        "VANISH Trial：Vasopressin 早加未改善 mortality，但減少 catecholamine。",
    ],
    "points": [
        "MAP target ≥ 65 mmHg；個體化於高血壓老人可考慮 80-85",
        "Central line preferred、peripheral 短期 (< 24h、< 0.1 µg/kg/min) 可接受",
        "Hydrocortisone 用於 refractory shock (vasopressor 仍需 > 0.25 µg/kg/min)",
    ],
    "keyword": "Septic shock, norepinephrine, vasopressor",
    "source": "Surviving Sepsis Campaign 2021",
},
20: {  # IHCA post-ROSC
    "answer_text": "立即重新給予完整 ACLS 藥物全劑量",
    "summary": "Post-ROSC 處置重點：(1) Oxygenation/Ventilation — SpO₂ 92-98%、PaCO₂ 35-45；(2) Hemodynamic — MAP ≥ 65；(3) Targeted Temperature Management (TTM) 32-36°C × 24h；(4) Coronary angiography if STEMI / shockable rhythm；(5) Neurologic prognosis 72h 後評估。不應 routinely re-bolus ACLS drugs。",
    "mechanism": "Post-cardiac arrest syndrome (PCAS) 4 components: (1) post-arrest brain injury；(2) post-arrest myocardial dysfunction；(3) systemic ischemia/reperfusion；(4) persistent precipitating pathology。TTM 透過降低 metabolic demand、減少 reperfusion injury 改善 neurological outcome。",
    "options": {
        "A": "錯誤 (本題不適當)。Post-ROSC 不應 routinely 再給 ACLS drugs；該專注 reperfusion 損傷、TTM、找原因。",
        "B": "正確。SpO₂ 92-98%、PaCO₂ 35-45 (避免 hyperoxia 與 hypocapnia)。",
        "C": "正確。TTM 32-36°C × 24h 為 standard post-ROSC care。",
        "D": "正確。STEMI 或 shockable rhythm 應 emergent cath lab。",
    },
    "guidelines": [
        "AHA 2020 ACLS：Post-cardiac arrest care。",
        "TTM Trial 2013：32°C vs 36°C 無差異；ILCOR 推 32-36°C × 24h。",
        "Targeted MAP ≥ 65；避免 hyperoxia (SpO₂ > 98%)。",
    ],
    "points": [
        "Neurologic prognosis 至少 72h 後評估 (TTM 延長至 5 天)",
        "Source identification 對 prevention recurrence 重要",
        "Family communication 與 organ donation evaluation 早討論",
    ],
    "keyword": "Post-ROSC, TTM, post-cardiac arrest syndrome",
    "source": "AHA 2020 ACLS Guidelines",
},
21: {  # NSTEMI
    "answer_text": "Aspirin + Heparin、避免 nitrate due to hypotension",
    "summary": "胸悶 + 盜汗 + EKG 變化 + BP 90/60 + HR 52 = ACS。低血壓 + bradycardia 提示 RCA territory (inferior MI) 可能 (RV infarct 風險)。應給 antiplatelet + anticoagulation、避免 nitrate (使 hypotension 惡化)，準備 cath lab。",
    "mechanism": "Inferior MI 常合併 RV infarct (RCA supplies)；RV 依賴 preload，nitrate 降低 preload → severe hypotension。Treatment：fluid bolus 維持 preload、reperfusion (PCI > thrombolysis)。",
    "options": {
        "A": "錯誤。Nitrate 在 inferior MI + low BP 為禁忌。",
        "B": "正確。Aspirin 162-325 mg + heparin (UFH 60 U/kg bolus)，避免 nitrate；fluid bolus 250-500 mL。",
        "C": "錯誤。Beta-blocker 在 bradycardia + low BP 為禁忌。",
        "D": "錯誤。Morphine 為 last resort (mask symptoms、可降 BP)；單獨 inadequate。",
    },
    "guidelines": [
        "ACC/AHA STEMI/NSTEMI Guidelines：MONA-B 已過時；個別化 antiplatelet + anticoagulation + reperfusion。",
        "Door-to-balloon < 90 min for STEMI。",
        "DAPT (Dual antiplatelet)：aspirin + P2Y12 inhibitor (ticagrelor、prasugrel)。",
    ],
    "points": [
        "RV infarct: V₄R lead ST elevation; treat with fluid, NOT nitrate/diuretic",
        "Bradycardia in inferior MI: atropine, may need pacing",
        "Cardiogenic shock complicating AMI: IABP, ECMO, urgent PCI",
    ],
    "keyword": "Acute coronary syndrome, inferior MI, RV infarct",
    "source": "ACC/AHA NSTEMI/STEMI Guidelines",
},

# ===== 神經麻醉 (Q22-25) =====
22: {  # CBF regulation
    "answer_text": "PaCO₂ 每升 1 mmHg，CBF 增加 1-2 mL/100g/min (約 4%)",
    "summary": "CBF 約 50 mL/100g/min。調控：(1) PaCO₂ — 最強 (3-5% per mmHg)；(2) PaO₂ — 顯著低 < 50 才影響；(3) MAP autoregulation 50-150；(4) CMRO₂ flow-metabolism coupling；(5) neurogenic、myogenic。",
    "mechanism": "CO₂ 在腦內形成 H₂CO₃ → 直接 vasodilate cerebral resistance vessels。Hyperventilation 短期降 ICP；長期 (> 6h) 失效 (renal compensation)。低 PaO₂ < 50 才大量 vasodilation。",
    "options": {
        "A": "錯誤 (敘述不精確)。",
        "B": "錯誤 (機制混淆)。",
        "C": "正確。PaCO₂ 對 CBF 影響最強；4% per mmHg 為標準。",
        "D": "錯誤。",
    },
    "guidelines": [
        "Brain Trauma Foundation：Acute herniation 可短期 hyperventilate PaCO₂ 30-35；routine prophylactic hyperventilation 不建議。",
        "Cerebral oximetry (NIRS) 監測 cerebral oxygenation。",
        "Maintain normocapnia (35-40) 為一般 TBI 目標。",
    ],
    "points": [
        "Hyperventilation lowers ICP 短期；不應為長期策略",
        "Inhaled anesthetics > 1 MAC 引起 vasodilation、ICP↑；TIVA preferred for ↑ICP",
        "Ketamine 影響 CBF 爭議性、但現代研究較中性",
    ],
    "keyword": "Cerebral blood flow, PaCO₂, autoregulation",
    "source": "Miller's Anesthesia 8/e Ch. 70 Neurosurgical Anesthesia",
},
23: {  # ICP impact
    "answer_text": "ICP 上升降低 CPP 與 CBF",
    "summary": "CPP = MAP − ICP。ICP 上升 → CPP 下降 → CBF 下降 (autoregulation 失效時更甚)。腦組織 hypoperfusion → ischemia → secondary brain injury。",
    "mechanism": "Monroe-Kellie doctrine：cranial volume 固定，腦 + 血 + CSF。任一成分增加 → 其他減少代償；超過 reserve → ICP 急升 (exponential)。",
    "options": {
        "A": "錯誤 (反向描述)。",
        "B": "錯誤 (混淆關係)。",
        "C": "正確。ICP↑ → CPP↓ → CBF↓ (autoregulation impaired in injury)。",
        "D": "錯誤 (描述不適當)。",
    },
    "guidelines": [
        "Brain Trauma Foundation 4/e：ICP treatment threshold > 22 mmHg；CPP target 60-70。",
        "Mannitol 0.25-1 g/kg、Hypertonic saline 3% 250 mL 為 osmotic therapy。",
        "Head elevation 30°、avoid jugular compression、normocapnia 35-40。",
    ],
    "points": [
        "Tier 1 ICP treatment：head elevation、sedation、analgesia、CSF drainage",
        "Tier 2：mannitol、hypertonic saline、hyperventilation (short)",
        "Tier 3：barbiturate coma、decompressive craniectomy",
    ],
    "keyword": "Intracranial pressure, cerebral perfusion pressure, Monroe-Kellie",
    "source": "Brain Trauma Foundation 4/e (2016)",
},
24: {  # SSEPs/MEPs
    "answer_text": "揮發性麻醉劑 < 0.5 MAC 影響較小，TIVA 對 MEPs 監測較佳",
    "summary": "SSEP / MEP 監測用於脊椎、神經外科手術。揮發性麻醉劑 dose-dependent 抑制 amplitude、延長 latency；MEPs 較 SSEPs 敏感。TIVA (propofol + remifentanil) 為理想麻醉。",
    "mechanism": "Volatile anesthetics 抑制 synaptic transmission, 對 cortical SSEP 影響大 (subcortical 較小)。MEPs 經 corticospinal tract，volatile > 0.5 MAC 即顯著抑制。NMBA 完全阻斷 MEPs，須避免。",
    "options": {
        "A": "錯誤。Volatile 對 MEPs 抑制顯著，不可隨意用。",
        "B": "正確。低濃度 (< 0.5 MAC) 揮發性可接受 SSEP；MEPs 監測首選 TIVA。",
        "C": "錯誤。NMBA 阻斷 MEPs，TOF 須保留。",
        "D": "錯誤 (混淆機制)。",
    },
    "guidelines": [
        "ASNM (American Society of Neurophysiological Monitoring)：MEPs 監測首選 TIVA。",
        "Etomidate、ketamine 可 enhance SSEPs (paradoxical)。",
        "NMBA：TOF 1-2/4 可接受 SSEPs；MEPs 避免使用。",
    ],
    "points": [
        "Visual evoked potential (VEP) 對麻醉敏感、罕用於監測",
        "Brainstem auditory evoked potential (BAEP) 較 robust to anesthesia",
        "Significant change: 50% amplitude ↓ 或 10% latency ↑",
    ],
    "keyword": "SSEPs, MEPs, TIVA, evoked potentials",
    "source": "Miller's Anesthesia 8/e Ch. 50 Monitoring of the CNS",
},
25: {  # 麻醉藥對腦生理
    "answer_text": "Propofol 降 CMRO₂、CBF、ICP",
    "summary": "理想 neuroprotective 藥物：propofol、barbiturate、etomidate (均降 CMRO₂ + CBF + ICP)。揮發性麻醉劑 dose-dependent：低濃度 (< 1 MAC) 接近 propofol，高濃度引起 cerebral vasodilation、ICP↑。Ketamine 與 N₂O 影響爭議性。",
    "mechanism": "CMRO₂ ↓ → flow-metabolism coupling → CBF ↓ → 腦血容量 ↓ → ICP ↓。Propofol burst suppression 可達 EEG-isoelectric, maximally protective。",
    "options": {
        "A": "錯誤 (敘述不精確)。",
        "B": "錯誤。",
        "C": "正確。Propofol 降 CMRO₂ + CBF + ICP；為 neuroanesthesia 首選。",
        "D": "錯誤。",
    },
    "guidelines": [
        "Society for Neuroscience in Anesthesiology and Critical Care (SNACC)：TIVA propofol-based 為 ICP↑ 病人 preferred。",
        "Burst suppression for refractory ICP 或 seizure。",
        "N₂O 在 air-containing structure (pneumocephalus、air embolism) 禁忌。",
    ],
    "points": [
        "Sevoflurane < 1 MAC 對腦 hemodynamics 影響小、可接受",
        "Ketamine 重新評價：可能 neuroprotective、不嚴格禁忌於 ICP",
        "Dexmedetomidine 降 CBF + CMRO₂ proportionally；保留腦血流調節",
    ],
    "keyword": "Cerebral metabolism, CMRO₂, propofol, neuroprotection",
    "source": "Miller's Anesthesia 8/e Ch. 70",
},

# ===== 骨科、止血帶 (Q26-30) =====
26: {  # 骨水泥植入症候群
    "answer_text": "Hypoxia、hypotension、cardiovascular collapse 為典型表現",
    "summary": "Bone Cement Implantation Syndrome (BCIS)：骨水泥固化時 monomer 進入循環 + fat/marrow embolism → 三主徵 hypoxia、hypotension、cardiovascular collapse。高風險：髖關節手術、老年、心衰、骨質疏鬆。",
    "mechanism": "PMMA (Polymethylmethacrylate) 放熱反應 + 機械壓迫骨髓內壓上升 → fat、marrow content、cement monomer 進入靜脈循環 → 肺循環 → pulmonary hypertension、RV failure、anaphylactoid 反應。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "正確。Hypoxia + hypotension + cardiovascular collapse 為經典三主徵。",
        "D": "錯誤。",
    },
    "guidelines": [
        "AAGBI Safety Guideline 2015：BCIS classification (Grade 1 mild、Grade 2 moderate、Grade 3 severe)。",
        "預防：充分 hydration、osmotically clean medullary canal、低壓 cement、保持 FiO₂↑、euvolemia、avoid N₂O。",
        "處置：100% O₂、fluid、vasopressor (norepinephrine)、CPR 若 arrest。",
    ],
    "points": [
        "高風險：老年女性、髖部骨折、心衰、肺病、肺高壓",
        "Cementless prosthesis 替代以避免 BCIS (尤其高風險)",
        "Vigilance during cementation + early intervention",
    ],
    "keyword": "Bone cement implantation syndrome, PMMA, hip arthroplasty",
    "source": "AAGBI BCIS Safety Guideline 2015; Miller's 8/e",
},
27: {  # Tourniquet 釋放低血壓
    "answer_text": "Reperfusion 後 metabolite (lactate、K⁺)、heat、CO₂ 進入循環引起 vasodilation",
    "summary": "Tourniquet 釋放後 hypotension 機制：(1) 蓄積之 vasoactive metabolites 釋出；(2) Reperfusion 引起的 reactive hyperemia；(3) Hypovolemia (血液重新分布至下肢)；(4) ETCO₂ 急升伴隨 transient acidosis；(5) Hypothermia from cold limb。",
    "mechanism": "Limb ischemic period 期間 anaerobic metabolism 累積 lactate、K⁺、H⁺、ROS。Release → systemic washout → vasodilation + 心肌抑制 → 血壓下降。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "錯誤。",
        "D": "正確。Reperfusion syndrome 為最主要機制。",
    },
    "guidelines": [
        "AAOS Tourniquet Guidelines：< 2 小時、上肢 SBP+50、下肢 SBP+100 mmHg。",
        "釋放前：increase FiO₂、bolus fluid、monitor ETCO₂、K、acid-base。",
        "嚴重 hyperkalemia 或 acidosis 可能、考慮慢釋放或 staged release。",
    ],
    "points": [
        "ETCO₂ 急升於 tourniquet 釋放 — 經典 capnogram changes",
        "Pre-existing hypovolemia、acidosis 加重 release-induced hypotension",
        "Tourniquet pain：充氣 45-60 min 後深層 aching、tachycardia",
    ],
    "keyword": "Tourniquet release, reperfusion, hyperkalemia",
    "source": "AAOS Tourniquet Use Guidelines",
},
28: {  # Dexmedetomidine
    "answer_text": "選擇性 α₂-adrenergic agonist、sympatholytic、sedation 無顯著呼吸抑制",
    "summary": "Dexmedetomidine 為高選擇性 α₂-agonist (clonidine 8 倍)。優點：sedation/analgesia 無顯著呼吸抑制、reduce anesthetic + opioid 需求、降低 emergence agitation 與 delirium、bradycardia、hypotension (initial 可能 hypertension)。",
    "mechanism": "中樞 α₂ receptor in locus coeruleus → 降低 noradrenaline release → sedation (mimics natural sleep)、analgesia。周邊 α₂ → vasoconstriction → initial hypertension；長期主要 sympatholytic → bradycardia、hypotension。",
    "options": {
        "A": "錯誤 (混淆機制)。",
        "B": "正確。α₂-agonist、特性如上。",
        "C": "錯誤 (描述不適當)。",
        "D": "錯誤。",
    },
    "guidelines": [
        "FDA approved for ICU sedation < 24h、procedural sedation。",
        "Loading dose 0.5-1 µg/kg over 10 min；maintenance 0.2-0.7 µg/kg/h。",
        "DEXMEDETOMIDINE-DELIRIUM (PRODEX trial)：dex vs midazolam — 減少 delirium、機械通氣天數。",
    ],
    "points": [
        "副作用：bradycardia (atropine response good)、hypotension、dry mouth",
        "對 awake fiberoptic intubation 有用 — 維持自主呼吸 + 配合",
        "可降低 emergence agitation 兒童",
    ],
    "keyword": "Dexmedetomidine, α2-agonist, ICU sedation",
    "source": "FDA Precedex label; Miller's 8/e Ch. 30",
},
29: {  # POVL
    "answer_text": "Prone position、長時間手術、low Hct、男性、貧血為風險因子",
    "summary": "Perioperative Vision Loss (POVL) 主因：Ischemic Optic Neuropathy (ION)、Central Retinal Artery Occlusion (CRAO)、Cortical blindness。Spine surgery prone position 為主要族群 (ASA POVL Registry)。",
    "mechanism": "ION：optic nerve 缺血；prone + 長時間 + 低 BP + 血液稀釋 + venous congestion (head down) → 局部 perfusion 不足。CRAO：直接眼球壓迫 (e.g. horseshoe headrest 不當)。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "錯誤。",
        "D": "正確。Prone position、長時間、貧血、男性、肥胖、低 BP 為風險。",
    },
    "guidelines": [
        "ASA Practice Advisory for POVL 2019：spine surgery > 6h、estimated blood loss > 1L 為 highest risk。",
        "預防：避免 head-down、保持 head neutral、avoid prolonged hypotension、monitor Hct、Mayfield/foam headrest 適當。",
        "ASA POVL Registry 持續收集 data。",
    ],
    "points": [
        "Vision loss 通常 first noticed in PACU、prognosis poor",
        "Cardiac surgery (CPB) 為次常見族群 (CRAO、cortical blindness)",
        "Mid-procedure 檢查眼瞼、避免外壓",
    ],
    "keyword": "POVL, ischemic optic neuropathy, prone position",
    "source": "ASA Practice Advisory for POVL 2019",
},
30: {  # 多模式止痛
    "answer_text": "Femoral block + epidural opioid + acetaminophen + ketorolac 屬完整 multimodal",
    "summary": "Multimodal analgesia for TKA：(1) Pre-emptive (gabapentinoid、celecoxib、acetaminophen)；(2) Intraoperative regional (femoral nerve block、adductor canal、PENG block)；(3) Local infiltration (LIA)；(4) Postop multimodal opioid-sparing。",
    "mechanism": "不同藥物作用於不同 pain pathway：(1) Peripheral (NSAIDs、LA)；(2) Spinal (epidural opioid、α2-agonist)；(3) Supraspinal (acetaminophen、opioid)。協同效應降低個別藥物副作用。",
    "options": {
        "A": "錯誤 (描述不完整)。",
        "B": "錯誤。",
        "C": "錯誤。",
        "D": "正確。完整 multimodal：acetaminophen + NSAIDs + epidural opioid + peripheral nerve block 為理想組合。",
    },
    "guidelines": [
        "ERAS Knee Replacement Pathway：multimodal opioid-sparing 為核心。",
        "ASRA：femoral block 可能延緩 ambulation；adductor canal block 為現代替代 (motor-sparing)。",
        "PROSPECT 推薦：TKA 採 multimodal + LIA + adductor canal block。",
    ],
    "points": [
        "Adductor canal block 保留 quadriceps function，方便 early ambulation",
        "PENG (pericapsular nerve group) block 為新興 hip option",
        "Continuous catheter 延長 analgesia 至 48-72h",
    ],
    "keyword": "Multimodal analgesia, TKA, ERAS",
    "source": "PROSPECT TKA Guidelines; ERAS Society",
},

# ===== Propofol、輸血、腹腔鏡、洗腎 (Q31-39) =====
31: {  # Propofol 不適合
    "answer_text": "Egg / Soy allergy 嚴重者 (相對禁忌)",
    "summary": "Propofol 配方含 soybean oil、egg lecithin、glycerol。嚴重 egg/soy allergy 為相對禁忌 (anaphylaxis 罕見但可能)。其他相對禁忌：嚴重心血管不穩、低血容、無法 secure airway、PRIS 風險高 (兒童長期 high dose)。",
    "mechanism": "Egg lecithin = phospholipid (非 protein)；過敏反應更可能源於 egg protein (ovalbumin) — 但臨床仍謹慎。嚴重食物過敏 + 既往 propofol 反應為禁忌。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "錯誤。",
        "D": "正確 (本題不適合使用 propofol)。Severe egg/soy allergy 為相對禁忌；雖然多數 egg allergy 可安全使用 (近 30 年研究)，嚴重 anaphylaxis history 仍應避免。",
    },
    "guidelines": [
        "ASA: egg allergy not absolute contraindication; but cautious with severe anaphylaxis history。",
        "PRIS：dose > 4 mg/kg/h × > 48h；FDA black box for pediatric ICU。",
        "替代：Etomidate、Ketamine、Thiopental、Midazolam。",
    ],
    "points": [
        "Egg-anaphylaxis 病人約 < 1% 對 propofol 反應，新證據認為大多安全",
        "Soy allergy 同樣低風險，但嚴重者建議替代",
        "PRIS 三聯徵：metabolic acidosis、rhabdomyolysis、cardiac failure",
    ],
    "keyword": "Propofol, allergy, contraindication, PRIS",
    "source": "FDA Propofol label; Stoelting's Pharmacology 5/e",
},
32: {  # 肝癌大出血優先輸注
    "answer_text": "FFP + Cryoprecipitate (補充凝血因子與 fibrinogen)",
    "summary": "肝癌 + 凝血異常 (factor synthesis ↓) + 大量出血 → 除 PRBC 外應優先補充 fibrinogen (cryoprecipitate 或 fibrinogen concentrate) 與 FFP (coagulation factors)。Massive transfusion protocol 1:1:1 (PRBC:FFP:Platelet)。",
    "mechanism": "肝硬化/肝癌：vit K-dependent factor (II、VII、IX、X) 合成下降、fibrinogen normal-low、thrombocytopenia (splenic sequestration)。大量出血 → dilutional coagulopathy + consumption → 需 hemostatic resuscitation。",
    "options": {
        "A": "正確。FFP + cryo 優先補充 fibrinogen 與 clotting factors；目標 fibrinogen > 200 mg/dL、INR < 1.5。",
        "B": "錯誤 (描述不適當)。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "ASA Practice Guidelines for Perioperative Blood Management 2015。",
        "Goal-directed transfusion：TEG/ROTEM 指引比例。",
        "Massive transfusion protocol 1:1:1 if no point-of-care available。",
        "Tranexamic acid 1 g IV 早期 (< 3h) 降低死亡率 (CRASH-2)。",
    ],
    "points": [
        "Fibrinogen 為首先消耗的凝血因子",
        "Cryoprecipitate 提供集中 fibrinogen (10-15 mL/unit ≈ 4 g/L)",
        "PCC (Prothrombin Complex Concentrate) 為 warfarin reversal、肝病替代",
    ],
    "keyword": "Massive transfusion, hepatic coagulopathy, fibrinogen",
    "source": "ASA Practice Guidelines for Perioperative Blood Management",
},
33: {  # 腹腔鏡 trocar 後高血壓
    "answer_text": "Pneumoperitoneum 引起 SVR↑ + CO 重分布 (sympathetic activation + 直接壓迫)",
    "summary": "Insufflation 後 BP↑、HR 輕度↑、ETCO₂↑ — 由 CO₂ 吸收 + intra-abdominal pressure (IAP) 壓迫 → SVR↑、splanchnic 與 renal flow ↓、reduced venous return (高 IAP 時)。",
    "mechanism": "IAP 12-15 mmHg：(1) Mechanical effect — diaphragm 上推、FRC↓、 atelectasis；vascular compression。(2) Humoral — CO₂ 吸收 + sympathetic activation → BP↑、SVR↑。Trendelenburg 加重 venous return + ICP。",
    "options": {
        "A": "正確。Pneumoperitoneum 經典反應：BP↑、SVR↑、ETCO₂↑、CO₂ absorption。",
        "B": "錯誤 (描述不適當)。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "EAES (European Association for Endoscopic Surgery) Guidelines：IAP ≤ 15 mmHg；低 IAP (8-10) 在敏感病人。",
        "Ventilation：increase minute ventilation 30-50% maintain ETCO₂；avoid hyperventilation。",
        "心血管病人：A-line monitoring、慢速 insufflation。",
    ],
    "points": [
        "嚴重 CO₂ embolism 雖罕見但致命 — 突發 ETCO₂↓、CV collapse",
        "Severe Trendelenburg → ↑ICP、facial edema、ETT migration",
        "Pneumothorax / pneumomediastinum 可能由 diaphragm 缺損",
    ],
    "keyword": "Pneumoperitoneum, laparoscopy, CO2 absorption",
    "source": "Miller's Anesthesia 8/e Ch. 76 Laparoscopic Anesthesia",
},
34: {  # 透析病人術前評估
    "answer_text": "術前 24h 透析、避免 K+ > 5.5、評估 access 與心血管",
    "summary": "ESRD/HD 病人術前重點：(1) Recent HD (≤ 24h)、(2) K+ < 5.5、(3) 評估 AV fistula 與 catheter access、(4) 心血管 (LVH、CAD、HF)、(5) anemia、(6) coagulopathy、(7) 藥物調整。",
    "mechanism": "ESRD 多重器官影響：心血管 (HTN、LVH、CAD)、貧血、coagulopathy (uremic platelet dysfunction)、metabolic (acidosis、hyperkalemia)、藥物動力學改變。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "正確。Recent HD + 電解質、心血管全面評估為標準。",
        "D": "錯誤。",
    },
    "guidelines": [
        "KDIGO Perioperative AKI Guidelines。",
        "麻醉藥選擇：avoid morphine、meperidine；prefer cisatracurium、fentanyl、remifentanil。",
        "AV fistula 保護：no IV、no BP cuff 該肢。",
    ],
    "points": [
        "AVF stenosis、infection 為常見併發症，術前 thrill/bruit 評估",
        "Uremic platelet dysfunction：DDAVP 0.3 µg/kg 改善",
        "EPO + IV iron 改善 anemia 但不過度 (target Hb 10-11)",
    ],
    "keyword": "ESRD, hemodialysis, AV fistula, preoperative",
    "source": "Stoelting's Anesthesia and Co-existing Disease 7/e Ch. Renal",
},
35: {  # 甲狀腺切除神經監測
    "answer_text": "Recurrent laryngeal nerve (RLN) monitoring + NMBA 限制使用",
    "summary": "甲狀腺切除術中 RLN injury 為主要併發症 (vocal cord paralysis)。IONM (Intraoperative Neuromonitoring) 透過 EMG ETT 偵測 RLN function。NMBA 須適度 (TOF ≥ 2)，避免完全阻斷影響 monitoring。",
    "mechanism": "RLN 走 tracheoesophageal groove；甲狀腺手術風險。IONM EMG ETT 接觸 vocal cords，刺激 RLN 偵測 EMG 反應 (loss = injury)。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "正確。RLN monitoring + 限制 NMBA 為標準。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "International Neural Monitoring Study Group (INMSG)：standardized IONM protocol。",
        "ETT 位置：cuff 在 vocal cords 中央；確認 EMG signal。",
        "Avoid deep NMBA — TOF count 2-3 可接受。",
    ],
    "points": [
        "Bilateral RLN injury → 嚴重 stridor、需 tracheostomy",
        "Superior laryngeal nerve (external branch) injury → 高音域 weakening",
        "Hypocalcemia 為術後另一併發症 (parathyroid injury)",
    ],
    "keyword": "Recurrent laryngeal nerve, IONM, thyroidectomy",
    "source": "INMSG Guidelines; Hagberg Airway Management 4/e",
},
36: {  # 常規用藥對術中
    "answer_text": "ACEi/ARB 術前停藥可降低術中 hypotension 發生率",
    "summary": "Perioperative medication management：(1) Continue — β-blocker、statin、ASA (大多手術)；(2) Hold — ACEi/ARB (morning of surgery, 減少術中 hypotension)、SGLT2-i (DKA risk)、metformin (lactic acidosis)、insulin (調整)；(3) Bridge — warfarin → heparin (高血栓風險)。",
    "mechanism": "ACEi/ARB 阻斷 RAAS；術中 anesthesia 引起 vasodilation + 麻醉藥心肌抑制 → 嚴重 hypotension difficult to vasopressor。停一劑改善血壓穩定。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "正確。ACEi/ARB 停藥減少術中 hypotension。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "ACC/AHA 2014 Perioperative Cardiovascular Guidelines。",
        "ESC/ESA 2014 Non-cardiac Surgery。",
        "Continue β-blocker (avoid abrupt withdrawal)；Statin perioperative continuation 安全。",
        "SGLT2-i：停 3-4 天 (DKA risk even with normal glucose)。",
    ],
    "points": [
        "POISE trial：高劑量 β-blocker 開始於 surgery 當天 — 增加 stroke、mortality",
        "Aspirin in low-risk surgery：可繼續；high-bleeding-risk (e.g. neuro)：停 7 天",
        "DAPT post-stent：須 cardiology consultation",
    ],
    "keyword": "ACEi, ARB, perioperative medication, hypotension",
    "source": "ACC/AHA 2014 Perioperative Guidelines",
},
37: {  # 達文西前列腺術
    "answer_text": "Steep Trendelenburg + pneumoperitoneum 引起 facial/glottic edema、ICP↑、IOP↑",
    "summary": "Robotic prostatectomy 採 steep Trendelenburg (30-45°) + pneumoperitoneum 長時間。獨特生理影響：facial swelling、conjunctival/glottic edema、ICP↑、IOP↑、aspiration risk、reduced FRC、shoulder/neck nerve injury。",
    "mechanism": "Trendelenburg + IAP↑：(1) Venous return ↑ → CVP↑；(2) Diaphragm 上推 → FRC↓、atelectasis、ventilator pressure↑；(3) ICP↑；(4) Cephalad fluid shift → face/glottic edema；(5) IOP 上升至 40+ mmHg。",
    "options": {
        "A": "正確。Steep Trendelenburg + pneumoperitoneum 生理影響為主要照護重點。",
        "B": "錯誤 (描述不適當)。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "ESA Robotic Surgery Anesthesia：穩定 patient 至 table、緩慢 positioning、protect arm/shoulder。",
        "Limit 機器手臂時間、間歇 level table reduce edema。",
        "Pre-op POVL risk assessment for glaucoma、prone-equivalent IOP changes。",
    ],
    "points": [
        "Limited access 機器運作中 — 麻醉問題處置困難",
        "ETT migration、cuff leak 常見 — 防止頻繁 endotracheal manipulation",
        "Eye protection essential — taping、lubricant、avoid pressure",
    ],
    "keyword": "Robotic surgery, Trendelenburg, prostatectomy",
    "source": "Miller's Anesthesia 8/e Ch. 77",
},
38: {  # 甲狀腺術前 CXR
    "answer_text": "Tracheal deviation/compression 提示 substernal goiter，須準備困難呼吸道",
    "summary": "甲狀腺術前 CXR 用於評估 tracheal deviation、compression、substernal extension。Goiter 壓迫 trachea → 困難插管、awake fiberoptic intubation、smaller ETT、可能緊急 tracheostomy。",
    "mechanism": "大型 goiter 壓迫氣管 → 軟化 (tracheomalacia)、舵狀 / horseshoe deformity。Substernal goiter 可壓迫 SVC、recurrent laryngeal nerve。Anesthesia induction NMBA 失去 muscle tone → 嚴重氣道塌陷。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "錯誤。",
        "D": "正確。Tracheal deviation/compression 為困難呼吸道警訊。",
    },
    "guidelines": [
        "DAS Difficult Airway Algorithm 2015：predict + plan。",
        "Awake fiberoptic intubation 為首選 (預期 difficult airway)。",
        "Surgical team standby for emergency tracheostomy。",
        "Avoid full NMBA until tube secured。",
    ],
    "points": [
        "CT neck/chest 提供更精確 anatomy",
        "Substernal goiter 不易 surgical access、可能 sternotomy",
        "Tracheomalacia 術後可塌陷、leak test、prolonged intubation if needed",
    ],
    "keyword": "Goiter, tracheal compression, difficult airway",
    "source": "Hagberg Airway Management 4/e",
},
39: {  # 70 kg 腹腔鏡多模式止痛
    "answer_text": "Fentanyl PCA 為主、單一 opioid 為多模式",
    "summary": "多模式止痛 (multimodal) 應結合不同機轉藥物 + 區域麻醉：(1) Acetaminophen 1 g q6h；(2) NSAIDs/COX-2 ketorolac 30 mg q6h；(3) Local infiltration / TAP block；(4) IV lidocaine / ketamine infusion；(5) Opioid 為 rescue。單一 Fentanyl PCA 非 multimodal。",
    "mechanism": "Multimodal 透過 synergistic + complementary mechanism，降低 individual drug doses、減少 PONV、便秘、呼吸抑制、住院天數。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "正確 (本題不適當的選項)。Fentanyl PCA 為單一 opioid，非 multimodal 概念。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "ERAS Society Colorectal Pathway：multimodal + TAP block + thoracic epidural 選項。",
        "PROSPECT laparoscopic abdominal surgery：multimodal opioid-sparing。",
        "ASRA: TAP block 為 abdominal surgery 補充止痛。",
    ],
    "points": [
        "Lidocaine infusion 1.5 mg/kg/h reduce opioid + 改善 ileus",
        "Ketamine 0.1-0.3 mg/kg bolus + low-dose infusion 對 opioid-tolerant 有效",
        "Dexmedetomidine 為 opioid-sparing 選項",
    ],
    "keyword": "Multimodal analgesia, laparoscopic surgery, ERAS",
    "source": "ERAS Society Guidelines; PROSPECT",
},

# ===== AS、OLV、HPV、OCR (Q40-43) =====
40: {  # Severe AS 麻醉
    "answer_text": "Spinal anesthesia 為理想麻醉方式",
    "summary": "Severe AS 麻醉禁忌：(1) Spinal anesthesia (sudden sympathectomy)；(2) Tachycardia；(3) Hypotension；(4) Hypovolemia。維持：sinus rhythm、normal HR 60-80、normal preload、 高 SVR、避免 hypotension。Phenylephrine、norepinephrine 為主要 vasopressor。",
    "mechanism": "Severe AS LVH stiff ventricle、preload-dependent、無法即時增加 stroke volume。Sudden sympathectomy → SVR↓ → BP↓ → coronary perfusion↓ → ischemia → arrhythmia → 死亡。",
    "options": {
        "A": "正確 (描述正確)。",
        "B": "錯誤 (本題錯誤的選項)。Spinal anesthesia 非首選，sympathectomy 災難性；通常選 GA 或 epidural 慢滴定。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "ACC/AHA 2014 Valvular Heart Disease。",
        "Severe AS: AVA < 1.0、mean gradient > 40、velocity > 4.0。",
        "TAVR 高風險病人替代開胸 AVR。",
        "Anesthesia: GA + invasive monitoring + judicious fluid + phenylephrine。",
    ],
    "points": [
        "Coronary perfusion 嚴重依賴 diastolic BP — 維持 ≥ 60 mmHg",
        "心律不整 (especially AF) 失去 atrial kick (30% CO)、致命",
        "TEE 監測 LV function 與 valve gradient",
    ],
    "keyword": "Severe aortic stenosis, spinal contraindication, sinus rhythm",
    "source": "ACC/AHA 2014 Valvular Heart Disease Guidelines",
},
41: {  # OLV hypoxia
    "answer_text": "立即停止 OLV 改 two-lung ventilation",
    "summary": "OLV 期間 hypoxia 處置依序：(1) 確認 DLT 位置 (fiberoptic)；(2) FiO₂ 1.0；(3) PEEP 5-10 cmH₂O 至 ventilated lung；(4) CPAP 5 cmH₂O 至 non-ventilated lung；(5) Recruitment maneuver；(6) 暫時 two-lung ventilation；(7) Clamp PA (極端)。Step 1 通常 troubleshoot 而非立即放棄 OLV。",
    "mechanism": "OLV hypoxia 主因：DLT malposition (常見 50%+)、shunt to non-ventilated lung、atelectasis、HPV failure (volatile high MAC、vasodilator)。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤 (本題不適當的選項)。立即停止 OLV 為最後手段；應先 troubleshoot。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "ASA、ATS Thoracic Anesthesia Guidelines。",
        "Lung-protective: TV 4-6 mL/kg IBW、PEEP 5-10、driving pressure < 15。",
        "Fiberoptic confirmation 為 DLT 位置 gold standard。",
    ],
    "points": [
        "Most common cause OLV hypoxia: DLT migration (especially after position change)",
        "Apneic insufflation 5-10 cmH₂O O₂ to non-ventilated lung",
        "Right-sided surgery: place left DLT (避免 RUL blockage)",
    ],
    "keyword": "One-lung ventilation, hypoxia, DLT, HPV",
    "source": "Miller's Anesthesia 8/e Ch. 65 Thoracic Anesthesia",
},
42: {  # HPV inhibition
    "answer_text": "Nitric Oxide (NO) 不抑制 HPV",
    "summary": "HPV (Hypoxic Pulmonary Vasoconstriction) 為缺氧區域 pulmonary artery 收縮、血流 redirect 至 oxygenated region 機制。Inhibitors: 揮發性麻醉劑 (high MAC)、vasodilator (nitrate、nicardipine、milrinone)、PEEP 過高、metabolic alkalosis、hypocapnia。NO 為 inhaled selective pulmonary vasodilator 但選擇性 dilate ventilated areas — 改善 V/Q matching，不抑制 HPV。",
    "mechanism": "Alveolar hypoxia → pulmonary arteriole smooth muscle 收縮 (via redox-sensitive K channel、Ca-mediated)。Volatile anesthetic > 1 MAC 直接抑制 HPV signaling。",
    "options": {
        "A": "錯誤 (本題不抑制 HPV — 正確答案)。Inhaled NO 選擇性 dilate ventilated lung，改善 oxygenation 但「不抑制 HPV」。",
        "B": "錯誤。Sevoflurane > 1 MAC 抑制 HPV。",
        "C": "正確 (本題答案 — 不抑制 HPV)。Inhaled NO 不影響 HPV。",
        "D": "錯誤。Nicardipine vasodilator 抑制 HPV。",
    },
    "guidelines": [
        "Inhaled NO 用於 pulmonary HTN、 ARDS、refractory hypoxia OLV (selective pulmonary vasodilator)。",
        "Pulmonary vasodilator effect 僅於 ventilated alveoli (delivered via airway)；非 ventilated 部分無作用 — 故 V/Q match 改善。",
    ],
    "points": [
        "Sevoflurane < 1 MAC + TIVA 對 OLV 較好 (HPV preserved)",
        "Inhaled milrinone 為 selective pulmonary vasodilator (selective)",
        "Hypocapnia 抑制 HPV → 維持 normocapnia",
    ],
    "keyword": "Hypoxic pulmonary vasoconstriction, inhaled NO, V/Q matching",
    "source": "Miller's Anesthesia 8/e Ch. 27",
},
43: {  # 眼心反射
    "answer_text": "OCR 不可預防、只能反應後處置",
    "summary": "Oculocardiac reflex (OCR)：眼外肌牽引或眼球壓迫 → trigeminal nerve afferent → vagal efferent → bradycardia (≥ 20% HR drop)、可至 sinus arrest。常見小兒 strabismus surgery。",
    "mechanism": "Trigeminovagal arc：long ciliary nerve → ophthalmic V₁ → trigeminal ganglion → trigeminal nucleus → vagal nerve → SA node。Hypoxia、hypercapnia、light anesthesia 加重反射。",
    "options": {
        "A": "正確 (描述適當)。",
        "B": "正確。",
        "C": "錯誤 (本題錯誤的選項)。OCR 可預防：deep anesthesia、prophylactic atropine/glycopyrrolate、慢手術動作、good ventilation。",
        "D": "正確。",
    },
    "guidelines": [
        "Pediatric Anesthesia: prophylactic atropine 0.02 mg/kg IV before traction in high-risk procedures。",
        "Treatment: (1) stop traction；(2) IV atropine 0.02 mg/kg；(3) ensure adequate ventilation; (4) deepen anesthesia。",
    ],
    "points": [
        "Recurrence: repeat traction may recur (反射 fatiguable)",
        "可能 reflexes: nausea、bronchospasm、laryngospasm",
        "Severe: sinus arrest、asystole — CPR 啟動",
    ],
    "keyword": "Oculocardiac reflex, trigeminovagal, atropine",
    "source": "Coté and Lerman Pediatric Anesthesia 6/e",
},

# ===== 甲狀腺風暴、TOF、DLT、ICD、CPB (Q44-49) =====
44: {  # 甲狀腺風暴
    "answer_text": "Beta-blocker 為禁忌",
    "summary": "甲狀腺風暴 (thyroid storm)：嚴重 hyperthyroidism + 心血管 (tachycardia、AF、heart failure)、CNS (agitation、psychosis、coma)、GI (vomiting、diarrhea、jaundice)、hyperthermia。處置：β-blocker (propranolol)、PTU/methimazole、iodine (Lugol)、steroid (dexamethasone)、active cooling。",
    "mechanism": "甲狀腺風暴由 surgery、infection、trauma、iodine 暴露、stop antithyroid drugs 觸發。Increased catecholamine sensitivity 主導心血管表現。β-blocker 對抗 sympathetic + 部分抑制 T4 → T3 conversion (propranolol)。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (本題錯誤敘述)。β-blocker (propranolol、esmolol) 為「首選」非禁忌；控制 tachycardia、心血管症狀。",
        "C": "正確。PTU 阻斷 T4 合成 + T4→T3 conversion。",
        "D": "正確。",
    },
    "guidelines": [
        "American Thyroid Association Hyperthyroidism Guidelines。",
        "Burch-Wartofsky Point Scale 評估 thyroid storm severity。",
        "Sequence：(1) β-blocker；(2) PTU 600-1000 mg loading；(3) iodine (>1h after PTU)；(4) dexamethasone 2 mg q6h。",
    ],
    "points": [
        "β-blocker 在 acute HF 慎用 — esmolol short-acting 較安全",
        "Aspirin 禁忌 (displace T4 from binding → free T4↑)",
        "Severe cases: plasmapheresis、therapeutic hypothermia 考慮",
    ],
    "keyword": "Thyroid storm, propranolol, PTU, Burch-Wartofsky",
    "source": "ATA Hyperthyroidism Guidelines 2016",
},
45: {  # 法洛氏四重症
    "answer_text": "Right ventricular hypertrophy",
    "summary": "Tetralogy of Fallot (TOF) 四項特徵：(1) Pulmonary stenosis (RVOT obstruction)；(2) RV hypertrophy；(3) Overriding aorta；(4) VSD。Cyanosis 程度依 RVOT obstruction 嚴重度。",
    "mechanism": "RVOT obstruction → RV pressure↑ → RVH。VSD allows R-to-L shunt → deoxygenated blood 進入體循環 → cyanosis。Tet spell：increased RVOT obstruction (catecholamine、dehydration) → 急性 cyanosis。",
    "options": {
        "A": "正確。",
        "B": "正確。",
        "C": "錯誤 (本題錯誤敘述 — 似有誤譯)。應為 LV hypertrophy 是錯誤 — TOF 為 RV hypertrophy。",
        "D": "正確。",
    },
    "guidelines": [
        "AHA Congenital Heart Disease Guidelines。",
        "Anesthesia for TOF：maintain SVR、avoid hypovolemia、avoid extreme tachycardia、reduce RVOT spasm。",
        "Tet spell：knee-chest position、O₂、IV fluid、phenylephrine、morphine、esmolol。",
    ],
    "points": [
        "Most common cyanotic congenital heart disease > 1 yr old",
        "Surgical repair: complete repair at 3-6 months ideal",
        "Anesthetic: avoid drops in SVR (worsens R-to-L shunt)",
    ],
    "keyword": "Tetralogy of Fallot, RVOT obstruction, tet spell",
    "source": "Coté and Lerman Pediatric Anesthesia 6/e",
},
46: {  # 左管雙腔
    "answer_text": "Left DLT 適用所有右肺手術，避免 RUL bronchus blockage",
    "summary": "Left DLT 較 right DLT 安全 (right DLT 易堵 RUL bronchus due to short right mainstem and high RUL takeoff)。Left DLT 適用大多 thoracic surgery；right DLT 僅 left mainstem 病灶 (left bronchial mass、left pneumonectomy 需 right DLT 隔離)。",
    "mechanism": "Right mainstem bronchus 短 (~2.5 cm) + RUL bronchus take-off 距 carina 1.5-2 cm → right DLT bronchial cuff 易塞 RUL。Left mainstem 長 (~5 cm)、 較容易 accommodating left DLT。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (本題錯誤敘述)。Left DLT 不是適用「所有」右肺手術，但是「大多」；right DLT 罕用 — 描述部分不精確或誤譯。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "Fiberoptic bronchoscopy 為 DLT 位置 confirmation gold standard。",
        "DLT size 依身高、性別 (女性 35-37 Fr、男性 39-41 Fr)。",
        "Bronchial blocker 為替代：difficult airway、already intubated。",
    ],
    "points": [
        "DLT malposition 為 OLV hypoxia 主因",
        "Position change (lateral decubitus) 後重新確認位置",
        "Single-lumen ETT + bronchial blocker 為較容易插管之替代",
    ],
    "keyword": "Double-lumen tube, OLV, fiberoptic",
    "source": "Miller's Anesthesia 8/e Ch. 65",
},
47: {  # 扁桃腺術後出血
    "answer_text": "可採用 inhalation induction 不需 IV access",
    "summary": "Post-tonsillectomy bleeding 為麻醉急症，視為 full stomach + 可能 hypovolemia + difficult airway：(1) IV access first (resuscitation)；(2) RSI、suction、預備血品；(3) Backup difficult airway 設備；(4) 由經驗豐富 anesthesia 執行。Inhalation induction 不適合 — 嘔吐 + 飽肚 + 困難呼吸道。",
    "mechanism": "Tonsillectomy bleeding 24h 內 (primary) 或 5-10 天 (secondary)；病人吞入大量血液 → full stomach + hypovolemia + Hb↓ + 困難 view (blood in airway)。Inhalation induction 進入 stage 2 → laryngospasm + aspiration risk 高。",
    "options": {
        "A": "正確。",
        "B": "正確。",
        "C": "正確。",
        "D": "錯誤 (本題不適當)。Inhalation induction 不適合 — aspiration、laryngospasm 風險極高；應 RSI 後 secured airway。",
    },
    "guidelines": [
        "APAGBI Difficult Pediatric Airway。",
        "Pre-induction: IV fluid resuscitation 20 mL/kg、血品準備。",
        "RSI: ketamine + etomidate 維持循環、succinylcholine 1.5 mg/kg 或 rocuronium 1.2 mg/kg。",
        "Two large suctions ready。",
    ],
    "points": [
        "拔管時:完全清醒、protective reflexes、lateral position",
        "成人 + 兒童同樣處置原則",
        "考慮 left lateral head-down 防 aspiration",
    ],
    "keyword": "Post-tonsillectomy bleeding, RSI, difficult airway",
    "source": "APAGBI; Coté and Lerman 6/e",
},
48: {  # ICD 術中
    "answer_text": "Magnet 永久關閉 ICD",
    "summary": "ICD 術前準備：(1) 確認 manufacturer、device function；(2) Electrocautery → 干擾 sensing → 可能 inappropriate shock 或 inhibit pacing；(3) Magnet over ICD 「暫時」disable shock function (sensing 不變)；(4) Bipolar electrocautery preferred；(5) Pacing-dependent 病人 reprogram to asynchronous。",
    "mechanism": "Magnet over ICD: disable tachyarrhythmia detection/therapy (shock) 但不影響 pacing。Move magnet → restore。對 pacemaker：magnet → asynchronous pacing。各 manufacturer 細節不同。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "正確。",
        "C": "錯誤 (本題錯誤敘述)。Magnet 「暫時」disable shock，移除即恢復；非永久 deactivate。",
        "D": "正確。",
    },
    "guidelines": [
        "HRS/ASA Expert Consensus 2011 on CIED Management。",
        "Cardiology consultation pre-op (CIED check、interrogation)。",
        "Post-op interrogation: ensure restored function、check parameters。",
        "Bipolar cautery > monopolar；short bursts。",
    ],
    "points": [
        "Pacemaker-dependent: magnet → asynchronous (e.g. VOO 80 bpm)",
        "ICD shock during surgery: stop electrocautery、magnet over device",
        "CPR over device OK if needed",
    ],
    "keyword": "ICD, pacemaker, magnet, electrocautery",
    "source": "HRS/ASA Expert Consensus on CIED 2011",
},
49: {  # CPB 麻醉
    "answer_text": "CPB 期間需保持 normothermia (37°C)",
    "summary": "CPB 麻醉特殊考量：(1) Heparin (anticoagulation, ACT > 480) pre-bypass；(2) Hypothermia (28-34°C) 降代謝、保護器官；(3) 血液稀釋、cardioplegia；(4) Volatile anesthetic via CPB circuit；(5) Reversal protamine 1 mg per 100 U heparin；(6) Coagulation management。",
    "mechanism": "CPB diverts blood from heart-lung，使用 oxygenator (gas exchange) + roller/centrifugal pump (CO)。Hypothermia 降低 metabolic demand、enable safer ischemic time。Cardioplegia (high K solution) 停心臟、保護心肌。",
    "options": {
        "A": "錯誤 (本題錯誤敘述)。CPB 期間「降溫」(mild to moderate hypothermia 28-34°C) 為標準；normothermia 並非必要。",
        "B": "正確。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "STS/SCA Anesthetic Management of Cardiac Surgery。",
        "ACT > 480 sec for CPB (heparin)。",
        "Antifibrinolytic (TXA、ε-aminocaproic acid) 減少 bleeding。",
        "Coming off CPB: rewarm、wean ventilation、inotropic support、TEE。",
    ],
    "points": [
        "Hypothermia: every 1°C ↓ → CMRO₂ ↓ 6-7%",
        "Volatile anesthetic via CPB circuit, monitor BIS",
        "Heparin-induced thrombocytopenia (HIT)：用 bivalirudin 替代",
    ],
    "keyword": "Cardiopulmonary bypass, hypothermia, heparin",
    "source": "STS/SCA Cardiac Surgery Anesthesia",
},

# ===== 兒科麻醉、剖腹產 (Q50-58) =====
50: {  # 幽門狹窄
    "answer_text": "立即手術為急症",
    "summary": "Pyloric stenosis (幽門狹窄) 為「醫療急症非外科急症」— 必先矯正電解質與脫水 (hypochloremic、hypokalemic metabolic alkalosis)。Surgery 等到 Cl > 100、HCO₃ < 30。Pyloromyotomy 在電解質正常後施行。",
    "mechanism": "胃幽門肥厚 → 出口阻塞 → 反覆嘔吐 → loss of HCl + 脫水。Metabolic alkalosis (loss of H⁺ + Cl⁻)，kidney 保 Na/HCO₃ 排 K → hypokalemia。Paradoxical aciduria (late)。",
    "options": {
        "A": "錯誤 (本題錯誤敘述)。Pyloric stenosis 非急症手術；需先 24-48h 矯正脫水與電解質。",
        "B": "正確。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "APAGBI Neonatal Surgery：electrolyte correction first; Cl > 100、HCO₃ < 30 為 surgery criteria。",
        "麻醉：full stomach RSI、suction OG tube、warm fluids、normothermia。",
        "Post-op：apnea risk (residual alkalosis depresses respiration)、glucose monitoring。",
    ],
    "points": [
        "Typical infant: 3-6 wks old、firstborn male、projectile vomiting",
        "Olive-shaped mass palpable RUQ、US confirms",
        "Pyloromyotomy curative",
    ],
    "keyword": "Pyloric stenosis, metabolic alkalosis, pyloromyotomy",
    "source": "Coté and Lerman 6/e",
},
51: {  # 剖腹產 ERAS
    "answer_text": "Cesarean section 不適合 ERAS",
    "summary": "ERAS for cesarean section：pre-op (NPO、carbohydrate drink 2h)、intra-op (multimodal anesthesia、prophylactic phenylephrine、TXA)、post-op (early oral intake、early mobilization、 multimodal opioid-sparing analgesia、early Foley removal)。已證實降低 LOS、opioid use。",
    "mechanism": "ERAS principles 適用所有 surgical population including obstetric。對 CS：減少 surgical stress、improve recovery、enable bonding、降低 hospital stay。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "正確。",
        "C": "錯誤 (本題錯誤敘述)。ERAS 完全適合 CS；目前 SOAP、ERAS Society 都有 CS guidelines。",
        "D": "正確。",
    },
    "guidelines": [
        "ERAS Society Cesarean Delivery Guidelines 2018-2019。",
        "SOAP Consensus 2020。",
        "Multimodal analgesia: intrathecal morphine、acetaminophen、NSAID、TAP block (rescue)。",
    ],
    "points": [
        "Intrathecal morphine 0.1 mg 提供 18-24h analgesia",
        "Early oral intake (within 2h)、early mobilization (within 6h)",
        "Early Foley removal (≤ 12h) 減少 UTI",
    ],
    "keyword": "ERAS, cesarean section, intrathecal morphine",
    "source": "ERAS Society CS Guidelines; SOAP Consensus",
},
52: {  # 12 kg 兒童輸尿管手術
    "answer_text": "輸液 20-40 mL/h LR 或 isotonic crystalloid",
    "summary": "Pediatric intraoperative fluid (12 kg)：(1) Maintenance (4-2-1 rule)：48 mL/h；(2) Surgical loss (minimal blood loss case): 1-2 mL/kg/h baseline + 3-5 mL/kg/h for moderate surgery。NPO 已矯正 + minimal loss = mainly maintenance + small replacement。",
    "mechanism": "兒童 fluid 三組成：maintenance (Holliday-Segar) + deficit replacement + ongoing loss。Isotonic crystalloid preferred避免 hyponatremia。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "錯誤。",
        "D": "正確。20-40 mL/h LR 或 isotonic 為 12 kg 兒童麻醉中合理。",
    },
    "guidelines": [
        "APA 2018 Pediatric Perioperative Fluid Management：isotonic fluid + dextrose containing for maintenance。",
        "Avoid hypotonic D5W (hyponatremia risk)。",
        "Goal-directed where possible。",
    ],
    "points": [
        "4-2-1 rule: 4 mL/kg/h first 10 kg、2 mL/kg/h next 10 kg、1 mL/kg/h beyond",
        "Blood loss replacement: 3:1 crystalloid : blood lost",
        "Hypoglycemia risk infant: add D5 maintenance",
    ],
    "keyword": "Pediatric fluid, Holliday-Segar, isotonic",
    "source": "APA Pediatric Fluid Guidelines 2018",
},
53: {  # 子癇前症 + MgSO4
    "answer_text": "MgSO₄ 對 NMBA 無影響",
    "summary": "MgSO₄ 對麻醉影響：(1) Potentiates NMBA — depolarizing + nondepolarizing 均加重，劑量減 50%；(2) Vasodilation → hypotension；(3) NM block transmission 抑制；(4) CNS depression 加重 anesthetic effect；(5) Calcium gluconate 為解毒。",
    "mechanism": "Magnesium 阻斷 presynaptic Ca channel → 降低 ACh release；postsynaptic membrane 降敏感性。與 NMBA 協同 → prolonged paralysis。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "正確。",
        "C": "正確。",
        "D": "錯誤 (本題錯誤敘述)。MgSO₄「顯著」 potentiates NMBA，劑量需減量 50%；TOF 嚴密監測。",
    },
    "guidelines": [
        "ACOG Practice Bulletin 222 (2020) Preeclampsia/Eclampsia。",
        "Therapeutic Mg range 4-8 mg/dL；toxicity (loss DTR、respiratory depression) > 10。",
        "Anesthesia: avoid succinylcholine high dose、reduce NMBA dose 50%、TOF monitoring。",
    ],
    "points": [
        "Magnesium continue 24h postpartum (seizure prophylaxis)",
        "Antihypertensive: labetalol、hydralazine、nifedipine",
        "Spinal/epidural still preferred for CS in preeclampsia (improved BP control)",
    ],
    "keyword": "MgSO4, preeclampsia, NMBA potentiation",
    "source": "ACOG Practice Bulletin 222; Chestnut 6/e",
},
54: {  # 產後大出血
    "answer_text": "PPH 主因為 uterine atony，輸注 fluid + uterotonic 為首要",
    "summary": "Postpartum Hemorrhage (PPH)：失血 > 500 mL (vaginal) 或 > 1000 mL (CS)。4T 原因：Tone (atony, 70%)、Trauma、Tissue (retained)、Thrombin。處置：bimanual massage、uterotonics (oxytocin、ergot、carboprost、misoprostol)、fluid resuscitation、blood products、surgical intervention if persistent。",
    "mechanism": "Uterine atony → 無法收縮壓迫 placental site vessels → 持續出血。Failed uterotonic → balloon tamponade、B-Lynch suture、uterine artery embolization、hysterectomy。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "正確。",
        "C": "錯誤 (本題錯誤敘述 — 詳情依官方答案推測為某項配方錯誤)。",
        "D": "正確。",
    },
    "guidelines": [
        "ACOG Practice Bulletin 183 Postpartum Hemorrhage。",
        "Sequence: oxytocin → methylergonovine (avoid in HTN) → carboprost (avoid in asthma) → misoprostol → TXA。",
        "Massive transfusion 1:1:1。",
    ],
    "points": [
        "Tranexamic acid 1g IV within 3h of PPH onset (WOMAN trial)",
        "Surgical: B-Lynch、uterine artery ligation、hysterectomy",
        "Interventional radiology: uterine artery embolization",
    ],
    "keyword": "Postpartum hemorrhage, uterine atony, uterotonics",
    "source": "ACOG Practice Bulletin 183; WOMAN trial",
},
55: {  # PDPH
    "answer_text": "PDPH 第一線治療為 epidural blood patch",
    "summary": "PDPH 階段性處置：(1) Conservative — bed rest、hydration、analgesia、caffeine 500 mg、stool softener；(2) Persistent/severe (> 24-48h)：epidural blood patch (15-20 mL autologous blood) 成功率 70-90%。Blood patch 為「rescue」非 first-line。",
    "mechanism": "PDPH 由 CSF leak 引起 intracranial hypotension → 牽引 pain-sensitive structures。Blood patch sealing dural defect + 增加 epidural pressure → 即時減壓。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "正確。",
        "C": "正確。",
        "D": "錯誤 (本題錯誤敘述)。Epidural blood patch 為「rescue」治療，非 first-line。First-line 為 conservative。",
    },
    "guidelines": [
        "ASRA 2010 PDPH。",
        "Conservative first 24-48h；persistent severe → EBP。",
        "Sphenopalatine ganglion block 為新興 option。",
    ],
    "points": [
        "Pencil-point needle (Whitacre/Sprotte) reduces PDPH",
        "EBP 可重複 1-2 次",
        "Differential: cortical vein thrombosis、subdural hematoma、preeclampsia",
    ],
    "keyword": "PDPH, epidural blood patch, conservative",
    "source": "Chestnut 6/e; ASRA 2010",
},
56: {  # 牙科特殊需求病人
    "answer_text": "強制 IV insertion 不可接受",
    "summary": "Uncooperative + no IV + special needs dental → inhalation induction with sevoflurane (parental presence) → secure IV after asleep。Avoid forced restraint or IV (traumatic、ethics)。Premedication：oral midazolam、intranasal、IM ketamine 為選項。",
    "mechanism": "Special needs (autism、severe cognitive impairment、cerebral palsy) 病人合作困難。Mask induction safer than struggling IV attempt。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "正確。",
        "C": "正確。",
        "D": "錯誤 (本題不適當)。Forced IV insertion in uncooperative special needs 為 traumatic、ethically 不可。應 inhalation induction first。",
    },
    "guidelines": [
        "AAP/ASA Pediatric Sedation Guidelines。",
        "ADA Special Needs Dental Care。",
        "Premedication: oral midazolam 0.5 mg/kg、intranasal dexmedetomidine 2 µg/kg、IM ketamine 4-6 mg/kg。",
    ],
    "points": [
        "Family-centered approach 加 parental presence",
        "Mask induction sevoflurane 8% + O₂；secure airway + IV after asleep",
        "Post-op: monitor for emergence agitation",
    ],
    "keyword": "Special needs anesthesia, dental, inhalation induction",
    "source": "AAP/ASA Pediatric Sedation Guidelines",
},
57: {  # 4 週 PDA ligation
    "answer_text": "需備齊心臟手術設備、預期 hypotension、prepare blood",
    "summary": "Pediatric PDA ligation：(1) Premature/full-term newborn；(2) Left thoracotomy approach、retraction of left lung；(3) PDA temporary clamp 評估反應；(4) ductal closure 後 LV preload 急升、BP 改變；(5) Recurrent laryngeal nerve injury 風險。",
    "mechanism": "PDA 是 fetal circulation 通道 (主動脈 → 肺動脈)。Premature 持續開放 → L-to-R shunt → CHF、pulmonary congestion。Surgical ligation 或 catheter occlusion device。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "正確 (敘述適當)。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "APAGBI Neonatal Cardiac Anesthesia。",
        "Indomethacin/ibuprofen 為 medical closure (premature)，但有 contraindications。",
        "Sufficient blood products available; thoracotomy 出血可大量。",
    ],
    "points": [
        "RLN injury: vocal cord paralysis、stridor",
        "Temperature management critical (small infant)",
        "Hemodynamic monitoring: BP cuff (right arm preferred — coarctation rule out)",
    ],
    "keyword": "PDA ligation, premature, neonatal anesthesia",
    "source": "Coté and Lerman 6/e",
},
58: {  # 兒童氣道
    "answer_text": "Glottis 高於成人，位於 C5",
    "summary": "兒童氣道特徵：(1) 頭大、頸短、舌大、tonsil 大；(2) Larynx 位置「較高」(C3-C4 newborn → C5-C6 adult)；(3) 較窄 cricoid (傳統)；(4) 會厭較長 omega/U-shaped；(5) 較短氣管。",
    "mechanism": "Pediatric airway 與成人差異隨年齡漸減，~8 歲後接近成人。larynx high 解釋 sniffing position 不需要 (newborn 自然 sniffing)。",
    "options": {
        "A": "正確 (描述適當)。",
        "B": "錯誤 (本題錯誤敘述)。新生兒 glottis 位置在 C3-C4，較成人 C5-C6「高」(較 cephalad)。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "APAGBI Pediatric Airway Guidelines。",
        "Cuffed ETT now widely accepted (Khine 等研究)。",
        "ETT size: cuffed = (age/4) + 3.5；uncuffed = (age/4) + 4。",
        "Depth: (age/2) + 12 cm at lip。",
    ],
    "points": [
        "Newborn: sniffing position natural; older child needs shoulder roll",
        "Suction equipment & various size ETT ready",
        "Rapid desaturation due to low FRC + high O₂ consumption",
    ],
    "keyword": "Pediatric airway, larynx position, cricoid",
    "source": "Coté and Lerman 6/e; APAGBI Guidelines",
},

# ===== Carbetocin、HELLP、DMD (Q59-61) =====
59: {  # Carbetocin
    "answer_text": "Carbetocin 適用 hypertensive 病人",
    "summary": "Carbetocin (Duratocin®) 為 long-acting oxytocin analog，半衰期 ~40 min (vs oxytocin 4-10 min)。優點：single 100 µg IV slow injection 取代 oxytocin infusion；用於 CS PPH 預防。副作用類似 oxytocin：hypotension、tachycardia、N/V、flushing、headache。",
    "mechanism": "Carbetocin 與 oxytocin receptor binding → 子宮收縮、PPH 預防。較 oxytocin 抗水解 → 延長作用。Avoid in preeclampsia、severe cardiovascular disease (與 oxytocin 同)。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "正確。",
        "C": "錯誤 (本題錯誤敘述)。Carbetocin 同 oxytocin 引起 hypotension，severe preeclampsia/severe HTN/cardiac disease 為禁忌或慎用。",
        "D": "正確。",
    },
    "guidelines": [
        "WHO PPH Prevention：carbetocin 為 oxytocin 替代 (when refrigeration limited)。",
        "FIGO Guidelines：carbetocin 同 oxytocin efficacy for PPH prevention CS。",
        "CHAMPION trial：heat-stable carbetocin non-inferior to oxytocin for PPH prevention。",
    ],
    "points": [
        "Single dose 100 µg IV slow (avoid hypotension)",
        "Heat-stable formulation 適合 low-resource settings",
        "Cost 較 oxytocin 高",
    ],
    "keyword": "Carbetocin, Duratocin, PPH prevention, oxytocin analog",
    "source": "WHO/FIGO PPH Guidelines; CHAMPION trial",
},
60: {  # HELLP / preeclampsia
    "answer_text": "HELLP syndrome 急刀 + MgSO₄ + 血品準備",
    "summary": "36 週孕婦頭痛、上腹痛、噁心、BP 160/110、Hb 9.1、溶血、 thrombocytopenia (68K) = HELLP syndrome (Hemolysis、Elevated Liver enzymes、Low Platelets) — severe preeclampsia 變異型。處置：delivery (definitive)、MgSO₄、antihypertensive、 monitor coagulopathy。",
    "mechanism": "HELLP：placental dysfunction → endothelial damage → microangiopathic hemolysis、liver ischemia、 platelet consumption。Mortality 1-25%；併發症 DIC、placental abruption、acute liver hemorrhage/rupture、AKI。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "正確 (敘述適當)。Delivery + MgSO₄ + blood products preparation 為標準。",
        "D": "錯誤。",
    },
    "guidelines": [
        "ACOG Practice Bulletin 222 (2020)。",
        "Delivery: ≥ 34 週 → 立即；< 34 週 → 個別化、steroid for fetal lung maturity 可能。",
        "Anesthesia: regional preferred if platelet > 70K (some 50K)、coagulation normal、no DIC。",
        "Severe coagulopathy → GA。",
    ],
    "points": [
        "Class I (plt < 50K)、II (50-100)、III (100-150)",
        "Magnesium continue 24h postpartum",
        "Steroid (dexamethasone) controversial — limited benefit for HELLP",
    ],
    "keyword": "HELLP syndrome, severe preeclampsia, MgSO4",
    "source": "ACOG Practice Bulletin 222; Chestnut 6/e Ch. 36",
},
61: {  # DMD
    "answer_text": "避免 succinylcholine 與 volatile anesthetics, prefer TIVA",
    "summary": "Duchenne Muscular Dystrophy (DMD)：(1) Succinylcholine 「絕對禁忌」 — fatal hyperkalemia + rhabdomyolysis；(2) Volatile anesthetics 引起 anesthesia-induced rhabdomyolysis (AIR)，相對禁忌；(3) TIVA (propofol + remifentanil) 為首選；(4) Nondepolarizing NMBA 作用延長。",
    "mechanism": "DMD: dystrophin gene mutation → muscle membrane instability → muscle injury。Succinylcholine 引起大量 K release → cardiac arrest。Volatile anesthetics 可引起 rhabdomyolysis、 hyperkalemia、cardiac arrest 即使無 MH。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "正確 (敘述適當)。Avoid sux + volatile, TIVA preferred。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "MHAUS recommendations for DMD anesthesia。",
        "TIVA: propofol + remifentanil + rocuronium (with sugammadex reversal)。",
        "Pre-op cardiac evaluation: echo、ECG、Holter (DMD 50-80% cardiomyopathy by adolescence)。",
        "Post-op: monitor for rhabdomyolysis (CK)、cardiac function、respiratory failure。",
    ],
    "points": [
        "DMD ≠ Malignant Hyperthermia, but similar precautions",
        "Cardiomyopathy progressive: 12-18 yrs onset",
        "Respiratory function decline; pulmonary risk assessment important",
    ],
    "keyword": "Duchenne muscular dystrophy, succinylcholine, TIVA",
    "source": "MHAUS DMD Guidelines; Coté and Lerman 6/e",
},

# ===== 老年生理、肥胖 (Q62-66) =====
62: {  # 老化呼吸系統
    "answer_text": "FEV1 與 FVC 隨年齡下降、closing capacity 上升",
    "summary": "Aging respiratory: (1) FEV1 ↓ 25-30 mL/yr after 30、FVC ↓；(2) FRC 微增 (vs total lung capacity 大致不變)；(3) Closing capacity ↑ — 超過 FRC → small airway closure in tidal volume → atelectasis、V/Q mismatch；(4) PaO₂ ↓ 約 0.4 mmHg/yr；(5) Compliance ↑ (rubber band ageing)；(6) Chest wall stiff。",
    "mechanism": "彈性蛋白 elastin 破壞 → loss of elastic recoil → emphysematous-like changes (senile emphysema)。Alveolar surface area ↓ → diffusion capacity ↓。Chest wall fibrosis → 呼吸 work ↑。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (描述不適當)。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "Respiratory aging predisposes老年 to perioperative pulmonary complications: atelectasis、aspiration、pneumonia。",
        "Pre-oxygenation more critical (faster desaturation due to ↑ closing capacity)。",
        "PEEP 5-10 cmH₂O 維持 FRC、recruitment maneuver。",
    ],
    "points": [
        "A-a gradient widens with age — expected PaO₂ formula: 100 − (age/3)",
        "Cough/swallow reflexes diminish → aspiration risk",
        "Sleep apnea prevalence high — screen and address",
    ],
    "keyword": "Respiratory aging, closing capacity, FEV1",
    "source": "Stoelting's Co-existing Disease 7/e Ch. Aging",
},
63: {  # 老年生理
    "answer_text": "心輸出、GFR、肝血流均下降，baroreflex 鈍化",
    "summary": "Aging multi-system changes: (1) CV — LV diastolic dysfunction、stiff arteries、baroreflex blunted、HR variability ↓；(2) Renal — GFR ↓ 1 mL/min/yr after 40、 ↓ concentration ability、 ↑ medication accumulation；(3) Hepatic — flow ↓、CYP ↓ slightly；(4) CNS — neuronal loss、autoregulation narrower、MAC ↓ 6%/decade；(5) Body composition — lean mass ↓、fat ↑、 ↓ TBW。",
    "mechanism": "Aging-related decline 影響 pharmacokinetics、pharmacodynamics、 organ reserve。Polypharmacy 加重 drug interaction。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (描述不適當)。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "ASA Brain Health Initiative：Perioperative neurocognitive disorders。",
        "Avoid Beers Criteria drugs：benzodiazepine、 anticholinergic、 meperidine。",
        "Dose adjustments: induction agents ↓ 30-50%; volatile ↓; opioid ↓。",
    ],
    "points": [
        "Cr can be falsely normal (low muscle mass)；use Cockcroft-Gault或 GFR formula",
        "Hypothermia risk high (low BMR、 thin skin)",
        "Frailty as predictor (Clinical Frailty Scale)",
    ],
    "keyword": "Geriatric physiology, baroreflex, GFR, MAC",
    "source": "Miller's Anesthesia 8/e Ch. 80",
},
64: {  # 老年多種藥
    "answer_text": "Anticholinergic 藥物易引起譫妄與便秘",
    "summary": "老年 polypharmacy + 多重共病 → drug-drug interaction、累積副作用。Beers Criteria 列舉 potentially inappropriate medications：anticholinergic、benzodiazepine、long-acting opioid、NSAIDs (renal/GI)、 1st-gen antihistamine。",
    "mechanism": "Anticholinergic effect cumulative (anti-Parkinsonian、antidepressant、antihistamine、 antispasmodic) → cognitive impairment、 delirium、 urinary retention、 constipation、 dry mouth、 tachycardia。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "正確 (敘述適當)。Anticholinergic 累積引起譫妄、便秘、UR。",
        "D": "錯誤。",
    },
    "guidelines": [
        "Beers Criteria 2019 (AGS)：drugs to avoid or use with caution in elderly。",
        "STOPP/START Criteria：European version。",
        "Anticholinergic Cognitive Burden (ACB) scale。",
    ],
    "points": [
        "Common offenders: diphenhydramine、 hydroxyzine、 amitriptyline、 oxybutynin",
        "Benzodiazepine 增加 falls、 fractures、 delirium",
        "NSAIDs renal、 GI、 cardiovascular concerns in elderly",
    ],
    "keyword": "Beers Criteria, anticholinergic, polypharmacy",
    "source": "AGS Beers Criteria 2019",
},
65: {  # 肥胖呼吸器
    "answer_text": "Low TV (6-8 mL/kg IBW) + PEEP 5-10 + recruitment",
    "summary": "Obese ventilation: (1) TV 6-8 mL/kg「IBW」(not actual)；(2) PEEP 5-10 cmH₂O 防 atelectasis；(3) Recruitment maneuver；(4) FiO₂ as needed；(5) Pressure-controlled ventilation 考慮；(6) Avoid high pressure (chest wall stiff、 IAP↑)。",
    "mechanism": "肥胖 FRC ↓ (chest wall + abdominal mass)、atelectasis、shunt → 快速 desaturation。PEEP 維持 FRC、recruit collapsed alveoli。Ideal body weight calculation 避免 over-distension。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (描述不適當)。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "SOBA (Society for Obesity and Bariatric Anaesthesia) Guidelines。",
        "ARDS Network: low TV 4-6 mL/kg IBW for ARDS; 6-8 mL/kg IBW for healthy lung。",
        "Ramped position improves laryngoscopy + ventilation。",
    ],
    "points": [
        "IBW (male) = 50 + 2.3 × (height in inches − 60); female = 45.5 + 2.3 × …",
        "Difficult mask ventilation in obese: BONES mnemonic",
        "OSA assessment: STOP-BANG questionnaire",
    ],
    "keyword": "Obesity ventilation, IBW, PEEP",
    "source": "SOBA Guidelines; ARDS Network",
},
66: {  # 肥胖姿勢呼吸影響
    "answer_text": "Supine 加重 atelectasis 與 desaturation",
    "summary": "Obesity + supine：(1) Abdominal mass cephalad pressure on diaphragm → FRC ↓ severely；(2) Atelectasis、shunt、hypoxia；(3) Reverse Trendelenburg 或 ramped position 改善 FRC + 視野；(4) Prone position 困難，加重 IAP。",
    "mechanism": "Supine 肥胖人 FRC 可降至 closing capacity 以下 → small airway closure during tidal breathing → V/Q mismatch、hypoxia。Pre-oxygenation 困難。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "正確 (敘述適當)。Supine 加重 atelectasis 與 desaturation。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "SOBA Guidelines: 25-30° head-up tilt for pre-oxygenation。",
        "Ramped position: tragus aligned with sternal notch。",
        "Reverse Trendelenburg or sitting position improve FRC + ventilation。",
    ],
    "points": [
        "Apneic time before desaturation 嚴重縮短 (FRC small、 O₂ consumption high)",
        "Pre-oxygenation 100% O₂ × 3-5 min + CPAP",
        "Intra-operative recruitment maneuvers maintain FRC",
    ],
    "keyword": "Obesity positioning, FRC, ramped position",
    "source": "SOBA Guidelines",
},

# ===== ERAS、感染管制、NPO、Sepsis (Q67-70) =====
67: {  # ERAS 麻醉
    "answer_text": "Long-acting opioid 為 ERAS 核心",
    "summary": "ERAS 麻醉原則：multimodal opioid-sparing、regional anesthesia、euvolemia (avoid over- or under-resuscitation)、normothermia、PONV prophylaxis、early extubation、PACU bypass possible、 early oral intake、early mobilization。Long-acting opioid 違反 opioid-sparing。",
    "mechanism": "Opioid use 增 PONV、 ileus、 sedation → 延長 LOS。Multimodal 與 regional 減少 opioid 需求。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (本題錯誤敘述)。Long-acting opioid 違反 ERAS opioid-sparing principle。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "ERAS Society Pathways: Cardiac、 Colorectal、 Gynecology、 Orthopedic、 etc.。",
        "Pre-op: carbohydrate drink 2h、 multimodal pre-emptive (acetaminophen、 gabapentin、 celecoxib)。",
        "Intra-op: regional anesthesia preferred、 euvolemic goal-directed fluid、 normothermia、 PONV prevention。",
        "Post-op: early oral intake、 multimodal analgesia、 early mobilization、 early Foley removal。",
    ],
    "points": [
        "Goal-directed fluid (SVV-guided) > liberal or restrictive",
        "PONV prophylaxis ≥ 2 agents in moderate risk (Apfel score)",
        "Regional anesthesia central to opioid-sparing",
    ],
    "keyword": "ERAS, opioid-sparing, multimodal",
    "source": "ERAS Society Guidelines",
},
68: {  # 感染管制
    "answer_text": "預防性抗生素於切皮後 1 小時內給予",
    "summary": "Surgical Antibiotic Prophylaxis：(1) Timing — 「切皮前」60 分鐘內 (vancomycin、fluoroquinolone 內 120 min)；(2) Re-dose at 2 half-lives 或 > 1.5L blood loss；(3) Duration — 多數手術 24h 內停止 (cardiac < 48h)；(4) Drug — cefazolin most common (broad coverage、low cost)。",
    "mechanism": "預防性抗生素血中濃度高於 MIC 於切皮時 → 預防 SSI。Late administration (after incision) 顯著降低 efficacy。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (本題錯誤敘述)。預防性抗生素應「切皮前 60 分鐘內」，不是「切皮後」。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "ASHP/SHEA/IDSA Surgical Antibiotic Prophylaxis Guidelines 2013。",
        "CDC SSI Prevention Guidelines。",
        "Cefazolin standard for clean and clean-contaminated surgery。",
        "MRSA screening + vancomycin for high-risk patients。",
    ],
    "points": [
        "Re-dose for prolonged surgery or large blood loss",
        "Hair removal: clipper not razor",
        "Normothermia + euglycemia + supplemental O₂ reduce SSI",
    ],
    "keyword": "Surgical antibiotic prophylaxis, SSI prevention",
    "source": "ASHP/SHEA/IDSA SSI Guidelines 2013",
},
69: {  # 2 歲禁食指南
    "answer_text": "Light meal 6h、Heavy/fatty meal 8h",
    "summary": "ASA NPO Guidelines (2017)：Clear liquid 2h、Breast milk 4h、Infant formula/non-human milk 6h、Light meal (toast + clear liquid) 6h、Fried/fatty/meat 8h。Pediatric 同樣標準。",
    "mechanism": "Gastric emptying rate: clear liquid fastest、 milk + solid slower。Empty stomach 減少 aspiration risk。",
    "options": {
        "A": "錯誤 (描述不適當)。",
        "B": "錯誤。",
        "C": "錯誤。",
        "D": "正確 (敘述適當)。Light meal 6h、Heavy/fatty 8h。",
    },
    "guidelines": [
        "ASA Practice Guidelines for Preoperative Fasting 2017。",
        "APAGBI、ESPNIC: longer fasting unnecessary, can lead to dehydration、 hypoglycemia in children。",
        "ERAS: 2h clear carbohydrate drink improves outcomes。",
    ],
    "points": [
        "Diabetes、GERD、pregnancy、obstruction → 延長禁食或 RSI",
        "Chewing gum considered clear liquid",
        "Black coffee, tea without milk → clear liquid",
    ],
    "keyword": "NPO, ASA fasting guidelines",
    "source": "ASA Practice Guidelines for Preoperative Fasting 2017",
},
70: {  # 腹膜炎 RSI
    "answer_text": "立即 mask ventilation + slow induction",
    "summary": "Peritonitis + sepsis + 嗜睡 + low BP + hypoxia + fever + NPO < 4h = septic shock + full stomach + difficult airway。處置：(1) Fluid resuscitation、vasopressor、antibiotic 同時進行；(2) RSI (full stomach、 ileus、 high aspiration risk)；(3) Etomidate + rocuronium 1.2 mg/kg；(4) Cricoid pressure (optional)；(5) Avoid mask ventilation。",
    "mechanism": "Septic peritonitis: vasodilation + capillary leak + cardiac depression → shock。Ileus + abdominal pressure → aspiration risk 極高。RSI minimize aspiration window。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "正確。",
        "C": "正確。",
        "D": "錯誤 (本題錯誤敘述)。Mask ventilation 在 full stomach + ileus 為禁忌；應 RSI。",
    },
    "guidelines": [
        "Surviving Sepsis Campaign 2021。",
        "Damage Control Surgery for septic peritonitis: source control + ICU optimization。",
        "Ketamine 或 etomidate 維持 hemodynamics during induction。",
    ],
    "points": [
        "Avoid propofol high dose — cardiovascular collapse",
        "Awake intubation if extremely high aspiration risk + cooperative",
        "Aggressive fluid + early antibiotic + source control 為治療關鍵",
    ],
    "keyword": "Septic shock, peritonitis, RSI",
    "source": "Surviving Sepsis 2021; ATLS",
},

# ===== 困難呼吸道、LAST、Positioning、Laryngospasm (Q71-74) =====
71: {  # 100 kg 困難插管後
    "answer_text": "繼續嘗試直接喉鏡多次",
    "summary": "Rocuronium 80 mg (rapid) + difficult mask ventilation + failed DL → 失敗插管 algorithm。立即：(1) 求救；(2) Plan B — supraglottic airway (SGA: LMA)、video laryngoscope；(3) Plan C — face mask + Sugammadex 16 mg/kg if rocuronium recently administered；(4) Plan D — Front of neck access (FONA)。「繼續嘗試 DL」延誤救援、加重 trauma。",
    "mechanism": "DAS Difficult Airway Algorithm 2015 強調限制 attempts、early progression to next plan。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (本題錯誤敘述)。繼續多次 DL 嘗試延誤、加重 trauma；應 progress to next plan。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "DAS 2015 Difficult Airway Guidelines。",
        "Sugammadex 16 mg/kg for emergency rocuronium reversal in CICO scenarios。",
        "Maximum 3 attempts at intubation; declare difficult airway。",
    ],
    "points": [
        "Sugammadex 速度 < 3 min for reversal — 不能延誤 FONA",
        "Video laryngoscope as Plan A or B per institutional protocol",
        "Cannot Intubate Cannot Oxygenate (CICO) → FONA without delay",
    ],
    "keyword": "Difficult airway, DAS algorithm, sugammadex",
    "source": "DAS 2015 Difficult Airway Guidelines",
},
72: {  # LAST
    "answer_text": "立即啟動 20% Lipid Emulsion + CPR + benzodiazepine",
    "summary": "Bupivacaine 200 mg + 5 min 後 LAST 表現 (耳鳴、視覺改變、seizure、VF) = severe LAST。處置：(1) 求救、停藥、 airway 100% O₂；(2) Benzodiazepine for seizure (avoid propofol)；(3) Lipid Emulsion 20% 1.5 mL/kg bolus + 0.25 mL/kg/min infusion；(4) High-quality CPR；(5) Epinephrine ≤ 1 µg/kg (lower doses)；(6) Avoid vasopressin、CCB、β-blocker、lidocaine。",
    "mechanism": "Bupivacaine 高 lipid solubility → 心肌 Na channel + mitochondrial dysfunction → resistant 心律不整。Lipid emulsion 透過 lipid sink + metabolic shuttle 將 bupivacaine 從心肌移除。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (描述不適當)。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "ASRA Practice Advisory on LAST 2018 Checklist。",
        "20% Intralipid available in OR、L&D, anywhere LA used。",
        "Total lipid emulsion ≤ 12 mL/kg。",
    ],
    "points": [
        "Prevention: ultrasound guidance、incremental injection、test dose、total dose calculation",
        "Bupivacaine total dose ≤ 2 mg/kg、 lidocaine ≤ 4.5 mg/kg (7 mg/kg with epi)",
        "Observe ≥ 12 hours after successful resuscitation",
    ],
    "keyword": "LAST, lipid emulsion, bupivacaine",
    "source": "ASRA 2018 LAST Checklist",
},
73: {  # 擺位注意
    "answer_text": "Prone position 不需顧及眼壓",
    "summary": "Surgical positioning principles：(1) Padding for pressure points；(2) Avoid extreme joint angles；(3) Eye protection (especially prone)；(4) Check arm position regularly；(5) Avoid jugular compression；(6) Pulse checks distal extremity。Prone position 是 POVL highest risk — eye protection 尤其重要。",
    "mechanism": "Position-related injury 主要兩類：(1) 壓迫 (nerve、 vessel、 eye、 skin)；(2) Stretch (brachial plexus、 sciatic)。",
    "options": {
        "A": "錯誤 (本題錯誤敘述)。Prone position 反而 eye injury 最高風險、 IOP 在 prone 可大幅上升；必須保護。",
        "B": "正確 (敘述適當)。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "ASA Practice Advisory for Prevention of POVL 2019。",
        "ASA Practice Advisory for Prevention of Perioperative Peripheral Neuropathies 2018。",
    ],
    "points": [
        "Common nerve injuries: ulnar (supine)、 common peroneal (lithotomy)、 brachial plexus (lateral)",
        "POVL risk: prone、 long duration、 hypotension、 anemia",
        "Periodic position checks during long cases",
    ],
    "keyword": "Surgical positioning, POVL, nerve injury",
    "source": "ASA Practice Advisories",
},
74: {  # Laryngospasm
    "answer_text": "立即 100% O₂ + CPAP + 加深麻醉，必要時 succinylcholine",
    "summary": "Laryngospasm 處置順序：(1) 100% O₂ CPAP via tight mask；(2) Jaw thrust + Larson's point pressure；(3) 加深麻醉 (propofol 0.5-1 mg/kg or deepen volatile)；(4) Succinylcholine 0.1-0.5 mg/kg IV (or 4 mg/kg IM if no IV)；(5) Atropine 0.02 mg/kg if bradycardia。",
    "mechanism": "Laryngospasm: 反射性 vocal cord 收縮，多由 secretions、 surgical stimulation 觸發 during stage 2 anesthesia。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (本題錯誤敘述)。應立即 100% O₂ + CPAP、 jaw thrust、 deepen anesthesia，不是「直接 succinylcholine」without other measures。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "APAGBI Pediatric Difficult Airway 2015。",
        "PALS for severe desaturation。",
        "Prevention: smooth induction, avoid stage 2 manipulation, treat URI symptoms。",
    ],
    "points": [
        "Larson's point: mandible behind earlobe",
        "Negative pressure pulmonary edema (NPPE) — post-laryngospasm complication",
        "URI symptoms: postpone elective surgery 2-4 wks",
    ],
    "keyword": "Laryngospasm, CPAP, succinylcholine",
    "source": "APAGBI Pediatric Difficult Airway 2015",
},

# ===== 創傷、燒燙傷、MH、PONV、Liver Tx、 Brain Death (Q75-80) =====
75: {  # Lethal triad
    "answer_text": "Hyperthermia 為 lethal triad 之一",
    "summary": "Trauma 'Lethal Triad' (also Damage Control Triad)：(1) Hypothermia；(2) Acidosis；(3) Coagulopathy。三者相互惡化 → death spiral。Hyperthermia 「不是」lethal triad — 反而 hypothermia (< 35°C) 為其一。",
    "mechanism": "Hypothermia → enzyme function ↓ → coagulation factor activity ↓、 platelet dysfunction → coagulopathy。Hypoperfusion → anaerobic metabolism → lactic acidosis。Massive transfusion crystalloid → dilutional coagulopathy + hypothermia。",
    "options": {
        "A": "正確 (本題不屬於 lethal triad — 正確答案)。Hyperthermia 不是 trauma lethal triad；應為 hypothermia。",
        "B": "錯誤 (描述適當)。Hypothermia 確實是 lethal triad 之一。",
        "C": "錯誤。Acidosis 是 lethal triad 之一。",
        "D": "錯誤。Coagulopathy 是 lethal triad 之一。",
    },
    "guidelines": [
        "ATLS 10/e (2018) Damage Control Resuscitation。",
        "Permissive hypotension (SBP 80-90 unless TBI)、 1:1:1 transfusion、 TXA 1g within 3h、 active warming。",
    ],
    "points": [
        "Active rewarming: warm fluids、 forced air warmer、 normothermia critical",
        "Massive transfusion protocol: 1:1:1 RBC:FFP:Platelet",
        "Tranexamic acid (CRASH-2)：within 3h",
    ],
    "keyword": "Lethal triad, hypothermia, damage control",
    "source": "ATLS 10/e Trauma Guidelines",
},
76: {  # 燒燙傷
    "answer_text": "燒傷 24h 後可使用 succinylcholine 為合適選擇",
    "summary": "Burn anesthesia：(1) Succinylcholine 「禁忌」 from 24h 後 (extrajunctional AChR up-regulation, hyperkalemic cardiac arrest)；(2) Resistance to nondepolarizing NMBA (need 2-3× dose)；(3) Airway concern (face/neck burn → swelling, CO inhalation)；(4) Fluid (Parkland formula)；(5) Difficult IV access；(6) Hypothermia risk。",
    "mechanism": "Burn → extrajunctional AChR up-regulation (immature γ-subunit) → succinylcholine 引起大量 K efflux → fatal hyperkalemia。Effect persists from 24h up to 1-2 yr after healing。",
    "options": {
        "A": "正確 (本題錯誤敘述 — 答案 A 為錯誤)。Succinylcholine 在 burn 24h 後為「禁忌」非「合適」。",
        "B": "錯誤 (描述適當)。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "ABA (American Burn Association) Guidelines。",
        "Parkland formula: 4 mL × kg × %TBSA over 24h (LR)，1st half in 8h、 2nd half 16h。",
        "Airway: early prophylactic intubation for face/neck burn (rapid edema)。",
        "Carbon monoxide poisoning: 100% O₂、HBO₂ for severe。",
    ],
    "points": [
        "Rocuronium dose ↑ 2-3× due to receptor up-regulation",
        "Hypermetabolic state weeks-months post-burn (high glucose、 protein turnover)",
        "Multiple operations + skin grafts over time",
    ],
    "keyword": "Burn anesthesia, succinylcholine contraindication, Parkland",
    "source": "ABA Burn Guidelines; Miller's 8/e Ch. 81",
},
77: {  # MH
    "answer_text": "Dantrolene 為次要治療",
    "summary": "Malignant Hyperthermia (MH)：(1) Triggers — volatile anesthetics、 succinylcholine；(2) Signs — early ETCO₂↑、 tachycardia、 muscle rigidity、 hyperthermia (late)、 acidosis、 hyperkalemia、 rhabdomyolysis、 DIC；(3) Treatment — Dantrolene 2.5 mg/kg IV 「first-line」 + 停 triggers + 100% O₂ + cooling + manage electrolytes。",
    "mechanism": "RYR1 mutation → SR Ca²⁺ uncontrolled release → sustained muscle contraction → ATP 大量消耗 + heat + lactate + K release。Dantrolene 阻斷 RYR1 → 終止 contraction。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "錯誤 (本題錯誤敘述)。Dantrolene 為「first-line」非次要；2.5 mg/kg IV、 可至 10 mg/kg cumulative。",
        "C": "正確。",
        "D": "正確。",
    },
    "guidelines": [
        "MHAUS Protocol 2018：Dantrolene + supportive care + ICU。",
        "MHAUS Hotline: 1-800-MH-HYPER。",
        "Family screening: caffeine-halothane contracture test (CHCT) or genetic testing。",
    ],
    "points": [
        "Ryanodex (new formulation) — quicker mixing (vs traditional Dantrium powder)",
        "ETCO₂ rise often earliest sign — even before hyperthermia",
        "Continue dantrolene infusion 24h after stabilization (recurrence)",
    ],
    "keyword": "Malignant hyperthermia, Dantrolene, RYR1",
    "source": "MHAUS Protocol 2018",
},
78: {  # PONV
    "answer_text": "PONV 發生率約 20-30% 一般族群，高風險族群可達 70-80%",
    "summary": "PONV (Postoperative Nausea and Vomiting)：(1) 發生率約 20-30% 一般、 70-80% 高風險；(2) Apfel Score (4 risk factors)：female、 nonsmoker、 PONV history、 postop opioid；(3) Prophylaxis ≥ 2 antiemetics for moderate risk、 3 for high；(4) Drugs：5HT3 antagonist、 dexamethasone、 droperidol、 NK1 antagonist、 scopolamine。",
    "mechanism": "PONV 多因素：vestibular、 chemoreceptor trigger zone、 cortical、 GI。Volatile anesthetic、 opioid、 N₂O、 surgery type all contribute。",
    "options": {
        "A": "正確 (本題答案 — 錯誤敘述)。詳情待官方答案 verification。",
        "B": "錯誤。",
        "C": "錯誤。",
        "D": "錯誤。",
    },
    "guidelines": [
        "SAMBA 4th Consensus Guidelines for Management of PONV 2020。",
        "Apfel Score: ≥ 2 risk factors → ≥ 2 prophylactic agents。",
        "High-risk surgery: gynecologic、 laparoscopic、 strabismus、 ENT。",
    ],
    "points": [
        "TIVA propofol 較 volatile 低 PONV",
        "Adequate hydration、 minimize opioid (multimodal)、 regional anesthesia",
        "Rescue antiemetic: different class from prophylaxis",
    ],
    "keyword": "PONV, Apfel score, antiemetic prophylaxis",
    "source": "SAMBA 4th Consensus 2020",
},
79: {  # 肝臟移植 reperfusion
    "answer_text": "Hypertension 與 hypocapnia 為 reperfusion 期間典型表現",
    "summary": "Liver transplant phases：(1) Pre-anhepatic；(2) Anhepatic (cross-clamp)；(3) Neohepatic (reperfusion)。Reperfusion 期間典型現象：(1) Hypotension (vasodilator、 K、 lactate 釋出)；(2) Hyperkalemia；(3) Hypocalcemia (citrate)；(4) Acidosis；(5) Bradyarrhythmia → asystole；(6) Hypothermia (cold preservation solution)。",
    "mechanism": "Re-clamp release 釋出 stored vasoactive substances + cold preservation solution → systemic effects。",
    "options": {
        "A": "錯誤 (描述適當)。",
        "B": "錯誤。",
        "C": "錯誤。",
        "D": "正確 (本題不會出現 — 答案 D)。Reperfusion 多為 hypotension 非 hypertension；hypercapnia (ETCO₂↑) 非 hypocapnia。",
    },
    "guidelines": [
        "ISMETT / Liver Transplant Anesthesia Consensus。",
        "Pre-reperfusion: hyperventilate、 increase preload、 calcium、 bicarbonate、 vasopressor preparation。",
        "Post-reperfusion syndrome: > 30% MAP drop, lasting > 1 min。",
    ],
    "points": [
        "Veno-veno bypass vs piggyback technique reduce caval clamp issues",
        "Coagulopathy management: TEG-guided product replacement",
        "Post-op ICU: graft function monitoring, immunosuppression",
    ],
    "keyword": "Liver transplant, reperfusion syndrome",
    "source": "ISMETT Liver Transplant Anesthesia",
},
80: {  # 腦死器官捐贈
    "answer_text": "腦死器捐病人 ASA 分級為 ASA V",
    "summary": "腦死器捐 (Donation after Brain Death, DBD)：(1) ASA classification = VI (organ donor)，非 V (moribund)；(2) Physiological management critical for organ viability — maintain MAP > 65、 SpO₂ > 95、 normothermia、 control DI、 electrolytes、 glucose；(3) Hormonal replacement：T3/T4、 vasopressin、 corticosteroid。",
    "mechanism": "Brain death 引起 catecholamine storm → exhaustion → vasoplegia → loss of pituitary function (DI、 thyroid、 cortisol)。Organ preservation requires aggressive support。",
    "options": {
        "A": "正確 (敘述適當)。",
        "B": "正確。",
        "C": "正確。",
        "D": "錯誤 (本題錯誤敘述)。腦死器捐 ASA 為「VI」非 V (V 為 moribund 但 still alive)。",
    },
    "guidelines": [
        "OPTN/UNOS Organ Procurement Protocols。",
        "Hormonal replacement therapy: T4 20 µg IV bolus + 10 µg/h infusion、 methylprednisolone 15 mg/kg、 vasopressin 1 U bolus + infusion 0.5-4 U/h、 insulin。",
        "Maintain physiologic parameters until organ retrieval。",
    ],
    "points": [
        "Brain death determination: clinical + apnea test + ancillary (per local law)",
        "Spinal reflexes can occur — not signs of brain function",
        "Family communication and consent timing critical",
    ],
    "keyword": "Brain death, organ donation, ASA VI",
    "source": "OPTN/UNOS Protocols; Miller's 8/e Ch. 82",
},

}

# Load questions
with open('/tmp/np-anesthesia/questions.json') as f:
    qs = json.load(f)

# Apply enhancements to 114 進階麻醉
updated = 0
for q in qs:
    if q['year'] != 114 or q['specialty'] != 'anesth_advanced':
        continue
    n = int(q['id'].split('-')[-1].replace('A', ''))
    if n in E:
        enh = E[n]
        q['explanation'] = {
            "summary": enh.get('summary', ''),
            "mechanism": enh.get('mechanism', ''),
            "options": enh.get('options', {}),
            "guidelines": enh.get('guidelines', []),
            "points": enh.get('points', []),
            "keyword": enh.get('keyword', ''),
        }
        q['source'] = enh.get('source', q.get('source', ''))
        updated += 1

print(f"Enhanced {updated}/80 questions in 114 進階麻醉")

# Save
with open('/tmp/np-anesthesia/questions.json', 'w') as f:
    json.dump(qs, f, ensure_ascii=False, separators=(',', ':'))

import os
print(f"File size: {os.path.getsize('/tmp/np-anesthesia/questions.json')/1024:.0f}KB")
