#!/usr/bin/env python3
"""
Rebuild detailed explanations for 114 進階麻醉 80 questions.
KEY DIFFERENCE FROM PREVIOUS ATTEMPT: This time using VERIFIED official answers.
Each explanation defends the OFFICIAL correct answer (not my fabricated one).
"""
import json
import re

# Each entry: answer letter(s) verified from official PDF
E = {}

def add(n, summary, mechanism, options, guidelines, points, keyword, source):
    E[n] = {
        "summary": summary.strip(),
        "mechanism": mechanism.strip(),
        "options": options,
        "guidelines": guidelines,
        "points": points,
        "keyword": keyword.strip(),
        "source": source.strip(),
    }

# ===== Q1 (C: ③④) 腸道營養 =====
add(1,
    summary="③④ 正確。鼻胃管錯位常見於昏迷反射差病人；長期 (>4 週) 灌食建議 PEG。①②錯：EN 優於 PN；腹瀉應先找原因非單純止瀉。",
    mechanism="EN 維持腸黏膜屏障、保留 GALT 免疫、減少 bacterial translocation；只要 GI tract 可用即應優先於 PN。腸道灌食腹瀉多源於 osmolality 過高、灌食速率快、抗生素引起 C. difficile、感染、低 albumin，非纖維素不足。",
    options={
        "A": "錯誤。①「PN 優於 EN」違反 ASPEN/ESPEN 共識，EN 應為首選。",
        "B": "錯誤。②「止瀉藥+減纖維」處置不對，應先找原因 (osmolality、speed、infection)。",
        "C": "正確。③ NG 錯位於昏迷者常見；④ PEG 為長期 (>4-6 週) 灌食標準術式。",
        "D": "錯誤。①錯如上。",
    },
    guidelines=[
        "ASPEN/SCCM 2016：ICU 病人 24-48h 內啟動 EN；目標卡路里 7-10 天達成。",
        "ESPEN 2019：EN 優於 PN，除非有 contraindication (intestinal failure、obstruction、severe shock)。",
        "PEG 適應症：預期 EN ≥ 4 週、神經吞嚥障礙、頭頸癌、嚴重腦傷。",
    ],
    points=[
        "EN benefits：低成本、低感染、維持腸黏膜、減少 bacterial translocation",
        "EN 禁忌：機械性腸阻塞、severe shock、severe ileus、GI ischemia",
        "灌食腹瀉處理：稀釋、降速、找感染源 (尤其 C. difficile)",
    ],
    keyword="Enteral nutrition, NG tube placement, PEG",
    source="ASPEN/SCCM 2016 Critical Care Nutrition Guidelines; Miller's Anesthesia 8/e Ch. 84",
)

# ===== Q2 (C: HbA1c) 營養狀態評估指標 =====
add(2,
    summary="HbA1c 反映 3 個月平均血糖控制，是「血糖控制」指標，不直接反映「營養狀態」。BMI、albumin、hemoglobin 均為常用營養指標。",
    mechanism="營養評估三維度：(1) anthropometric (體重變化、BMI、midarm circumference、 triceps skinfold)；(2) biochemical (albumin、prealbumin、transferrin)；(3) hematologic (Hb 反映 iron、protein、B12/folate)。HbA1c 為糖化血紅素，反映糖尿病控制非營養。",
    options={
        "A": "錯誤 (是營養指標)。BMI 為粗略人體測量學指標，反映體重/身高關係。",
        "B": "錯誤 (是營養指標)。Albumin 半衰期 20 天，<3.5 g/dL 提示營養不良或炎症。",
        "C": "正確 (不是營養指標)。HbA1c 為血糖控制指標，與營養狀態無直接相關。",
        "D": "錯誤 (是營養指標)。Hemoglobin 反映 protein、iron、B12/folate 攝取，為間接營養指標。",
    },
    guidelines=[
        "ASPEN 2019：營養評估應綜合 SGA (Subjective Global Assessment) + NRS-2002 + biochemistry。",
        "ESPEN GLIM Criteria 2018：診斷 malnutrition 需 ≥1 phenotypic + ≥1 etiologic criteria。",
        "ADA：DM 病人 HbA1c < 7% 為一般目標；< 8% 為老年/合併症。",
    ],
    points=[
        "Prealbumin 半衰期 2 天，反映短期變化最敏感",
        "Albumin 受 inflammation、肝功能、水分影響，非純營養指標",
        "NRS-2002 為 ESPEN 推薦 ICU screening tool",
    ],
    keyword="Nutritional assessment, HbA1c, albumin, BMI",
    source="ESPEN/ASPEN Guidelines; Miller's Anesthesia 8/e Ch. Nutrition",
)

# ===== Q3 (A) 嚴重高血鉀 — Ca gluconate 不降鉀 =====
add(3,
    summary="Ca gluconate 「穩定心肌膜電位」防止致命心律不整，但「不降低血清鉀濃度」。降鉀需 insulin/glucose、β2-agonist、HCO₃ (shift) 或 dialysis/resin (remove)。",
    mechanism="高鉀升高靜止膜電位 (RMP) 接近 threshold → 心肌 Na channel 失活 → 致命心律不整。Ca²⁺ 升高 threshold potential → 重新拉開差距，穩定心肌但「不改變」K 濃度。Insulin 活化 Na/K ATPase 將 K 推入細胞；β2-agonist 同機轉；HCO₃ 矯正 acidosis 同時 H/K exchange。",
    options={
        "A": "錯誤 (本題不適當的選項)。Ca gluconate 「穩定心肌」非「降鉀」；此敘述混淆兩種作用。",
        "B": "正確。Insulin 10 U + D50 25-50g 15 分鐘起效 shift K 入細胞。",
        "C": "正確。NaHCO₃ 對 acidosis 病人特別有效，shift K 入細胞。",
        "D": "正確。β2-agonist (albuterol、salbutamol) nebulizer 可降鉀 0.5-1 mEq/L。",
    },
    guidelines=[
        "KDIGO 2020 Acute Hyperkalemia: (1) 心肌穩定 Ca gluconate 1g IV slow 2-5 min；(2) Shift insulin/glucose、β2、HCO₃；(3) Remove diuretic、resin、dialysis。",
        "ACLS：嚴重高鉀 (K > 6.5 + EKG changes) 立即 Ca、insulin/D50；考慮 HD。",
        "EKG 變化：peaked T → wide QRS → sine wave → VF/asystole。",
    ],
    points=[
        "Ca gluconate 10% 10 mL IV slow 2-5 min；30 分鐘可重複",
        "Insulin/glucose 後監測血糖 ≥ 6h (delayed hypoglycemia)",
        "Sodium polystyrene sulfonate (Kayexalate) 效果緩，與 bowel necrosis 相關，已減少使用",
    ],
    keyword="Hyperkalemia, calcium gluconate, membrane stabilization",
    source="KDIGO 2020 Hyperkalemia; Stoelting's Co-existing Disease 7/e Ch. Renal",
)

# ===== Q4 (CD 多答) 成人營養需求不適當 =====
add(4,
    summary="C、D 兩個都是「不適當」的敘述。BMI 25-29 肥胖病人之熱量計算應用 adjusted weight，非單純按 actual。某些組織需 glucose，但每日約 100-130g 而非 40g。",
    mechanism="肥胖病人 lean body mass 與 metabolic rate 並非與 weight 線性相關。Adjusted Body Weight (ABW) = IBW + 0.25×(Actual−IBW)。腦約 100-120g glucose/天為基本需求 (非 40g)；RBC、腎髓質、眼水晶體無 mitochondria 需依賴 glucose。",
    options={
        "A": "正確 (是適當的敘述)。RDA 蛋白質 0.8 g/kg 滿足 97% 健康成人。",
        "B": "正確 (是適當的敘述)。重症 protein ≥ 1.2-1.5 g/kg (ASPEN/SCCM 2016)；嚴重 catabolism 可達 2 g/kg。",
        "C": "錯誤 (本題答案之一)。BMI 25-29 計算需求應採 ABW 或 IBW，21-25 kcal/kg/day 描述不精確。",
        "D": "錯誤 (本題答案之一)。腦每日 glucose 需求約 100-130g 維持，非 40g。",
    },
    guidelines=[
        "ASPEN/SCCM 2016：重症一般 25-30 kcal/kg/day；肥胖採 hypocaloric high-protein。",
        "ESPEN 2019：indirect calorimetry 為金標準；無 IC 時用 weight-based formula。",
        "ADA 限糖飲食仍需 ≥ 130 g/day 維持腦能量。",
    ],
    points=[
        "重症肥胖 (BMI > 30) hypocaloric high-protein：11-14 kcal/kg actual + protein 2 g/kg IBW",
        "蛋白質為 lean mass 維持關鍵，重症期間優先",
        "Refeeding syndrome 風險：低 P、低 K、低 Mg → 補充 + 慢速啟動",
    ],
    keyword="Caloric requirements, obesity, hypocaloric high-protein, glucose requirement",
    source="ASPEN/SCCM 2016 Critical Care Nutrition Guidelines",
)

# ===== Q5 (D) 病毒性腦炎 — MRI 枕葉錯誤 =====
add(5,
    summary="HSV-1 腦炎典型侵犯「顳葉、額葉」(temporal, frontal lobes)，「不是枕葉」。MRI T2/FLAIR temporal lobe hyperintensity 為經典表現。",
    mechanism="HSV-1 經 olfactory 或 trigeminal pathway 進入 CNS，攻擊 temporal/frontal lobe (而非枕葉)。CSF：lymphocytic pleocytosis、protein↑、可有 RBC (haemorrhagic necrosis)、HSV PCR sensitivity > 95% (1-3 天後)。",
    options={
        "A": "正確。HSV-1 為成人急性病毒性腦炎最常見原因。",
        "B": "正確。Fever、AMS、personality change、seizure 為典型四主徵。",
        "C": "正確。CSF 應做 HSV PCR 與 enterovirus PCR 兩者並查。",
        "D": "錯誤 (本題不適當)。MRI 雖為最敏感影像，但 HSV-1 典型病灶在「顳葉/額葉」非「枕葉」。",
    },
    guidelines=[
        "IDSA Encephalitis Guidelines 2008：所有疑似病毒性腦炎應立即 empiric Acyclovir 10 mg/kg IV q8h，待 CSF HSV PCR。",
        "Acyclovir 早期 (< 4 天) 啟動可降死亡率 70% → 28%。",
        "MRI > CT；EEG 可見 PLEDs (periodic lateralized epileptiform discharges)。",
    ],
    points=[
        "HSV-1 典型 MRI 部位為 temporal/frontal lobe (非枕葉)",
        "經典 CSF：lymphocytic pleocytosis + 紅血球 (haemorrhagic necrosis)",
        "Acyclovir empiric treatment 不待確診 — early treatment 改變預後",
    ],
    keyword="Viral encephalitis, HSV-1, temporal lobe, acyclovir",
    source="IDSA Encephalitis Guidelines 2008; Harrison's Principles of Internal Medicine",
)

# ===== Q6 (C) Aminoglycosides 不適當 =====
add(6,
    summary="Aminoglycosides 在低 pH、低氧、膿瘍環境中「活性顯著下降」。其作用需要 oxygen-dependent active transport 進入細菌，故在膿瘍與 anaerobic 環境效果差。",
    mechanism="Aminoglycoside 進入細菌需 O₂-dependent transport (energy-dependent phase I 與 II)。低 pH 抑制 transport、anaerobic 環境無 O₂、膿瘍 acidic 環境均降低效力。故對 abscess 與 anaerobe 無效。",
    options={
        "A": "正確。與 30S ribosomal subunit 結合，mRNA 誤讀，抑制蛋白合成。",
        "B": "正確。與 β-lactam 併用 (synergy)，對嚴重 Gram-negative 感染與心內膜炎有效。",
        "C": "錯誤 (本題不適當)。低 pH/低 O₂/膿瘍環境中 aminoglycoside 活性「顯著下降」，需先 source control (drainage)。",
        "D": "正確。Nephrotoxicity (近端腎小管，可能可逆但持續暴露不可逆)、ototoxicity (cochlear + vestibular，不可逆)。",
    },
    guidelines=[
        "IDSA：Once-daily extended-interval dosing (5-7 mg/kg) 為 standard，except 妊娠、心內膜炎、嚴重 burn、CrCl < 20。",
        "TDM：Trough < 1 µg/mL (gentamicin) 避免 nephrotoxicity。",
        "對 abscess 應先 drainage source control + 抗生素治療。",
    ],
    points=[
        "Bactericidal: β-lactam、aminoglycoside、fluoroquinolone、vancomycin、metronidazole",
        "Aminoglycoside 對 anaerobe (Bacteroides、Clostridium) 無效",
        "與 NMBA 協同 (Mg、neostigmine 亦可加重)，麻醉中監測 TOF",
    ],
    keyword="Aminoglycosides, abscess penetration, oxygen-dependent transport",
    source="Sanford Guide to Antimicrobial Therapy; Stoelting's Pharmacology 5/e",
)

# ===== Q7 (D) TMP-SMX 無法治療 Pseudomonas =====
add(7,
    summary="TMP-SMX (Baktar®) 廣效，但對 Pseudomonas aeruginosa「天然抗藥」。可治 PCP、Nocardia、Stenotrophomonas、MRSA skin、Toxoplasma、E. coli UTI。",
    mechanism="TMP 阻斷 dihydrofolate reductase；SMX 阻斷 dihydropteroate synthetase；兩段協同阻斷 folate synthesis → bacterial DNA synthesis 抑制。Pseudomonas 對 TMP-SMX 完全天然抗藥 (intrinsic resistance via efflux pump + altered targets)。",
    options={
        "A": "錯誤 (TMP-SMX 可治療)。Pneumocystis jirovecii 為 TMP-SMX 首選治療與預防。",
        "B": "錯誤 (TMP-SMX 可治療)。E. coli UTI 是 TMP-SMX 典型適應症。",
        "C": "錯誤 (TMP-SMX 可治療)。MRSA skin/soft tissue infection 可用 TMP-SMX。",
        "D": "正確 (本題答案)。Pseudomonas aeruginosa 對 TMP-SMX 天然抗藥；需 ceftazidime、cefepime、carbapenem、piperacillin-tazobactam、aminoglycoside、fluoroquinolone。",
    },
    guidelines=[
        "CDC PCP Prophylaxis：HIV CD4 < 200 給 TMP-SMX 1 SS/day。",
        "Pseudomonas 感染：anti-pseudomonal β-lactam ± aminoglycoside or fluoroquinolone。",
        "TMP-SMX 副作用：Stevens-Johnson syndrome、TEN、hyperkalemia、bone marrow suppression、kernicterus 新生兒。",
    ],
    points=[
        "TMP-SMX 涵蓋：Gram+ (含 MRSA)、Gram- (E. coli、Klebsiella、Stenotrophomonas)、PCP、Nocardia、Toxoplasma",
        "不涵蓋：Pseudomonas、Mycobacterium、anaerobe、Enterococcus",
        "G6PD deficiency 可引起 hemolysis",
    ],
    keyword="TMP-SMX, Pseudomonas, sulfamethoxazole",
    source="Sanford Guide; CDC Antimicrobial Guidelines",
)

# ===== Q8 (D) 細菌性心內膜炎 =====
add(8,
    summary="發燒+ tachycardia + leukocytosis + 高 CRP + 「指甲夾板出血 (splinter hemorrhage)」 + 「主動脈瓣區舒張期心雜音」= 細菌性心內膜炎 (IE) 典型表現。",
    mechanism="細菌性心內膜炎：細菌附著於 valve (尤其 aortic、mitral) → vegetation 形成 → 瓣膜功能不全 (regurgitation murmur) + 系統性栓塞 (splinter hemorrhage、Janeway lesion、Osler node、Roth spots)。",
    options={
        "A": "錯誤。腹膜炎主要 abdominal pain + peritoneal sign，與本題敘述不符。",
        "B": "錯誤。Myocarditis 雖有 fever + tachycardia，但通常無 splinter hemorrhage 或 valve murmur。",
        "C": "錯誤。Pericarditis 表現為 chest pain + friction rub，非舒張期 murmur。",
        "D": "正確 (本題答案)。發燒 + leukocytosis + splinter hemorrhage + AR murmur = 典型 IE。",
    },
    guidelines=[
        "Duke Criteria：major (BC + echo vegetation) + minor (fever、predisposing condition、vascular phenomena、immunologic、microbiologic evidence) 診斷 IE。",
        "Empiric AB：vancomycin + ceftriaxone (native valve)；vancomycin + gentamicin + cefepime (prosthetic)。",
        "TEE 較 TTE 敏感於 vegetation 偵測。",
    ],
    points=[
        "Splinter hemorrhage、Janeway lesion (palms/soles)、Osler nodes (painful)、Roth spots、conjunctival petechiae",
        "Most common organism: Staph aureus (acute)、Strep viridans (subacute)、Enterococcus",
        "Surgical indications: large vegetation、heart failure、abscess、persistent bacteremia",
    ],
    keyword="Infective endocarditis, Duke criteria, splinter hemorrhage",
    source="AHA/IDSA IE Guidelines; Harrison's Internal Medicine",
)

# ===== Q9 (C) Mobitz II =====
add(9,
    summary="70 歲女性暈厥 + EKG 顯示固定 PR + 突然 dropped beats = Mobitz type II (位於 infranodal HIS-Purkinje system)，高度進展至 complete AV block 風險，需 permanent pacemaker。",
    mechanism="Mobitz II：PR interval 固定，間歇 P 波不傳導 (dropped QRS)，無 progressive PR prolongation。病灶在 His-Purkinje system (infranodal)，常合併 wide QRS。風險高、不可逆。",
    options={
        "A": "錯誤。First-degree AV block：PR > 200 ms 但每個 P 都跟 QRS，無 dropped beats。",
        "B": "錯誤。Mobitz I (Wenckebach)：PR 漸進延長後 dropped beat；多 AV nodal、相對良性。",
        "C": "正確 (本題答案)。Mobitz II：固定 PR、間歇 dropped beats、infranodal、症狀性需 pacemaker。",
        "D": "錯誤。Complete AV block：P 與 QRS 完全 dissociation、independent rates。",
    },
    guidelines=[
        "ACC/AHA/HRS 2018 Bradycardia Guidelines：Mobitz II 與 symptomatic AV block 為 permanent pacemaker class I 適應症。",
        "暫時處置：transcutaneous pacing；atropine 對 infranodal block 效果有限。",
        "Avoid β-blocker、CCB、digoxin。",
    ],
    points=[
        "Mobitz I (Wenckebach)：常 AV nodal、伴隨 narrow QRS、無需 pacing",
        "Mobitz II：常 infranodal、wide QRS、需 pacing",
        "2:1 AV block 須由 PR 變化判斷是 I 或 II",
    ],
    keyword="Mobitz type II, AV block, pacemaker",
    source="ACC/AHA/HRS 2018 Bradycardia and Cardiac Conduction Delay Guidelines",
)

# ===== Q10 (A) Adhesive SBO =====
add(10,
    summary="60 歲女性曾剖腹產 + 膽囊切除 (= 腹部手術史) + 腹痛 + 噁心嘔吐 + KUB air-fluid levels + distended small bowel = 沾黏性小腸阻塞 (adhesion 占 SBO 60-75%)。",
    mechanism="腹部手術後腹膜沾黏為 SBO 最常見原因。機械性阻塞 → 阻塞上方腸道擴張、積氣積液、嘔吐電解質流失 (代謝性鹼中毒 + hypokalemia)。Strangulation 風險：fever、tachycardia、peritonitis、lactate↑、CT free fluid → 急刀。",
    options={
        "A": "正確 (本題答案)。Adhesive SBO 為手術後最常見原因，典型 KUB 表現。",
        "B": "錯誤。大腸阻塞影像表現不同 (haustral pattern、cecal distension)，常因 colon cancer/volvulus。",
        "C": "錯誤。Ischemic colitis 多為 LLQ pain、bloody diarrhea。",
        "D": "錯誤。Small bowel diverticulitis 罕見，無此典型 KUB 表現。",
    },
    guidelines=[
        "EAST Practice Management Guidelines for SBO：CT 為首選 imaging；保守治療 (NG decompression + IV fluid + electrolyte correction) 對 partial/simple 60-85% 成功。",
        "緊急手術指標：peritonitis、ischemia、closed-loop、failure of conservative trial 48-72h。",
        "麻醉：RSI (full stomach)、aspiration 防護、可能 hypovolemic shock。",
    ],
    points=[
        "SBO 4 大常見原因：adhesion (60-75%)、hernia (10-20%)、malignancy (10%)、IBD/intussusception",
        "Closed-loop obstruction 為手術急症 (ischemia 風險)",
        "麻醉誘導：NG decompression、 RSI 預防 aspiration",
    ],
    keyword="Small bowel obstruction, adhesion, RSI",
    source="EAST Practice Management Guidelines for SBO",
)

# ===== Q11 (A) Prerenal AKI 不符 — FENa > 1% =====
add(11,
    summary="腎前性 AKI 因腎元功能正常，努力保留 Na 與水，FENa「應 < 1%」。FENa > 1% 為 intrinsic AKI (ATN) 特徵，不符合 prerenal AKI 診斷。",
    mechanism="腎前性 AKI：RAAS + ADH 活化 → 近端腎小管 Na 重吸收增加、髓質集尿 → 高比重、 高 osmolality、低 Na、低 FENa、BUN/Cr 比上升 (preferential urea reabsorption)。ATN：腎小管 dysfunction → 無法保 Na → FENa↑、osmolality 接近血漿。",
    options={
        "A": "正確 (本題不符 prerenal)。FENa > 1% 為 intrinsic AKI 特徵；prerenal 應 < 1%。",
        "B": "錯誤 (符合 prerenal)。Urine osmolality > 500 mOsm/kg 表示集中尿，為 prerenal 典型。",
        "C": "錯誤 (符合 prerenal)。BUN/Cr > 20 為 prerenal 特徵 (preferential urea reabsorption)。",
        "D": "錯誤 (符合 prerenal)。FEUrea < 35% 為 prerenal 特徵；diuretic 使用後 FEUrea 比 FENa 更可靠。",
    },
    guidelines=[
        "KDIGO 2012 AKI：分 prerenal、intrinsic、postrenal；Stage 1-3 依 SCr 與 urine output。",
        "FENa = (UNa × PCr) / (PNa × UCr) × 100；diuretic 後改用 FEUrea。",
        "處置：恢復灌流 (fluid、CO 改善、stop nephrotoxin)；persistent → 進入 ATN。",
    ],
    points=[
        "ATN urine sediment：muddy brown granular casts",
        "Postrenal AKI：bilateral hydronephrosis (BPH、stone、tumor)",
        "Prerenal 早期可逆，延誤 → ATN (irreversible)",
    ],
    keyword="Prerenal AKI, FENa, BUN/Cr ratio, ATN",
    source="KDIGO 2012 AKI Guidelines",
)

# ===== Q12 (A) 外傷氣胸 — 立即胸管 =====
add(12,
    summary="25 歲外傷史 + 呼吸困難 + CXR 顯示外傷性氣胸 = symptomatic traumatic pneumothorax，立即 tube thoracostomy 為標準處置；張力性氣胸需先 needle decompression 再 chest tube。",
    mechanism="Pneumothorax 胸膜腔氣體 → lung collapse → V/Q mismatch、hypoxia。Tension pneumothorax：one-way valve 機制持續氣體進入 → mediastinal shift → 阻擋 venous return → 心血管虛脫。",
    options={
        "A": "正確 (本題答案)。Symptomatic 或 traumatic pneumothorax 應放 28-32 Fr chest tube 4-5th ICS, anterior axillary line。",
        "B": "錯誤。觀察 + 肌肉鬆弛劑無治療效果，無法解決氣胸。",
        "C": "錯誤。VATS 為 elective treatment for persistent/recurrent，非急性處置。",
        "D": "錯誤。Symptomatic 外傷性氣胸不應等 CT；先處理再診斷影像。",
    },
    guidelines=[
        "ATLS 10/e Trauma Guidelines：Tension PTX → needle decompression (5th ICS midaxillary)；Traumatic PTX → tube thoracostomy。",
        "BTS 2010 Pleural Disease：小氣胸 8-14 Fr 足夠；外傷或 hemothorax 需 28-32 Fr。",
        "Trauma：always check pneumothorax before GA induction — 正壓可使 PTX 變 tension。",
    ],
    points=[
        "Tension PTX 為臨床診斷 — 不可等 CXR",
        "麻醉考量：N₂O 使 PTX 擴大 → 已知氣胸禁忌",
        "拔管後 monitor lung re-expansion",
    ],
    keyword="Pneumothorax, tube thoracostomy, ATLS",
    source="ATLS 10/e; BTS Pleural Disease Guidelines 2010",
)

# ===== Q13 (B) 細菌性膽管炎 =====
add(13,
    summary="RUQ pain + jaundice + fever (Charcot's triad) + leukocytosis + 黃疸 = 急性化膿性膽管炎 (acute cholangitis)。需立即抗生素 + 膽道引流 (ERCP)。",
    mechanism="膽道阻塞 (stone、tumor、stricture) → bile stasis → bacterial colonization (E. coli、Klebsiella、Enterococcus) → 細菌入血。膽管壓力 > 25 cmH₂O 引起 cholangiovenous reflux → bacteremia → sepsis。",
    options={
        "A": "錯誤。病毒性肝炎主要 AST/ALT 明顯上升 (>1000)，本題 AST/ALT 僅輕微升高。",
        "B": "正確 (本題答案)。Charcot's triad (pain + fever + jaundice) + bili 高 + 中度 transaminitis = 細菌性膽管炎。",
        "C": "錯誤。肝硬化急性發作通常 chronic 病史，無此急性 cholangitic 特徵。",
        "D": "錯誤。Acute pancreatitis 主要 epigastric pain + lipase↑↑，本題 lipase 未提及但表現以膽管炎為主。",
    },
    guidelines=[
        "Tokyo Guidelines 2018 (TG18)：急性膽管炎診斷與分級。",
        "Severe cholangitis (Grade III)：immediate biliary drainage (preferably ERCP within 24h)。",
        "Empiric antibiotics：piperacillin-tazobactam、ceftriaxone + metronidazole、carbapenem (severe)。",
    ],
    points=[
        "Reynolds' pentad = Charcot's + hypotension + AMS = severe suppurative cholangitis (mortality 50%+)",
        "ERCP > PTC > surgery in most cases",
        "麻醉：sepsis 復甦、可能 coagulopathy、術後加護",
    ],
    keyword="Acute cholangitis, Charcot's triad, Tokyo Guidelines",
    source="Tokyo Guidelines 2018 (TG18)",
)

# ===== Q14 (A) HHS =====
add(14,
    summary="38 歲 T2DM + AMS + 血糖 980 + 高 osmolality 350 + ketone 0.1 + pH 7.36 + HCO₃ 22 = 高滲透性高血糖狀態 (HHS)，非 DKA (DKA pH < 7.3、HCO₃ < 18、ketone↑)。",
    mechanism="T2DM 殘餘 insulin 足以抑制 ketogenesis 但不足以降血糖 → 漸進性極高血糖 + 滲透性利尿 → 嚴重脫水 + hyperosmolality → 腦功能異常。比 DKA 進展慢 (days-weeks)、脫水嚴重 (~9 L deficit)。",
    options={
        "A": "正確 (本題答案)。HHS criteria: 血糖 > 600、osmolality > 320、pH > 7.3、HCO₃ > 18、minimal ketone、AMS。",
        "B": "錯誤。DKA: 血糖通常 > 250、pH < 7.3、HCO₃ < 18、ketone > 3、Kussmaul respiration。",
        "C": "錯誤。Lactic acidosis 主要 lactate 顯著上升、本題 lactate 1.9 接近正常。",
        "D": "錯誤。本題 pH 7.36 接近正常，無顯著 acidosis。",
    },
    guidelines=[
        "ADA Management of DKA and HHS：(1) Aggressive fluid resuscitation (1-1.5 L NS in first hour)；(2) Insulin infusion 0.1 U/kg/h after K > 3.3；(3) K replacement early；(4) 血糖目標 250-300 first 24h 防 cerebral edema。",
        "Trigger 找：infection (most common)、MI、stroke、pancreatitis、停 insulin。",
    ],
    points=[
        "HHS 麻醉：rehydration first、K correction、慎防 hypoglycemia 與 cerebral edema",
        "Fluid resuscitation 速度低於 DKA (脫水嚴重但 osmolality 急降危險)",
        "Mortality 10-20%；老年合併症多",
    ],
    keyword="HHS, hyperosmolar hyperglycemic state, DKA",
    source="ADA Standards of Medical Care in Diabetes",
)

# ===== Q15 (C) BNP =====
add(15,
    summary="BNP/NT-proBNP 為心衰竭嚴重度、預後、治療反應的主要血清指標。心室因 stretch、wall stress 分泌；NT-proBNP 半衰期較長適合門診監測。",
    mechanism="BNP 主要作用：natriuresis、diuresis、vasodilation；對抗 RAAS 與 sympathetic activation。BNP > 100、NT-proBNP > 300 提示 HF；< 35 / < 125 可排除 HF (high NPV)。",
    options={
        "A": "錯誤。Troponin T 為 myocardial injury (AMI、myocarditis)，雖 HF 可輕度升高，但非 severity 指標。",
        "B": "錯誤。Myoglobin 為早期 muscle injury marker，已較少使用。",
        "C": "正確 (本題答案)。BNP/NT-proBNP 為 HF severity & prognosis 主要 marker。",
        "D": "錯誤。Lactate 反映 tissue hypoxia/perfusion (shock、sepsis)，非 HF 直接 marker。",
    },
    guidelines=[
        "ACC/AHA HF Guidelines 2017 Update：BNP/NT-proBNP 用於診斷、severity、prognosis、guidance of therapy。",
        "Acute HF in ED：BNP > 500、NT-proBNP > 1000 (<50y)、> 1800 (>50y) 高度支持 HF。",
        "BNP 在 obesity (↓)、renal failure (↑) 須調整解讀。",
    ],
    points=[
        "PARADIGM-HF：ARNI (Entresto) 降低 HFrEF mortality",
        "NT-proBNP > 1000 加重住院預後差",
        "AHF 早期分流：BNP-guided 仍受爭議",
    ],
    keyword="BNP, NT-proBNP, heart failure",
    source="ACC/AHA HF Guidelines; Stoelting's 7/e Ch. Cardiovascular",
)

# ===== Q16 (B) 氣壓性傷害 (Barotrauma) =====
add(16,
    summary="機械通氣 + 呼吸器警示 + 「頸部皮下氣泡 (crepitus)」 + 「右側呼吸音變弱」 + SpO₂↓ = barotrauma 引起 pneumomediastinum/pneumothorax，需通知醫師評估胸管。",
    mechanism="Mechanical ventilation barotrauma：high pressure → alveolar rupture → air dissect along bronchovascular sheath → mediastinum → cervical SQ → 皮下氣泡。可進展為 tension pneumothorax → 心血管虛脫。",
    options={
        "A": "錯誤。VAP 通常 fever + leukocytosis + 新增浸潤，非急性 SQ emphysema。",
        "B": "正確 (本題答案)。Barotrauma 引起 pneumothorax/pneumomediastinum，需 CXR/CT + chest tube。",
        "C": "錯誤。Ventilator 脫落不會引起 SQ emphysema (反而 SpO₂ 急降 + ETCO₂ 為 0)。",
        "D": "錯誤。Dyssynchrony 主要 peak pressure 變動，無 SQ emphysema。",
    },
    guidelines=[
        "ARDS Network 6 mL/kg lung-protective ventilation 減少 barotrauma。",
        "處置：confirm with CXR/CT、reduce PEEP/TV、chest tube if pneumothorax、考慮 needle aspiration of pneumomediastinum if tension。",
    ],
    points=[
        "Crackling on palpation = SQ emphysema (Hamman's sign)",
        "Tension pneumomediastinum 為急症 — 處置同 tension pneumothorax",
        "ARDS 低 TV (4-6 mL/kg) + plateau pressure ≤ 30 cmH₂O",
    ],
    keyword="Barotrauma, pneumomediastinum, subcutaneous emphysema",
    source="ARDSnet protocol; Miller's 8/e Critical Care",
)

# ===== Q17 (C) Sepsis 30 mL/kg fluid =====
add(17,
    summary="65 歲男性 UTI + 寒顫 + 高燒 + BP 85/50 + 心跳快、尿少 + 乳酸 4.2 = septic shock。Surviving Sepsis 1-hour bundle 優先：立刻 30 mL/kg 晶體輸液 + broad-spectrum antibiotic。",
    mechanism="Sepsis: cytokine storm → endothelial dysfunction → vasodilation + capillary leak → distributive shock。Lactate > 4 提示 tissue hypoperfusion。Early aggressive fluid + antibiotic 改善 mortality。",
    options={
        "A": "錯誤。Hydronephrosis 雖可能存在，但休克復甦優先；US 可延後。",
        "B": "錯誤。退燒藥不能解決根本問題，且休克病人不應 routine 用。",
        "C": "正確 (本題答案)。30 mL/kg crystalloid 為 1-hour bundle 標準。",
        "D": "錯誤。等待醫師延誤 vasopressor 啟動；NP 應即時 fluid + 通報。",
    },
    guidelines=[
        "Surviving Sepsis Campaign 2021 1-hour bundle: (1) Lactate；(2) Blood culture；(3) Broad-spectrum antibiotic；(4) Crystalloid 30 mL/kg；(5) Vasopressor for MAP ≥ 65。",
        "Lactate clearance > 10%/h 預後改善指標。",
        "Norepinephrine first-line vasopressor。",
    ],
    points=[
        "Procalcitonin 較 CRP specific for bacterial infection",
        "Early antibiotic + source control 為 sepsis 治療關鍵",
        "Hour-1 bundle adherence 改善 outcome",
    ],
    keyword="Sepsis, sepsis bundle, fluid resuscitation",
    source="Surviving Sepsis Campaign 2021",
)

# ===== Q18 (B) 心因性休克 =====
add(18,
    summary="Cardiogenic shock 主要機轉為「心肌收縮力不足」(failure of pump function) 導致 CO 下降。Hypovolemic 為血容不足；obstructive 為機械阻塞；distributive 為 vasodilation。",
    mechanism="Cardiogenic shock：心肌喪失 contractility (AMI、cardiomyopathy、myocarditis、severe valve disease) → forward flow 減少 → 系統灌流不足 + 肺鬱血。CO↓、SVR↑、PCWP↑。",
    options={
        "A": "錯誤。Hypovolemic 為「血容不足」非「血管阻塞」。",
        "B": "正確 (本題答案)。Cardiogenic = 心肌收縮力不足 → CO↓。",
        "C": "錯誤。Obstructive (PE、tamponade、tension PTX) 為機械阻塞，非感染。",
        "D": "錯誤。Distributive 特徵為「血管擴張、SVR↓」非 preload↑。",
    },
    guidelines=[
        "ACC/AHA Cardiogenic Shock Guidelines 2017。",
        "Treatment：inotrope (dobutamine、milrinone)、vasopressor、IABP、ECMO、urgent PCI for AMI。",
        "SCAI Cardiogenic Shock Classification (A-E) 預後分級。",
    ],
    points=[
        "Mixed shock 常見 (e.g. cardiogenic + distributive after MI sepsis)",
        "PA catheter / TEE / POCUS 可區分 shock 類型",
        "Treatment 依 type：fluid for hypovolemic、inotrope for cardiogenic、relieve obstruction、vasopressor for distributive",
    ],
    keyword="Cardiogenic shock, pump failure, hemodynamic profile",
    source="Miller's Anesthesia 8/e Critical Care; ACC/AHA 2017",
)

# ===== Q19 (C) Norepinephrine =====
add(19,
    summary="Septic shock 第一線 vasopressor 為 Norepinephrine (α₁ + β₁)；維持 MAP ≥ 65。不足時加 Vasopressin、Epinephrine、Hydrocortisone。",
    mechanism="Norepinephrine 結合 α₁ 引起 vasoconstriction (升 SVR)、β₁ 輕度 inotropic effect (保 CO)；較少 tachycardia/arrhythmia 風險於 dopamine。",
    options={
        "A": "錯誤。Epinephrine 用於 anaphylaxis、cardiac arrest，非 septic shock 首選 (tachycardia、 lactate↑)。",
        "B": "錯誤。Dopamine 因 tachyarrhythmia、mortality 升而退居二線 (SOAP II trial)。",
        "C": "正確 (本題答案)。Norepinephrine first-line for septic shock。",
        "D": "錯誤。Vasopressin 為 second-line catecholamine-sparing；refractory shock 加入 0.03 U/min。",
    },
    guidelines=[
        "Surviving Sepsis 2021：NE first-line；加 Vasopressin 0.03 U/min；refractory 加 Epi、Hydrocortisone 200 mg/day。",
        "SOAP II Trial 2010：NE vs Dopamine — NE 死亡率較低、arrhythmia 少。",
        "VANISH Trial：Vasopressin 早加未改善 mortality，但減少 catecholamine。",
    ],
    points=[
        "MAP target ≥ 65 mmHg；個體化於高血壓老人可考慮 80-85",
        "Central line preferred、peripheral 短期 (< 24h、< 0.1 µg/kg/min) 可接受",
        "Hydrocortisone 用於 refractory shock (vasopressor 仍需 > 0.25 µg/kg/min)",
    ],
    keyword="Norepinephrine, septic shock, vasopressor",
    source="Surviving Sepsis Campaign 2021",
)

# ===== Q20 (A) ROSC 不適當 — Lidocaine 預防性 =====
add(20,
    summary="Post-ROSC 「不應 routine 給 lidocaine」防再次心律不整。AHA 2020 已移除 routine antiarrhythmic prophylaxis 建議；個別化 decision-making。",
    mechanism="Post-ROSC phase 重點：oxygenation、ventilation、 hemodynamics、TTM、coronary angiography (若 STEMI)。Routine antiarrhythmic 增加副作用 (proarrhythmia、 sedation)、無改善 outcome 證據。",
    options={
        "A": "錯誤 (本題不適當)。Routine lidocaine 已不建議；僅在 VT/VF recurrence 才考慮。",
        "B": "正確。PaCO₂ 35-45 mmHg (normocapnia) 避免 hyperventilation (CBF↓)。",
        "C": "正確。STEMI 或 high-suspicion STEMI 應 emergent cath lab。",
        "D": "正確。MAP ≥ 65 mmHg 維持灌流；個別化可考慮 80-90。",
    },
    guidelines=[
        "AHA 2020 ACLS Guidelines: Post-cardiac arrest care。",
        "TTM Trial 2013、TTM2 2021：32-36°C × 24h 為 standard。",
        "Targeted MAP ≥ 65；避免 hyperoxia (SpO₂ > 98%)；血糖 < 180 mg/dL。",
    ],
    points=[
        "Neurologic prognosis 至少 72h 後評估 (TTM 延長至 5 天)",
        "Source identification 對 prevention recurrence 重要",
        "Family communication 與 organ donation evaluation 早討論",
    ],
    keyword="Post-ROSC, lidocaine, AHA 2020",
    source="AHA 2020 ACLS Guidelines; ILCOR Consensus",
)

# ===== Q21 (C) AMI 給 nitroglycerin 不適當 (低血壓) =====
add(21,
    summary="病人 BP 90/60 + HR 52 + 胸悶盜汗 = ACS 合併 low BP/bradycardia (suggest inferior MI ± RV infarct)。「不應給 nitroglycerin」因會進一步降 BP、加重 RV infarct。",
    mechanism="Inferior MI 常合併 RV infarct (RCA territory)；RV 依賴 preload，nitroglycerin 降低 preload → severe hypotension。應 fluid bolus 維持 preload + reperfusion (PCI)。",
    options={
        "A": "正確。生命徵象監測 + IV access 為基本步驟。",
        "B": "正確。低流量 O₂ 若 SpO₂ < 90% (避免 hyperoxia)。",
        "C": "錯誤 (本題不適當)。Hypotension + bradycardia + inferior MI ± RV infarct → nitroglycerin 為禁忌。",
        "D": "正確。Right-sided EKG (V4R) 評估 RV infarct (ST elevation V4R)。",
    },
    guidelines=[
        "ACC/AHA STEMI/NSTEMI Guidelines：MONA-B 已過時；個別化 antiplatelet + anticoagulation + reperfusion。",
        "Door-to-balloon < 90 min for STEMI。",
        "RV infarct: fluid bolus、avoid nitrate/diuretic、 maintain preload。",
    ],
    points=[
        "RV infarct: V₄R lead ST elevation; treat with fluid",
        "Bradycardia in inferior MI: atropine, may need pacing",
        "Cardiogenic shock complicating AMI: IABP、ECMO、urgent PCI",
    ],
    keyword="Acute coronary syndrome, RV infarct, nitroglycerin contraindication",
    source="ACC/AHA NSTEMI/STEMI Guidelines",
)

# ===== Q22 (B) CBF 慢性高血壓 autoregulation =====
add(22,
    summary="慢性高血壓病人腦血流自我調節曲線「右移」— 上下限都「上升」。Normal autoregulation MAP 50-150；慢性高血壓 70-170。",
    mechanism="Chronic HTN 引起 cerebral vasculature remodeling (媒體層 hypertrophy) → autoregulation curve shifts right。低 BP 時更早失代償 (cerebral hypoperfusion)。慢性高血壓病人術中 MAP 不應降太低 (建議維持 baseline 80%)。",
    options={
        "A": "錯誤。低體溫「降低」CMRO₂ 與 CBF (flow-metabolism coupling)。",
        "B": "正確 (本題答案)。慢性高血壓 autoregulation 上下限均「上升」(right shift)。",
        "C": "錯誤。Normal CPP 50-70 mmHg，非 25-50。",
        "D": "錯誤。PaCO₂ 升高 → CBF「增加」(每 mmHg ↑ 約 4%)，非減少。",
    },
    guidelines=[
        "Brain Trauma Foundation 4/e：CPP 60-70 mmHg target。",
        "Cerebral oximetry (NIRS) 監測 cerebral oxygenation in vulnerable patients。",
        "Maintain normocapnia (35-40) 為一般目標。",
    ],
    points=[
        "Hyperventilation lowers ICP 短期；不應長期",
        "Inhaled anesthetics > 1 MAC 引起 vasodilation、ICP↑",
        "Ketamine 影響 CBF 爭議性、但現代研究較中性",
    ],
    keyword="Cerebral blood flow, autoregulation, chronic hypertension",
    source="Miller's Anesthesia 8/e Ch. 70 Neurosurgical Anesthesia",
)

# ===== Q23 (C) ICP↑ → CPP↓ =====
add(23,
    summary="CPP = MAP − ICP。ICP 升高 → CPP 「下降」 → 腦組織 hypoperfusion → secondary brain injury。",
    mechanism="Monroe-Kellie doctrine：cranial volume 固定 (腦 + 血 + CSF)。任一成分增加 → 其他減少代償；超過 reserve → ICP 急升 (exponential)。CPP 下降致 cerebral ischemia。",
    options={
        "A": "錯誤。ICP↑ 會「降低」CBF (除非 autoregulation 強烈代償，但通常 fail)。",
        "B": "錯誤。ICP↑ 不會增加 CBF。",
        "C": "正確 (本題答案)。CPP = MAP − ICP；ICP↑ → CPP↓。",
        "D": "錯誤。ICP↑ → CPP↓ 非增加。",
    },
    guidelines=[
        "Brain Trauma Foundation 4/e：ICP treatment threshold > 22 mmHg；CPP target 60-70。",
        "Mannitol 0.25-1 g/kg、Hypertonic saline 3% 250 mL 為 osmotic therapy。",
        "Head elevation 30°、avoid jugular compression、normocapnia 35-40。",
    ],
    points=[
        "Tier 1 ICP treatment：head elevation、sedation、analgesia、CSF drainage",
        "Tier 2：mannitol、hypertonic saline、hyperventilation (short)",
        "Tier 3：barbiturate coma、decompressive craniectomy",
    ],
    keyword="Intracranial pressure, cerebral perfusion pressure, Monroe-Kellie",
    source="Brain Trauma Foundation 4/e (2016)",
)

# ===== Q24 (B) SSEP/MEP — 靜脈麻醉劑影響小 =====
add(24,
    summary="一般臨床劑量下，靜脈麻醉劑 (propofol、 etomidate、 ketamine) 對 SSEP/MEP「影響較小」；揮發性麻醉劑 dose-dependent 抑制 amplitude。TIVA 為 MEP 監測首選。",
    mechanism="Volatile anesthetics 抑制 synaptic transmission；對 cortical SSEP 影響大、subcortical 較小；MEP 較 SSEP 敏感於 anesthetic suppression。NMBA 完全阻斷 MEP，須避免。",
    options={
        "A": "錯誤。Ketamine 「增加」short/medium latency 電位波幅；不是 long-latency。",
        "B": "正確 (本題答案)。TIVA (propofol + remifentanil) 對 SSEP/MEP 影響較小，為 MEP 監測首選。",
        "C": "錯誤。高劑量靜脈藥物會「抑制」amplitude、「延長」latency。",
        "D": "錯誤。揮發性麻醉劑「顯著抑制」MEP；> 0.5 MAC 即影響。",
    },
    guidelines=[
        "ASNM (American Society of Neurophysiological Monitoring)：MEPs 監測首選 TIVA。",
        "Etomidate、ketamine 可 enhance SSEP (paradoxical)。",
        "NMBA：TOF 1-2/4 可接受 SSEP；MEP 避免 NMBA。",
    ],
    points=[
        "Visual evoked potential (VEP) 對麻醉敏感、罕用於監測",
        "Brainstem auditory evoked potential (BAEP) 較 robust to anesthesia",
        "Significant change: 50% amplitude ↓ 或 10% latency ↑",
    ],
    keyword="SSEPs, MEPs, TIVA, evoked potentials",
    source="Miller's Anesthesia 8/e Ch. 50 Monitoring of the CNS",
)

# ===== Q25 (AB 多答) 麻醉藥對大腦 =====
add(25,
    summary="Etomidate 與 Propofol 兩者皆降低腦代謝率與顱內壓 / 腦血流量，均為 neuroanesthesia 適用藥物。Ketamine 「增加」CBF (爭議性近年再評估)；Isoflurane > 1 MAC 引起 vasodilation。",
    mechanism="Etomidate、 propofol、 barbiturate 透過 GABA-A receptor 增強 → CMRO₂ ↓ → flow-metabolism coupling → CBF↓ → 腦血容量↓ → ICP↓。Ketamine 主要 NMDA 阻斷 + sympathomimetic → 傳統認為 CBF↑、ICP↑ (近年研究爭議)。",
    options={
        "A": "正確 (本題答案之一)。Etomidate 降 CMRO₂ + CBF + ICP；維持血流動力學穩定。",
        "B": "正確 (本題答案之一)。Propofol 降 CMRO₂ + CBF + ICP；neuroanesthesia 首選。",
        "C": "錯誤。Ketamine 傳統認為「增加」CBF/ICP；不可單獨用於 ICP↑ 病人。",
        "D": "錯誤。Isoflurane < 1 MAC 維持 CBF；> 1 MAC 引起 vasodilation 增加 CBF (與 CMRO₂↓ 不平衡)。",
    },
    guidelines=[
        "SNACC (Society for Neuroscience in Anesthesiology and Critical Care)：TIVA propofol-based 為 ICP↑ 病人 preferred。",
        "Burst suppression for refractory ICP 或 seizure。",
        "N₂O 在 air-containing structure (pneumocephalus、air embolism) 禁忌。",
    ],
    points=[
        "Sevoflurane < 1 MAC 對腦 hemodynamics 影響小、可接受",
        "Ketamine 重新評價：可能 neuroprotective、不嚴格禁忌於 ICP",
        "Dexmedetomidine 降 CBF + CMRO₂ proportionally；保留腦血流調節",
    ],
    keyword="Cerebral metabolism, CMRO₂, propofol, etomidate, neuroprotection",
    source="Miller's Anesthesia 8/e Ch. 70",
)

# ===== Q26 (C) 骨水泥 — 心律不整 =====
add(26,
    summary="Bone Cement Implantation Syndrome (BCIS) 可引起「心律不整、心傳導阻滯、竇性停搏」。Hypotension + hypoxia + CV collapse 為 hallmark。常見於髖關節手術，非肩關節。",
    mechanism="PMMA (Polymethylmethacrylate) 放熱反應 + 機械壓迫骨髓內壓上升 → fat、marrow content、cement monomer 進入靜脈循環 → 肺循環 → pulmonary hypertension、RV failure、 anaphylactoid 反應、心律不整。",
    options={
        "A": "錯誤。BCIS 引起「低血壓、CO 下降」非高血壓增加。",
        "B": "錯誤。BCIS 引起 vasodilation 使「SVR 下降」。",
        "C": "正確 (本題答案)。可引起心律不整 (bradycardia、heart block、sinus arrest)。",
        "D": "錯誤。BCIS 主要見於「髖關節 (hip arthroplasty)」、膝關節也有，肩關節較少。",
    },
    guidelines=[
        "AAGBI Safety Guideline 2015：BCIS classification (Grade 1 mild、2 moderate、3 severe)。",
        "預防：充分 hydration、osmotically clean medullary canal、低壓 cement、保 FiO₂↑、euvolemia、avoid N₂O。",
        "處置：100% O₂、fluid、vasopressor (norepinephrine)、CPR 若 arrest。",
    ],
    points=[
        "高風險：老年女性、髖部骨折、心衰、肺病、肺高壓",
        "Cementless prosthesis 替代以避免 BCIS",
        "Vigilance during cementation + early intervention",
    ],
    keyword="Bone cement implantation syndrome, PMMA, hip arthroplasty",
    source="AAGBI BCIS Safety Guideline 2015; Miller's 8/e",
)

# ===== Q27 (C) Tourniquet release 低血壓 — 代謝性酸中毒 =====
add(27,
    summary="Tourniquet 釋放後 hypotension 主因為「缺血末端產物 (lactate、 K⁺、H⁺) 釋出引發代謝性酸中毒 + 心律不整 + vasodilation」。",
    mechanism="Limb ischemic period 期間 anaerobic metabolism 累積 lactate、K⁺、H⁺、ROS。Release → systemic washout → metabolic acidosis + hyperkalemia + vasodilation + 心肌抑制 → BP↓。ETCO₂ 急升。",
    options={
        "A": "錯誤。Tourniquet 釋放後反而 sympathetic tone 「下降」(reperfusion 反應)。",
        "B": "錯誤。麻醉藥已在循環中，非 release 後才吸收。",
        "C": "正確 (本題答案)。Lactate、K⁺、H⁺ 釋出引發 metabolic acidosis + arrhythmia + hypotension。",
        "D": "錯誤。Tourniquet release 常引起 reflex tachycardia (非 bradycardia)。",
    },
    guidelines=[
        "AAOS Tourniquet Guidelines：< 2 小時、上肢 SBP+50、下肢 SBP+100 mmHg。",
        "釋放前：increase FiO₂、bolus fluid、monitor ETCO₂、K、acid-base。",
        "嚴重 hyperkalemia 或 acidosis 可能、考慮慢釋放或 staged release。",
    ],
    points=[
        "ETCO₂ 急升於 tourniquet 釋放 — 經典 capnogram changes",
        "Pre-existing hypovolemia/acidosis 加重 release-induced hypotension",
        "Tourniquet pain：充氣 45-60 min 後深層 aching、tachycardia",
    ],
    keyword="Tourniquet release, reperfusion, hyperkalemia, lactic acidosis",
    source="AAOS Tourniquet Use Guidelines",
)

# ===== Q28 (D) Dexmedetomidine — α2 受體 =====
add(28,
    summary="Dexmedetomidine 為高選擇性 α₂-adrenergic agonist，可用於抗焦慮、鎮靜與止痛。半衰期約 2 小時 (非 6 小時)；單獨不能達強效鎮痛；不引起顯著呼吸抑制，適合 awake fiberoptic intubation。",
    mechanism="中樞 α₂ receptor in locus coeruleus → 降低 noradrenaline release → sedation (mimics natural sleep)、analgesia。周邊 α₂ → vasoconstriction → initial hypertension；長期主要 sympatholytic → bradycardia、hypotension。Elimination half-life ~2-3h。",
    options={
        "A": "錯誤。Dexmedetomidine 「不引起顯著呼吸抑制」，反而適合 awake intubation。",
        "B": "錯誤。Elimination half-life 約 2-3 小時，「非超過 6 小時」。",
        "C": "錯誤。Dexmedetomidine 鎮痛效果「中等」，不能完全取代 opioid。",
        "D": "正確 (本題答案)。α₂-adrenergic agonist；可用於抗焦慮、鎮靜、止痛。",
    },
    guidelines=[
        "FDA approved for ICU sedation < 24h、procedural sedation。",
        "Loading dose 0.5-1 µg/kg over 10 min；maintenance 0.2-0.7 µg/kg/h。",
        "DEX 重新評估 (PRODEX、SPICE III)：與 propofol/midazolam 比較。",
    ],
    points=[
        "副作用：bradycardia (atropine response good)、hypotension、dry mouth",
        "對 awake fiberoptic intubation 有用 — 維持自主呼吸 + 配合",
        "可降低 emergence agitation 兒童",
    ],
    keyword="Dexmedetomidine, α2-agonist, ICU sedation",
    source="FDA Precedex label; Miller's 8/e Ch. 30",
)

# ===== Q29 (B) POVL — ION + 青光眼 =====
add(29,
    summary="圍術期視力喪失 (POVL) 主因：Ischemic Optic Neuropathy (ION)，青光眼為共存風險因子。並非眼睛直接創傷或 hypotension 策略。",
    mechanism="ION：optic nerve 缺血；prone + 長時間 + 低 BP + 血液稀釋 + venous congestion (head down) → 局部 perfusion 不足。Glaucoma 預存眼壓高、optic nerve 已 vulnerable。",
    options={
        "A": "錯誤。POVL 多由 ION (非直接創傷)；direct trauma 較少見。",
        "B": "正確 (本題答案)。ION + glaucoma 為已知風險因子。",
        "C": "錯誤。Head positioning 與 IOP 高度相關 (prone IOP 可升至 40+)。",
        "D": "錯誤。「刻意 hypotension」策略「增加」POVL 風險，非降低。",
    },
    guidelines=[
        "ASA Practice Advisory for POVL 2019：spine surgery > 6h、estimated blood loss > 1L 為 highest risk。",
        "預防：避免 head-down、保持 head neutral、avoid prolonged hypotension、monitor Hct、Mayfield/foam headrest 適當。",
        "ASA POVL Registry 持續收集 data。",
    ],
    points=[
        "Vision loss 通常 first noticed in PACU、prognosis poor",
        "Cardiac surgery (CPB) 為次常見族群 (CRAO、cortical blindness)",
        "Mid-procedure 檢查眼瞼、避免外壓",
    ],
    keyword="POVL, ischemic optic neuropathy, glaucoma, prone position",
    source="ASA Practice Advisory for POVL 2019",
)

# ===== Q30 (D) TKA 多模式止痛 — 降低 opioid =====
add(30,
    summary="多模式止痛核心目標為「降低 opioid 使用量」。Acetaminophen + ketorolac + 單次 epidural opioid + femoral block 結合不同機轉，協同降痛 + opioid-sparing。",
    mechanism="不同藥物作用於 pain pathway 不同階段：(1) Peripheral (NSAIDs、LA)；(2) Spinal (epidural opioid、α2-agonist)；(3) Supraspinal (acetaminophen、 opioid)。協同降低個別藥物副作用。",
    options={
        "A": "錯誤。Acetaminophen 與 epidural opioid「協同」止痛，無拮抗。",
        "B": "錯誤。Ketorolac 為「周邊」NSAID (COX inhibitor)，非中樞；與 acetaminophen 機轉「不同」。",
        "C": "錯誤。Femoral nerve block「會影響 quadriceps function」、增加 fall risk；近年改用 adductor canal block。",
        "D": "正確 (本題答案)。多模式止痛核心 = 降低 opioid 用量 + 副作用。",
    },
    guidelines=[
        "ERAS Knee Replacement Pathway：multimodal opioid-sparing 為核心。",
        "PROSPECT TKA：multimodal + LIA + adductor canal block。",
        "ASRA：femoral block 可能延緩 ambulation；adductor canal block 為現代替代。",
    ],
    points=[
        "Adductor canal block 保留 quadriceps function，方便 early ambulation",
        "PENG (pericapsular nerve group) block 為新興 hip option",
        "Continuous catheter 延長 analgesia 至 48-72h",
    ],
    keyword="Multimodal analgesia, TKA, ERAS, opioid-sparing",
    source="PROSPECT TKA Guidelines; ERAS Society",
)

# ===== Q31 (A) Propofol — 大豆/花生過敏 =====
add(31,
    summary="Propofol 配方含「大豆油 (soybean oil)、egg lecithin」。對大豆或花生 (花生與大豆同為豆科) 嚴重過敏者為「相對禁忌」(罕見 anaphylaxis 風險)。",
    mechanism="Propofol 配方 = 1% propofol + 10% soybean oil + 2.25% glycerol + 1.2% egg lecithin。Lecithin 為 phospholipid (非 protein) 引起 allergy 罕見；soybean oil 蛋白可能 trigger 過敏。",
    options={
        "A": "正確 (本題答案)。對大豆/花生嚴重過敏者，propofol 相對禁忌。",
        "B": "錯誤。長期 benzo 病人 propofol 可用 (劑量可能需調整)。",
        "C": "錯誤。BMI 40 病人胃鏡常用 propofol (適當劑量 + ramped position)。",
        "D": "錯誤。CKD stage 3 propofol 可用，肝代謝為主。",
    },
    guidelines=[
        "ASA: egg allergy not absolute contraindication; cautious with severe anaphylaxis history。",
        "PRIS：dose > 4 mg/kg/h × > 48h；FDA black box for pediatric ICU。",
        "替代：Etomidate、Ketamine、Thiopental、Midazolam。",
    ],
    points=[
        "Egg-anaphylaxis 病人約 < 1% 對 propofol 反應，新證據認為大多安全",
        "Soy allergy 同樣低風險，但嚴重者建議替代",
        "PRIS 三聯徵：metabolic acidosis、rhabdomyolysis、cardiac failure",
    ],
    keyword="Propofol, soy allergy, egg lecithin",
    source="FDA Propofol label; Stoelting's Pharmacology 5/e",
)

# ===== Q32 (D) 肝癌大出血 — PCC + cryo =====
add(32,
    summary="肝癌 + coagulopathy (factor synthesis ↓) + 大量出血 → 優先補充「凝血因子 (PCC) + fibrinogen (cryoprecipitate)」。PCC 提供 vitamin K-dependent factor (II、VII、IX、X)，快速矯正 INR；cryo 補 fibrinogen。",
    mechanism="肝硬化/肝癌：vit K-dependent factor 合成下降、fibrinogen normal-low、thrombocytopenia。大量出血 → dilutional coagulopathy + consumption。PCC 較 FFP 快速 (small volume、no thawing) 矯正凝血。",
    options={
        "A": "錯誤。Cryo + DDAVP 缺乏 vit K-dependent factor 補充。",
        "B": "錯誤。Fibrinogen 補充必要但缺 vit K factor (II、VII、IX、X)。",
        "C": "錯誤。FFP 雖含凝血因子，但量大、需 thaw、起效慢。",
        "D": "正確 (本題答案)。PCC (vit K factor) + cryo (fibrinogen) 快速、有效矯正肝病 coagulopathy。",
    },
    guidelines=[
        "ASA Practice Guidelines for Perioperative Blood Management 2015。",
        "Goal-directed transfusion：TEG/ROTEM 指引比例。",
        "Massive transfusion protocol 1:1:1 if no point-of-care available。",
        "Tranexamic acid 1 g IV 早期 (< 3h) 降低死亡率 (CRASH-2)。",
    ],
    points=[
        "PCC 4-factor 含 II、VII、IX、X (Kcentra、Beriplex)",
        "Cryoprecipitate 提供集中 fibrinogen (10-15 mL/unit ≈ 4g/L)",
        "肝病 INR 不直接對應 bleeding risk (rebalanced hemostasis)",
    ],
    keyword="Massive transfusion, PCC, cryoprecipitate, hepatic coagulopathy",
    source="ASA Practice Guidelines for Perioperative Blood Management; ESA 2017",
)

# ===== Q33 (A) 腹腔鏡 — TOF 1, rocuronium 10mg =====
add(33,
    summary="腹腔鏡置 trocar 後麻醉照護：BP 180/103 + HR 106 + ETCO₂ 45 提示 sympathetic stimulation + light anesthesia。「TOF 1 count」表示 NMBA 已開始恢復，應補 rocuronium 10 mg 維持深度肌肉鬆弛 (laparoscopy 必要)。",
    mechanism="腹腔鏡需要深度 NMBA 維持 abdominal wall 鬆弛、改善 surgical view、減少 IAP 需求。TOF count 1 表示已 75% receptor blockade，但臨床上不夠深；應 PTC ≥ 1 或 TOF 0/4 為 deep block。",
    options={
        "A": "正確 (本題答案)。TOF 1 count 提示需要 boost rocuronium 維持 deep block。",
        "B": "錯誤。PEEP 不應為 0；應維持 5-10 防 atelectasis。I:E 1:1 在阻塞性肺病不適用。",
        "C": "錯誤。BIS 40 為適當麻醉深度，不需大量 remifentanil bolus；5-10 µg/kg 過量。",
        "D": "錯誤。BIS 70 過淺 (awareness risk)，sevoflurane 反而應「增加」非降到 < 0.3 MAC。",
    },
    guidelines=[
        "EAES (European Association for Endoscopic Surgery) Guidelines：IAP ≤ 15 mmHg；低 IAP (8-10) 在敏感病人。",
        "Deep NMBA (PTC ≥ 1) 改善 surgical condition 並降低 IAP 需求。",
        "Ventilation：increase minute ventilation 30-50% maintain ETCO₂；avoid hyperventilation。",
    ],
    points=[
        "嚴重 CO₂ embolism 雖罕見但致命 — 突發 ETCO₂↓、CV collapse",
        "Severe Trendelenburg → ↑ICP、facial edema、ETT migration",
        "BIS 40-60 為適當 GA 深度",
    ],
    keyword="Laparoscopy, NMBA, TOF, deep block",
    source="Miller's Anesthesia 8/e Ch. 76 Laparoscopic Anesthesia",
)

# ===== Q34 (C) 透析病人 — imipramine 心律不整 =====
add(34,
    summary="長期透析病人服用 imipramine (tricyclic antidepressant, TCA) 會「提高心律不整風險」(TCA 阻斷 Na channel + 抗膽鹼，QT 延長)。",
    mechanism="TCA (imipramine、amitriptyline) 多重藥理作用：(1) Na channel block (quinidine-like → QT 延長、torsades)；(2) Anticholinergic；(3) α-blockade (orthostatic hypotension)；(4) 中樞 NE/serotonin uptake inhibition。ESRD 透析後濃度可能 fluctuate。",
    options={
        "A": "錯誤。透析病人應「警惕高鉀+高磷」，非「高鈣+低磷」。",
        "B": "錯誤。透析病人應警惕「高鉀」，非「高鈉+低鉀」。",
        "C": "正確 (本題答案)。Imipramine (TCA) 增加心律不整風險。",
        "D": "錯誤。Fluoxetine (SSRI) 與 atypical HUS 無關。",
    },
    guidelines=[
        "KDIGO Perioperative AKI Guidelines。",
        "麻醉藥選擇：avoid morphine、meperidine；prefer cisatracurium、fentanyl、remifentanil。",
        "AV fistula 保護：no IV、no BP cuff 該肢。",
    ],
    points=[
        "AVF stenosis/infection 為常見併發症，術前 thrill/bruit 評估",
        "Uremic platelet dysfunction：DDAVP 0.3 µg/kg 改善",
        "EPO + IV iron 改善 anemia 但 target Hb 10-11 (避免過高)",
    ],
    keyword="ESRD, TCA, imipramine, arrhythmia",
    source="Stoelting's Anesthesia and Co-existing Disease 7/e Ch. Renal",
)

# ===== Q35 (A) 甲狀腺手術 — RLN 監測 =====
add(35,
    summary="甲狀腺切除術中神經功能監測為「recurrent laryngeal nerve (RLN)」，因 RLN 走 tracheoesophageal groove 緊鄰甲狀腺，injury 引起 vocal cord paralysis。",
    mechanism="RLN 為迷走神經分支，主管除 cricothyroid muscle 外的喉部肌肉。Injury → vocal cord paralysis (unilateral hoarseness、bilateral 嚴重 stridor 需 tracheostomy)。IONM 透過 EMG ETT 接觸 vocal cords，刺激 RLN 偵測 EMG (loss = injury)。",
    options={
        "A": "正確 (本題答案)。RLN 為甲狀腺術中監測主要神經。",
        "B": "錯誤。Superior laryngeal nerve external branch 主管 cricothyroid，影響高音域，少數機構同時監測但非主要。",
        "C": "錯誤。IONM 與術後「聲帶水腫」無關 (聲帶水腫源於 intubation 創傷)。",
        "D": "錯誤。NMBA 劑量「顯著影響」EMG 訊號；應限制 NMBA (TOF ≥ 2)。",
    },
    guidelines=[
        "International Neural Monitoring Study Group (INMSG)：standardized IONM protocol。",
        "ETT 位置：cuff 在 vocal cords 中央；確認 EMG signal。",
        "Avoid deep NMBA — TOF count 2-3 可接受。",
    ],
    points=[
        "Bilateral RLN injury → 嚴重 stridor、需 tracheostomy",
        "Superior laryngeal nerve (external branch) injury → 高音域 weakening",
        "Hypocalcemia 為術後另一併發症 (parathyroid injury)",
    ],
    keyword="Recurrent laryngeal nerve, IONM, thyroidectomy",
    source="INMSG Guidelines; Hagberg Airway Management 4/e",
)

# ===== Q36 (B) Furosemide — 低鉀 =====
add(36,
    summary="Furosemide (loop diuretic) 作用於 thick ascending limb，抑制 Na/K/2Cl cotransporter → Na+K+Cl 大量排出尿 → 「低鉀血症 (hypokalemia)」 + metabolic alkalosis。",
    mechanism="Furosemide 增加 Na 至 distal tubule，刺激 K+ secretion (aldosterone-mediated)。長期使用 + 飲食 K 不足 → 顯著 hypokalemia → 心律不整、weakness。麻醉中需監測 K。",
    options={
        "A": "錯誤。Captopril (ACEi) 與 hypotension、 hyperkalemia 相關，「不是 hypothermia」。",
        "B": "正確 (本題答案)。Furosemide → urinary K loss → hypokalemia。",
        "C": "錯誤。Propranolol (β-blocker) 與 bradycardia、bronchospasm 相關，「不是寡尿」。",
        "D": "錯誤。Clopidogrel (antiplatelet) 與 bleeding 相關，「不是高鉀」。",
    },
    guidelines=[
        "ACC/AHA 2014 Perioperative Cardiovascular Guidelines。",
        "Continue β-blocker、statin、ASA (大多手術)。",
        "Hold ACEi/ARB morning of surgery (避免術中 hypotension)。",
    ],
    points=[
        "Loop diuretic 副作用：hypokalemia、alkalosis、 hypomagnesemia、 ototoxicity、 hyperuricemia",
        "麻醉中 K < 3.0 易誘發 ventricular arrhythmia",
        "K 補充：oral KCl preferred、 IV 慢速 (max 10 mEq/h peripheral)",
    ],
    keyword="Furosemide, loop diuretic, hypokalemia",
    source="Stoelting's Pharmacology 5/e",
)

# ===== Q37 (B) 達文西前列腺 — 頭低腳高 + 心臟回流 =====
add(37,
    summary="達文西前列腺術 steep Trendelenburg (30-45°) + pneumoperitoneum，「頭低腳高姿位」使下肢血液回流心臟「增加 cardiac filling」 → CVP↑、CO 改變。",
    mechanism="Steep Trendelenburg + IAP↑：(1) Venous return ↑ → CVP↑、preload↑；(2) Diaphragm 上推 → FRC↓、atelectasis、 ventilator pressure↑；(3) ICP↑；(4) Cephalad fluid shift → face/glottic edema；(5) IOP 上升。",
    options={
        "A": "錯誤。CO₂ 氣腹「不可燃」，不會引起電燒火花 (反而抑制)。",
        "B": "正確 (本題答案)。Trendelenburg + pneumoperitoneum 使 venous return 增加、心臟 filling↑。",
        "C": "錯誤。機械手臂不直接改變 ETT 內徑，但 ETT 可能 migration。",
        "D": "錯誤。氣腹「不會」降低 MAC；MAC 由 anesthetic concentration 決定。",
    },
    guidelines=[
        "ESA Robotic Surgery Anesthesia：穩定 patient 至 table、緩慢 positioning、protect arm/shoulder。",
        "Limit 機器手臂時間、間歇 level table reduce edema。",
        "Pre-op POVL risk assessment for glaucoma、prone-equivalent IOP changes。",
    ],
    points=[
        "Limited access 機器運作中 — 麻醉問題處置困難",
        "ETT migration、 cuff leak 常見 — 防止頻繁 endotracheal manipulation",
        "Eye protection essential — taping、 lubricant、 avoid pressure",
    ],
    keyword="Robotic surgery, Trendelenburg, prostatectomy",
    source="Miller's Anesthesia 8/e Ch. 77",
)

# ===== Q38 (A) 甲狀腺術前 CXR — 氣管偏右 =====
add(38,
    summary="甲狀腺術前 CXR 評估「tracheal deviation/compression」。本題 CXR 顯示「氣管位置向右偏移」，提示甲狀腺腫塊壓迫氣管，需準備 difficult airway。",
    mechanism="大型 goiter 或 substernal extension 壓迫 trachea → 軟化 (tracheomalacia)、舵狀/horseshoe deformity。Anesthesia induction NMBA 失去 muscle tone → 嚴重氣道塌陷。Tracheal deviation 為 difficult airway 警訊。",
    options={
        "A": "正確 (本題答案)。CXR 顯示 tracheal deviation to right，提示 goiter 壓迫。",
        "B": "錯誤。「沾黏」非 CXR 可直接顯示。",
        "C": "錯誤。「廔管 (fistula)」需要對比影像確認，非 routine CXR。",
        "D": "錯誤。「發育不全」為先天性異常，與本題 (甲狀腺術前評估) 不符。",
    },
    guidelines=[
        "DAS Difficult Airway Algorithm 2015：predict + plan。",
        "Awake fiberoptic intubation 為首選 (預期 difficult airway)。",
        "Surgical team standby for emergency tracheostomy。",
        "Avoid full NMBA until tube secured。",
    ],
    points=[
        "CT neck/chest 提供更精確 anatomy",
        "Substernal goiter 不易 surgical access、可能 sternotomy",
        "Tracheomalacia 術後可塌陷、leak test、prolonged intubation if needed",
    ],
    keyword="Goiter, tracheal deviation, difficult airway",
    source="Hagberg Airway Management 4/e",
)

# ===== Q39 (D) Naldebain 150mg 不適當 =====
add(39,
    summary="Naldebain® (nalbuphine, 鴉片類 agonist-antagonist) 150 mg 「靜脈注射」超出常用劑量 (一般單劑 10-20 mg IV)。劑量過高 + 與其他 opioid (remifentanil) 合併使用恐拮抗或增加副作用。",
    mechanism="Nalbuphine 為 mixed κ-agonist / μ-antagonist 鴉片類。常用劑量 10-20 mg IV (single dose)。150 mg 超出 ceiling effect 反而增加副作用 (sedation、dysphoria) 無進一步止痛。",
    options={
        "A": "正確 (是適當的 multimodal)。Remifentanil 0.1 µg/kg/min infusion 為常用麻醉。",
        "B": "正確 (是適當的)。Dynastat® (parecoxib) 40 mg IV 為 COX-2 selective inhibitor。",
        "C": "正確 (是適當的)。Acetaminophen 500 mg 為 multimodal 基礎。",
        "D": "錯誤 (本題不適當)。Naldebain 150 mg 為超量；常用單劑 10-20 mg IV。",
    },
    guidelines=[
        "ERAS Society Colorectal Pathway：multimodal + TAP block + thoracic epidural 選項。",
        "PROSPECT laparoscopic abdominal surgery：multimodal opioid-sparing。",
        "ASRA: TAP block 為 abdominal surgery 補充止痛。",
    ],
    points=[
        "Lidocaine infusion 1.5 mg/kg/h reduce opioid + 改善 ileus",
        "Ketamine 0.1-0.3 mg/kg bolus + low-dose infusion 對 opioid-tolerant 有效",
        "Dexmedetomidine 為 opioid-sparing 選項",
    ],
    keyword="Multimodal analgesia, nalbuphine, dosing",
    source="ERAS Society Guidelines; PROSPECT",
)

# ===== Q40 (B) Severe AS — 不應降 SVR =====
add(40,
    summary="Severe AS 麻醉照護應「維持高 SVR」(避免 hypotension 引起 subendocardial ischemia)。「降低 SVR」會降冠脈灌流壓、誘發 ischemia → 死亡。",
    mechanism="Severe AS LV hypertrophy stiff ventricle、preload-dependent、無法即時增加 stroke volume。SVR↓ → 系統 hypotension → 冠脈灌流壓↓ → subendocardial ischemia → arrhythmia → 死亡。",
    options={
        "A": "正確 (是適當的)。Severe AS 可能無症狀，也可能出現 heart failure、angina、syncope。",
        "B": "錯誤 (本題錯誤)。應「維持高 SVR」非降低。Phenylephrine 為 vasopressor of choice。",
        "C": "正確 (是適當的)。Sinus rhythm + atrial kick (30% CO) 為 critical；AF/arrhythmia 災難。",
        "D": "正確 (是適當的)。Norepinephrine 升 SVR + 輕度 β₁ inotropic，適合 severe AS hypotension。",
    },
    guidelines=[
        "ACC/AHA 2014 Valvular Heart Disease：Severe AS AVA < 1.0、mean gradient > 40、velocity > 4.0。",
        "TAVR 高風險病人替代 open AVR (PARTNER trial)。",
        "Anesthesia：通常 GA + invasive monitoring + judicious fluid + phenylephrine。",
    ],
    points=[
        "Coronary perfusion 嚴重依賴 diastolic BP — 維持 ≥ 60 mmHg",
        "心律不整 (especially AF) 失去 atrial kick (30% CO)、致命",
        "TEE 監測 LV function 與 valve gradient",
    ],
    keyword="Severe aortic stenosis, SVR, hemodynamic goal",
    source="ACC/AHA 2014 Valvular Heart Disease Guidelines",
)

# ===== Q41 (B) OLV hypoxia — 不應夾閉肺靜脈 =====
add(41,
    summary="OLV hypoxia 處置：FiO₂ 1.0、確認 DLT 位置、PEEP/CPAP、recruitment。「夾閉肺靜脈」為極端最後手段；夾「肺動脈 (PA)」減少 shunt 才是合理 (亦罕用)。「夾肺靜脈」反而會加重 PE-like 病理。",
    mechanism="OLV 期間 nonventilated lung HPV (hypoxic pulmonary vasoconstriction) 自然分流血流。Severe hypoxia → 處置依序：(1) FiO₂↑；(2) Confirm DLT；(3) CPAP non-ventilated；(4) Recruitment；(5) PEEP；(6) Clamp PA (極端、需與術者協調)。Clamp PV 無臨床意義且危險。",
    options={
        "A": "正確 (是適當的)。FiO₂ 1.0 為第一步驟。",
        "B": "錯誤 (本題不適當)。應建議夾「肺動脈 (PA)」非「肺靜脈 (PV)」；且為極端最後手段。",
        "C": "正確 (是適當的)。Fiberoptic 確認 DLT 位置 — DLT malposition 為最常見原因。",
        "D": "正確 (是適當的)。Recruitment maneuvers 改善 ventilated lung 通氣。",
    },
    guidelines=[
        "AAGBI Thoracic Anesthesia 2010。",
        "Hypoxia algorithm: (1) FiO₂↑；(2) confirm DLT；(3) CPAP non-ventilated；(4) recruitment；(5) PEEP；(6) clamp PA (極端)。",
        "DLT vs Bronchial blocker：DLT 較快、suction 容易；BB 適合 ETT 已 in situ、difficult airway。",
    ],
    points=[
        "Most common cause OLV hypoxia: DLT migration (especially after position change)",
        "Apneic insufflation 5-10 cmH₂O O₂ to non-ventilated lung",
        "Right-sided surgery: place left DLT (避免 RUL blockage)",
    ],
    keyword="One-lung ventilation, hypoxia, DLT, HPV",
    source="Miller's Anesthesia 8/e Ch. 65 Thoracic Anesthesia",
)

# ===== Q42 (B) Beta blocker 不抑制 HPV =====
add(42,
    summary="Beta blocker 「不抑制」HPV。HPV inhibitors 為 vasodilator (calcium channel blocker、nitroglycerin、milrinone、SNP、isoflurane > 1 MAC)。Beta blocker 不影響 pulmonary vasoreactivity。",
    mechanism="HPV (Hypoxic Pulmonary Vasoconstriction) 為缺氧區域 pulmonary artery 收縮、血流 redirect 至 oxygenated region 機制。Inhibitors: 揮發性麻醉劑 (high MAC)、vasodilator (nitrate、 nicardipine、 milrinone)、PEEP 過高、metabolic alkalosis、hypocapnia。Beta blocker 主要作用於 systemic β receptors，對 pulmonary vasoreactivity 影響小。",
    options={
        "A": "錯誤 (會抑制 HPV)。CCB (nifedipine、 nicardipine) 抑制 pulmonary vasoconstriction。",
        "B": "正確 (本題答案)。Beta blocker「不抑制」HPV。",
        "C": "錯誤 (會抑制 HPV)。Nitroglycerin 為 vasodilator 抑制 HPV。",
        "D": "錯誤 (會抑制 HPV)。Milrinone (PDE3 inhibitor) 為 inodilator，抑制 HPV。",
    },
    guidelines=[
        "Inhaled NO 用於 pulmonary HTN、 ARDS、 refractory hypoxia OLV (selective pulmonary vasodilator) — 不抑制 HPV。",
        "Sevoflurane < 1 MAC + TIVA 對 OLV 較好 (HPV preserved)。",
    ],
    points=[
        "Inhaled NO 為 selective pulmonary vasodilator，改善 V/Q",
        "Inhaled milrinone 為新興 selective option",
        "Hypocapnia 抑制 HPV → 維持 normocapnia",
    ],
    keyword="Hypoxic pulmonary vasoconstriction, beta blocker, vasodilator",
    source="Miller's Anesthesia 8/e Ch. 27",
)

# ===== Q43 (C) OCR 反射路徑 =====
add(43,
    summary="眼心反射 (OCR) 反射路徑為「三叉神經傳入、迷走神經傳出」(trigeminovagal arc)。題目敘述「迷走神經傳入、三叉神經傳出」為「錯誤」。",
    mechanism="OCR：眼外肌牽引或眼球壓迫 → long ciliary nerve → ophthalmic V₁ → trigeminal ganglion (afferent) → trigeminal nucleus → vagal nerve (efferent) → SA node → bradycardia。Hypoxia、hypercapnia、light anesthesia 加重反射。",
    options={
        "A": "正確 (是適當的處置)。立即停止手術刺激為第一步。",
        "B": "正確 (是適當的處置)。Atropine 0.02 mg/kg IV 治療 bradycardia。",
        "C": "錯誤 (本題錯誤敘述)。正確為「三叉神經傳入、迷走神經傳出」非反過來。",
        "D": "正確 (是適當的)。Retrobulbar block 可能 trigger OCR (刺激 long ciliary nerve)。",
    },
    guidelines=[
        "Pediatric Anesthesia: prophylactic atropine 0.02 mg/kg IV before traction in high-risk procedures。",
        "Treatment: (1) stop traction；(2) IV atropine 0.02 mg/kg；(3) ensure adequate ventilation；(4) deepen anesthesia。",
    ],
    points=[
        "Recurrence: repeat traction may recur (反射 fatiguable)",
        "可能 reflexes: nausea、 bronchospasm、 laryngospasm",
        "Severe: sinus arrest、asystole — CPR 啟動",
    ],
    keyword="Oculocardiac reflex, trigeminovagal, atropine",
    source="Coté and Lerman Pediatric Anesthesia 6/e",
)

# ===== Q44 (B) 甲狀腺風暴死亡率 =====
add(44,
    summary="甲狀腺風暴 (thyroid storm) 死亡率約「10-30%」 (即使現代治療)，「不是 80%」。雖然嚴重，但 80% 過高估計。",
    mechanism="甲狀腺風暴由 surgery、 infection、 trauma、 iodine 暴露、 stop antithyroid drugs 觸發。Increased catecholamine sensitivity 主導心血管表現 (tachycardia、AF、 heart failure)。Treatment 與時間賽跑：β-blocker、 PTU、 iodine、 steroid、 cooling。",
    options={
        "A": "正確 (是適當的)。Surgery、 infection、 trauma、 parturition 為常見 trigger。",
        "B": "錯誤 (本題錯誤)。死亡率約 10-30%、「不是 80%」。",
        "C": "正確 (是適當的)。常於術後 6-24 小時出現。",
        "D": "正確 (是適當的)。PTU 術前「不停藥」，繼續抑制甲狀腺荷爾蒙合成。",
    },
    guidelines=[
        "American Thyroid Association Hyperthyroidism Guidelines 2016。",
        "Burch-Wartofsky Point Scale 評估 thyroid storm severity。",
        "Sequence：(1) β-blocker；(2) PTU 600-1000 mg loading；(3) iodine (>1h after PTU)；(4) dexamethasone 2 mg q6h。",
    ],
    points=[
        "β-blocker 在 acute HF 慎用 — esmolol short-acting 較安全",
        "Aspirin 禁忌 (displace T4 from binding → free T4↑)",
        "Severe cases: plasmapheresis、 therapeutic hypothermia 考慮",
    ],
    keyword="Thyroid storm, mortality, propranolol",
    source="ATA Hyperthyroidism Guidelines 2016",
)

# ===== Q45 (D) Tetralogy of Fallot 特徵錯誤 =====
add(45,
    summary="Tetralogy of Fallot 四特徵：(1) Pulmonary stenosis (RVOT obstruction)；(2) RV hypertrophy；(3) Overriding aorta；(4) VSD。「左心室出口狹窄」「不是」TOF 特徵。",
    mechanism="RVOT obstruction → RV pressure↑ → RVH。VSD allows R-to-L shunt → deoxygenated blood 進入體循環 → cyanosis。",
    options={
        "A": "正確。TOF 為發紺型先天性心臟病。",
        "B": "正確。VSD 為四特徵之一。",
        "C": "正確。Pulmonary stenosis (RVOT obstruction) 為四特徵之一。",
        "D": "錯誤 (本題錯誤)。TOF 為「右」心室出口狹窄 (pulmonary stenosis)，「不是左心室出口狹窄」。",
    },
    guidelines=[
        "AHA Congenital Heart Disease Guidelines。",
        "Anesthesia for TOF：maintain SVR、 avoid hypovolemia、 avoid extreme tachycardia、 reduce RVOT spasm。",
        "Tet spell：knee-chest position、 O₂、 IV fluid、 phenylephrine、 morphine、 esmolol。",
    ],
    points=[
        "Most common cyanotic CHD > 1 yr old",
        "Surgical repair: complete repair at 3-6 months ideal",
        "Anesthetic: avoid drops in SVR (worsens R-to-L shunt)",
    ],
    keyword="Tetralogy of Fallot, RVOT obstruction, pulmonary stenosis",
    source="Coté and Lerman Pediatric Anesthesia 6/e",
)

# ===== Q46 (C) DLT 開口錯誤 =====
add(46,
    summary="Left DLT 結構：「氣管端 (tracheal limb) 1 個開口、支氣管端 (bronchial limb) 1 個開口」，並非「氣管 1、支氣管 2」。",
    mechanism="Left DLT 設計：tracheal lumen 開口位於氣管 (對 right lung ventilation)；bronchial lumen 開口位於 left mainstem bronchus (對 left lung ventilation)。各有 1 個 cuff + 1 個 distal opening。",
    options={
        "A": "正確 (是適當的處置)。先打 tracheal cuff (氣管端) 防漏氣，再 advance bronchial limb。",
        "B": "正確 (是適當的處置)。Bronchial cuff 上緣應剛好在 carina，避免過深 (RUL blockage)。",
        "C": "錯誤 (本題錯誤)。氣管端與支氣管端「各 1 個開口」，非氣管 1 支氣管 2。",
        "D": "正確 (是適當的處置)。Difficult airway 可用 single-lumen ETT + bronchial blocker。",
    },
    guidelines=[
        "Fiberoptic bronchoscopy 為 DLT 位置 confirmation gold standard。",
        "DLT size 依身高、性別 (女性 35-37 Fr、男性 39-41 Fr)。",
        "Bronchial blocker 為替代：difficult airway、 already intubated。",
    ],
    points=[
        "DLT malposition 為 OLV hypoxia 主因",
        "Position change (lateral decubitus) 後重新確認位置",
        "Single-lumen ETT + bronchial blocker 為較容易插管之替代",
    ],
    keyword="Double-lumen tube, DLT anatomy, OLV",
    source="Miller's Anesthesia 8/e Ch. 65",
)

# ===== Q47 (B) T&A bleeding — 不是 2 週後 =====
add(47,
    summary="Post-tonsillectomy bleeding 通常發生於「24 小時內 (primary, surgical)」或「5-10 天 (secondary, eschar separation)」。「術後 2 週之後」過遲，不符典型。",
    mechanism="Primary bleeding (< 24h): surgical hemostasis 不足。Secondary bleeding (5-10 days): eschar (痂) 脫離後血管暴露。2 週後出血罕見且 atypical。",
    options={
        "A": "正確 (是適當的)。出血病人可能 agitation、tachycardia、低血壓 (hypovolemia)。",
        "B": "錯誤 (本題不適當)。出血典型 24h 內或 5-10 天，「不是 2 週後」。",
        "C": "正確 (是適當的)。< 3 歲建議常規住院觀察 (OSA、respiratory complications)。",
        "D": "正確 (是適當的)。再次手術應 RSI (full stomach + 吞入血液)。",
    },
    guidelines=[
        "APAGBI Difficult Pediatric Airway 2015。",
        "Pre-induction: IV fluid resuscitation 20 mL/kg、 血品準備。",
        "RSI: ketamine + etomidate 維持循環、 succinylcholine 1.5 mg/kg 或 rocuronium 1.2 mg/kg。",
        "Two large suctions ready。",
    ],
    points=[
        "拔管時:完全清醒、protective reflexes、 lateral position",
        "成人 + 兒童同樣處置原則",
        "考慮 left lateral head-down 防 aspiration",
    ],
    keyword="Post-tonsillectomy bleeding, primary vs secondary, RSI",
    source="APAGBI; Coté and Lerman 6/e",
)

# ===== Q48 (D) ICD — 磁鐵移除恢復 =====
add(48,
    summary="磁鐵置於 ICD 上「暫時 disable」 tachyarrhythmia detection/therapy (shock function)，「移除磁鐵後恢復原本設定」。Pacemaker 部分磁鐵會 trigger asynchronous pacing。",
    mechanism="Magnet over ICD: disable tachyarrhythmia therapy 但不影響 pacing。Move magnet → restore original settings。各 manufacturer 細節不同 (Medtronic、Boston Scientific、St. Jude、Biotronik)。",
    options={
        "A": "正確 (是適當的)。Monopolar electrocautery 比 bipolar 更易 EMI。",
        "B": "正確 (是適當的)。連絡廠商調整、貼 transcutaneous defibrillator 為標準。",
        "C": "正確 (是適當的)。連續 EKG + arterial line 為重要監測。",
        "D": "錯誤 (本題錯誤)。應為「移除後恢復原本設定」非「都會恢復去顫」(去顫被 disable，pacing 不變)。實際上需確認廠商設定，prompt 似乎暗示句意不準。",
    },
    guidelines=[
        "HRS/ASA Expert Consensus 2011 on CIED Management。",
        "Cardiology consultation pre-op (CIED check、 interrogation)。",
        "Post-op interrogation: ensure restored function、 check parameters。",
        "Bipolar cautery > monopolar；short bursts。",
    ],
    points=[
        "Pacemaker-dependent: magnet → asynchronous (e.g. VOO 80 bpm)",
        "ICD shock during surgery: stop electrocautery、 magnet over device",
        "CPR over device OK if needed",
    ],
    keyword="ICD, pacemaker, magnet, electrocautery",
    source="HRS/ASA Expert Consensus on CIED 2011",
)

# ===== Q49 (C) CPB — Protamine IV push 錯誤 =====
add(49,
    summary="Protamine 「不可 IV push」(快速 IV → 嚴重 hypotension、pulmonary hypertension、anaphylactoid 反應)。應緩慢輸注 over 10-15 min。",
    mechanism="Protamine 為高度正電 polypeptide，中和 heparin (負電)。Rapid IV → histamine release + complement activation + pulmonary vasoconstriction → severe hypotension、PH、RV failure。緩慢輸注降低風險。",
    options={
        "A": "正確 (是適當的)。CPB 低溫降低 NMBA metabolism → 阻斷加強、延長。",
        "B": "正確 (是適當的)。降低 TV 通氣減少肺擴張遮蔽手術視野。",
        "C": "錯誤 (本題錯誤)。Protamine 「不可 IV push」；緩慢輸注 over 10-15 min。",
        "D": "正確 (是適當的)。Protamine 可引起 pulmonary HTN、RV failure，需 monitor。",
    },
    guidelines=[
        "STS/SCA Anesthetic Management of Cardiac Surgery。",
        "ACT > 480 sec for CPB (heparin)。",
        "Antifibrinolytic (TXA、ε-aminocaproic acid) 減少 bleeding。",
        "Coming off CPB: rewarm、 wean ventilation、 inotropic support、 TEE。",
    ],
    points=[
        "Hypothermia: every 1°C ↓ → CMRO₂ ↓ 6-7%",
        "Volatile anesthetic via CPB circuit, monitor BIS",
        "Heparin-induced thrombocytopenia (HIT)：用 bivalirudin 替代",
    ],
    keyword="CPB, protamine, slow infusion, anaphylactoid",
    source="STS/SCA Cardiac Surgery Anesthesia",
)

# ===== Q50 (A) 幽門狹窄 — 母乳禁食 4h 錯誤 =====
add(50,
    summary="幽門狹窄病人「不應使用標準 NPO」— 視為「full stomach」 (持續嘔吐、吸入風險高)，需 OG decompression、RSI。母乳一般禁食 4h 但「不適用於幽門狹窄」病人。",
    mechanism="Pyloric stenosis 胃幽門肥厚 → 出口阻塞 → 反覆嘔吐 → loss of HCl + 脫水 + hypochloremic metabolic alkalosis + hypokalemia。胃排空不可預測，full stomach 視之。",
    options={
        "A": "錯誤 (本題錯誤)。幽門狹窄病人需 OG decompression + RSI，「不適用母乳 4h」一般 NPO。",
        "B": "正確。Metabolic alkalosis + dehydration 為典型，須矯正才能手術。",
        "C": "正確。麻醉前 OG tube 排空胃為必要 (full stomach 風險)。",
        "D": "正確。建議用 cuffed ETT 防止 aspiration。",
    },
    guidelines=[
        "APAGBI Neonatal Surgery：electrolyte correction first; Cl > 100、 HCO₃ < 30 為 surgery criteria。",
        "麻醉：full stomach RSI、 suction OG tube、 warm fluids、 normothermia。",
        "Post-op：apnea risk (residual alkalosis depresses respiration)、 glucose monitoring。",
    ],
    points=[
        "Typical infant: 3-6 wks old、firstborn male、projectile vomiting",
        "Olive-shaped mass palpable RUQ、US confirms",
        "Pyloromyotomy curative",
    ],
    keyword="Pyloric stenosis, RSI, metabolic alkalosis",
    source="Coté and Lerman 6/e",
)

# ===== Q51 (A) 剖腹產 ERAS 禁食 8h 錯誤 =====
add(51,
    summary="ERAS for cesarean section：「清液 2h、固體 6-8h」為標準。「術前禁食 8 小時」過長，且 ERAS 鼓勵「術前 2h 給予 carbohydrate drink」減少 insulin resistance + 改善舒適。",
    mechanism="ERAS principles 適用 CS：減少 surgical stress、 improve recovery、enable bonding、降低 LOS。Pre-op fasting 過長反而增加 insulin resistance、 hypovolemia、 maternal discomfort。",
    options={
        "A": "錯誤 (本題錯誤)。應為清液 2h、固體 6h；ERAS 建議 2h CHO drink。「8 小時禁食」過長。",
        "B": "正確。等容性 (zero-balance) 晶體溶液輸液為 ERAS 原則。",
        "C": "正確。Active warming (forced air、warm fluids) 預防低體溫。",
        "D": "正確。下肢 intermittent pneumatic compression 預防 VTE。",
    },
    guidelines=[
        "ERAS Society Cesarean Delivery Guidelines 2018-2019。",
        "SOAP Consensus 2020。",
        "Multimodal analgesia: intrathecal morphine、 acetaminophen、 NSAID、 TAP block (rescue)。",
    ],
    points=[
        "Intrathecal morphine 0.1 mg 提供 18-24h analgesia",
        "Early oral intake (within 2h)、early mobilization (within 6h)",
        "Early Foley removal (≤ 12h) 減少 UTI",
    ],
    keyword="ERAS, cesarean section, NPO, carbohydrate drink",
    source="ERAS Society CS Guidelines; SOAP Consensus",
)

# ===== Q52 (C) 12 kg 兒童輸液 — 70 mL =====
add(52,
    summary="12 kg 兒童 1 小時輸液：Maintenance (4-2-1 rule)：4×10 + 2×2 = 44 mL/h。Surgical loss for moderate surgery (ureteral reimplantation) 約 2-3 mL/kg/h = 24-36 mL/h。Total ≈ 70 mL/h。",
    mechanism="兒童 fluid 三組成：maintenance (Holliday-Segar) + deficit replacement + ongoing loss。NPO 已矯正，主要為 maintenance + surgical loss。Ureteral reimplantation 為 moderate surgery (2-4 mL/kg/h evaporative/3rd space loss)。",
    options={
        "A": "錯誤。44 mL = maintenance only，未加 surgical loss。",
        "B": "錯誤。50 mL 為 maintenance + minimal surgical loss，未充分。",
        "C": "正確 (本題答案)。Maintenance 44 + surgical loss ~25 = 70 mL/h 為合理範圍。",
        "D": "錯誤。110 mL 過量，可能 fluid overload。",
    },
    guidelines=[
        "APA 2018 Pediatric Perioperative Fluid Management：isotonic fluid + dextrose containing for maintenance。",
        "Avoid hypotonic D5W (hyponatremia risk)。",
        "Goal-directed where possible。",
    ],
    points=[
        "4-2-1 rule: 4 mL/kg/h first 10 kg、 2 mL/kg/h next 10 kg、 1 mL/kg/h beyond",
        "Surgical loss: minor 1-2、 moderate 2-4、 major 4-8 mL/kg/h",
        "Hypoglycemia risk infant: add D5 maintenance",
    ],
    keyword="Pediatric fluid, 4-2-1 rule, maintenance + replacement",
    source="APA Pediatric Fluid Guidelines 2018; Coté and Lerman 6/e",
)

# ===== Q53 (D) 子癇前症 + MgSO4 + Sux 不減量 =====
add(53,
    summary="MgSO₄ 對 「nondepolarizing NMBA (rocuronium、vecuronium、cisatracurium)」 顯著加成，需減量 50%。但對「succinylcholine (depolarizing)」 並無需減量 — Sux 作用機轉不同。",
    mechanism="Magnesium 阻斷 presynaptic Ca channel → 降低 ACh release，與 nondepolarizing NMBA 協同 → prolonged paralysis。Succinylcholine 為 depolarizing 競爭性 agonist，Mg 對其影響小，不需減量。",
    options={
        "A": "正確。MgSO₄ 停藥增加 seizure 風險。",
        "B": "正確。Rocuronium (nondepolarizing) 受 Mg 加成、延長作用。",
        "C": "正確。TOF 監測精準 NMBA 用量。",
        "D": "錯誤 (本題錯誤)。Succinylcholine 「不需」因 MgSO₄ 減量；Mg 主要影響 nondepolarizing。",
    },
    guidelines=[
        "ACOG Practice Bulletin 222 (2020) Preeclampsia/Eclampsia。",
        "Therapeutic Mg range 4-8 mg/dL；toxicity (loss DTR、 respiratory depression) > 10。",
        "Anesthesia: avoid Sux high dose、 reduce nondepolarizing NMBA dose 50%、 TOF monitoring。",
    ],
    points=[
        "Magnesium continue 24h postpartum (seizure prophylaxis)",
        "Antihypertensive: labetalol、 hydralazine、 nifedipine",
        "Spinal/epidural still preferred for CS in preeclampsia (improved BP control)",
    ],
    keyword="MgSO4, preeclampsia, succinylcholine, NMBA",
    source="ACOG Practice Bulletin 222; Chestnut 6/e",
)

# ===== Q54 (C) 產後大出血 — MgSO4 不能幫助收縮 =====
add(54,
    summary="MgSO₄ 「不能」幫助子宮收縮，反而「會抑制」子宮收縮 (Mg 為 tocolytic)。子宮收縮無力應用 oxytocin、ergometrine、carboprost、misoprostol。",
    mechanism="Magnesium 阻斷 calcium channel → 降低 smooth muscle 收縮 → 子宮平滑肌鬆弛 (tocolysis 用於 preterm labor)。產後出血 + 子宮收縮無力應用 uterotonics 而非 Mg。",
    options={
        "A": "正確。Spinal level 依手術範圍：vagina/cervix T10、uterus T4。",
        "B": "正確。Edema 風險高，準備 short-handle 喉鏡 + smaller ETT。",
        "C": "錯誤 (本題錯誤)。MgSO₄ 「抑制」子宮收縮，不能幫助；應用 oxytocin/ergometrine。",
        "D": "正確。TEG/ROTEM 引導 goal-directed transfusion。",
    },
    guidelines=[
        "ACOG Practice Bulletin 183 Postpartum Hemorrhage。",
        "Sequence: oxytocin → methylergonovine (avoid in HTN) → carboprost (avoid in asthma) → misoprostol → TXA。",
        "Massive transfusion 1:1:1。",
    ],
    points=[
        "Tranexamic acid 1g IV within 3h of PPH onset (WOMAN trial)",
        "Surgical: B-Lynch、uterine artery ligation、 hysterectomy",
        "Interventional radiology: uterine artery embolization",
    ],
    keyword="Postpartum hemorrhage, uterine atony, MgSO4 tocolysis",
    source="ACOG Practice Bulletin 183; WOMAN trial",
)

# ===== Q55 (C) PDPH — 預防性 blood patch 錯誤 =====
add(55,
    summary="「預防性 (prophylactic) epidural blood patch」對 PDPH 預防「無顯著效果」(meta-analysis 不一致)。Blood patch 用於「治療」symptomatic PDPH (rescue)，非「預防」。",
    mechanism="PDPH 由 CSF leak 引起 intracranial hypotension → 牽引 pain-sensitive structures。Blood patch sealing dural defect + 增加 epidural pressure。預防性使用爭議：可能增加感染、neurologic complication 風險，且不一定有效。",
    options={
        "A": "正確。Risk factors：female、 pregnancy、多次 puncture、 prior headache history。",
        "B": "正確。鑑別 cortical vein thrombosis、 subdural hematoma、 preeclampsia (postpartum)、 primary headache。",
        "C": "錯誤 (本題錯誤)。預防性 blood patch 「無顯著預防效果」；blood patch 為 rescue treatment。",
        "D": "正確。Pencil-point needle (Whitacre、Sprotte) + 小 gauge 顯著降低 PDPH 率。",
    },
    guidelines=[
        "ASRA 2010 PDPH Consensus。",
        "預防：pencil-point needle、最小 gauge、減少嘗試次數。",
        "EBP timing：症狀 24-48h 後執行成功率較佳；可重複 1-2 次。",
    ],
    points=[
        "EBP 15-20 mL autologous blood、success rate 70-90%",
        "Sphenopalatine ganglion block 為新興 option",
        "Differential：cortical vein thrombosis、 subdural hematoma、 preeclampsia",
    ],
    keyword="PDPH, epidural blood patch, prophylactic",
    source="Chestnut 6/e Ch. 30; ASRA 2010",
)

# ===== Q56 (D) 牙科特殊需求 — IM pentobarbital 不適當 =====
add(56,
    summary="IM pentobarbital 「不適用」於現代特殊需求牙科鎮靜：作用慢、長半衰期、 high respiratory depression 風險、 difficult titration、 prolonged sedation。已大量被 dexmedetomidine、 ketamine、 midazolam 取代。",
    mechanism="Pentobarbital (barbiturate) 為長作用、 dose-dependent CNS depression。IM 起效慢 (10-30 min)、效果不可滴定、副作用大。現代 pediatric sedation 偏好短效、可滴定藥物。",
    options={
        "A": "正確 (是適當的)。Intranasal midazolam 0.2-0.5 mg/kg 為兒童常用 anxiolysis。",
        "B": "正確 (是適當的)。IM ketamine 4-6 mg/kg 為 uncooperative + difficult IV 標準。",
        "C": "正確 (是適當的)。Inhaled N₂O/O₂ 50/50 為兒童牙科常用。",
        "D": "錯誤 (本題不適當)。IM pentobarbital 為過時藥物，已不建議現代 pediatric sedation。",
    },
    guidelines=[
        "AAP/ASA Pediatric Sedation Guidelines。",
        "ADA Special Needs Dental Care。",
        "Premedication: oral midazolam 0.5 mg/kg、 intranasal dexmedetomidine 2 µg/kg、 IM ketamine 4-6 mg/kg。",
    ],
    points=[
        "Family-centered approach 加 parental presence",
        "Mask induction sevoflurane 8% + O₂；secure airway + IV after asleep",
        "Post-op: monitor for emergence agitation",
    ],
    keyword="Pediatric sedation, special needs, pentobarbital outdated",
    source="AAP/ASA Pediatric Sedation Guidelines",
)

# ===== Q57 (D) PDA ligation — fentanyl + cisatracurium =====
add(57,
    summary="新生兒 PDA ligation 麻醉：Fentanyl (穩定血流動力學) + Cisatracurium (Hofmann elimination, organ-independent) 為合適組合。",
    mechanism="新生兒 hemodynamic 脆弱，preferred opioids = fentanyl (穩定)、avoid bolus large doses。Cisatracurium 經 Hofmann elimination + ester hydrolysis，不依賴肝腎，適合新生兒。",
    options={
        "A": "錯誤。高 FiO₂ 對早產兒 retinopathy of prematurity (ROP) 風險、且可能 PDA 收縮反加重 L-to-R shunt。",
        "B": "錯誤。Prostaglandin E1 「維持 PDA 開放」(用於 ductal-dependent CHD)；不會「關閉」PDA。Indomethacin/ibuprofen 才是 medical closure。",
        "C": "錯誤。Right arm pre-ductal、 左下肢 post-ductal — 用於評估 shunt direction；不是「都在右手」。",
        "D": "正確 (本題答案)。Fentanyl + cisatracurium 為新生兒 PDA 麻醉合適組合。",
    },
    guidelines=[
        "APAGBI Neonatal Cardiac Anesthesia。",
        "Indomethacin/ibuprofen 為 medical closure (premature)，但有 contraindications。",
        "Sufficient blood products available; thoracotomy 出血可大量。",
    ],
    points=[
        "RLN injury: vocal cord paralysis、 stridor",
        "Temperature management critical (small infant)",
        "Hemodynamic monitoring: BP cuff (right arm preferred — coarctation rule out)",
    ],
    keyword="PDA ligation, premature, cisatracurium, fentanyl",
    source="Coté and Lerman 6/e",
)

# ===== Q58 (B) 兒童氣道錯誤 — 聲門狹窄 =====
add(58,
    summary="兒童氣道傳統教學「最狹窄處為環狀軟骨 (cricoid)」非聲門 (glottis)。雖然近年動態 MRI 研究顯示功能上 glottis 也窄，但傳統教科書仍以 cricoid 為主。「聲門最狹窄、需用較細 ETT」敘述不準確。",
    mechanism="Pediatric airway funnel-shaped，cricoid (subglottic) 為傳統最窄處。Cuffed ETT 選 size 時仍考慮 cricoid 較小。新研究 vocal cords 為 functional narrowest but cricoid 仍 critical for ETT size。",
    options={
        "A": "正確 (是適當的特徵)。扁桃體與腺樣體肥大為兒童上呼吸道阻塞常見原因。",
        "B": "錯誤 (本題錯誤)。傳統最窄處為「環狀軟骨 (cricoid)」非聲門；現代仍以此為 ETT 選擇基礎。",
        "C": "正確 (是適當的特徵)。會厭較長、 omega/U-shaped 影響聲門視野。",
        "D": "正確 (是適當的特徵)。枕骨突出，仰臥自然 sniffing position；但臥位可使頸前屈、阻塞氣道。",
    },
    guidelines=[
        "APAGBI Pediatric Airway Guidelines。",
        "Cuffed ETT now widely accepted (Khine 等研究)。",
        "ETT size: cuffed = (age/4) + 3.5；uncuffed = (age/4) + 4。",
        "Depth: (age/2) + 12 cm at lip。",
    ],
    points=[
        "Newborn: sniffing position natural; older child needs shoulder roll",
        "Suction equipment & various size ETT ready",
        "Rapid desaturation due to low FRC + high O₂ consumption",
    ],
    keyword="Pediatric airway, cricoid, ETT size",
    source="Coté and Lerman 6/e; APAGBI Guidelines",
)

# ===== Q59 (B) Carbetocin 維持時間 =====
add(59,
    summary="Carbetocin (Duratocin®) 為 long-acting oxytocin analog，半衰期 ~40 min，「維持時間較 oxytocin 長」(非短)。Single 100 µg IV 可取代 oxytocin infusion。",
    mechanism="Carbetocin 與 oxytocin receptor binding → 子宮收縮、PPH 預防。較 oxytocin 抗水解 → 延長作用 (4-7×)。Single dose 提供持續子宮收縮。",
    options={
        "A": "正確。Single 100 µg IV slow injection over ≥ 1 min (避免 hypotension)。",
        "B": "錯誤 (本題錯誤)。Carbetocin 維持時間「較 oxytocin 長」非短。",
        "C": "正確。2h 內 contraction 不良不應重複，應考慮其他 uterotonics。",
        "D": "正確。Hypotension 副作用：preeclampsia 病人需 BP 監測。",
    },
    guidelines=[
        "WHO PPH Prevention：carbetocin 為 oxytocin 替代 (heat-stable for low-resource settings)。",
        "FIGO Guidelines：carbetocin 同 oxytocin efficacy for PPH prevention CS。",
        "CHAMPION trial：heat-stable carbetocin non-inferior to oxytocin for PPH prevention。",
    ],
    points=[
        "Single dose 100 µg IV slow (avoid hypotension)",
        "Heat-stable formulation 適合 low-resource settings",
        "Cost 較 oxytocin 高",
    ],
    keyword="Carbetocin, Duratocin, oxytocin analog, long-acting",
    source="WHO/FIGO PPH Guidelines; CHAMPION trial",
)

# ===== Q60 (C) HELLP =====
add(60,
    summary="36 週孕婦 + BP 160/110 + 頭痛 + 上腹痛 + 溶血 + 血小板 68K + AST/ALT 高 + LDH 高 + 蛋白尿 = HELLP syndrome (Hemolysis、Elevated Liver enzymes、Low Platelets)。",
    mechanism="HELLP：placental dysfunction → endothelial damage → microangiopathic hemolysis、liver ischemia、 platelet consumption。Mortality 1-25%；併發症 DIC、placental abruption、acute liver hemorrhage/rupture、AKI。",
    options={
        "A": "錯誤。Acute fatty liver of pregnancy (AFLP) AST/ALT 較高 + hypoglycemia + ammonia↑，與 HELLP 不同。",
        "B": "錯誤。妊娠高血壓單純無 hemolysis、 thrombocytopenia、 transaminase↑。",
        "C": "正確 (本題答案)。HELLP 三聯：溶血 + 肝酶↑ + 血小板低，加上 preeclamptic features。",
        "D": "錯誤。胰臟炎主 lipase↑、 epigastric pain，非此 LDH/platelet 特徵。",
    },
    guidelines=[
        "ACOG Practice Bulletin 222 (2020)。",
        "Delivery: ≥ 34 週 → 立即；< 34 週 → 個別化、 steroid for fetal lung maturity 可能。",
        "Anesthesia: regional preferred if platelet > 70K (some 50K)、 coagulation normal、 no DIC。",
        "Severe coagulopathy → GA。",
    ],
    points=[
        "Class I (plt < 50K)、II (50-100)、III (100-150)",
        "Magnesium continue 24h postpartum",
        "Steroid (dexamethasone) controversial — limited benefit for HELLP",
    ],
    keyword="HELLP syndrome, preeclampsia",
    source="ACOG Practice Bulletin 222; Chestnut 6/e Ch. 36",
)

# ===== Q61 (A) DMD — TIVA =====
add(61,
    summary="Duchenne Muscular Dystrophy (DMD) 麻醉：採「TIVA (propofol + remifentanil)，避免吸入性麻醉劑」。揮發性 + succinylcholine 為禁忌 (anesthesia-induced rhabdomyolysis + hyperkalemia)。",
    mechanism="DMD: dystrophin gene mutation → muscle membrane instability → muscle injury。Volatile anesthetic + succinylcholine 引起 fatal hyperkalemia + rhabdomyolysis + cardiac arrest，即使無 MH 表現。TIVA 為安全選擇。",
    options={
        "A": "正確 (本題答案)。TIVA 避免吸入麻醉與 succinylcholine。",
        "B": "錯誤。「需要」1 年內 echo + 肺功能評估 (DMD 多有 cardiomyopathy + restrictive lung disease)。",
        "C": "錯誤。Succinylcholine 「絕對禁忌」(fatal hyperkalemia)；應用 rocuronium + sugammadex。",
        "D": "錯誤。DMD 主要為「restrictive ventilation」非阻塞性；應 minute ventilation 維持。",
    },
    guidelines=[
        "MHAUS recommendations for DMD anesthesia。",
        "TIVA: propofol + remifentanil + rocuronium (with sugammadex reversal)。",
        "Pre-op cardiac evaluation: echo、 ECG、 Holter (DMD 50-80% cardiomyopathy by adolescence)。",
        "Post-op: monitor for rhabdomyolysis (CK)、 cardiac function、 respiratory failure。",
    ],
    points=[
        "DMD ≠ Malignant Hyperthermia, but similar precautions",
        "Cardiomyopathy progressive: 12-18 yrs onset",
        "Respiratory function decline; pulmonary risk assessment important",
    ],
    keyword="Duchenne muscular dystrophy, TIVA, succinylcholine contraindication",
    source="MHAUS DMD Guidelines; Coté and Lerman 6/e",
)

# ===== Q62 (B) 老化呼吸 — Total lung capacity 不變 =====
add(62,
    summary="老化呼吸系統變化：FEV1 下降、closing capacity「上升」、FRC「增加」、TLC「不變或微增」、ERV「減少」。「TLC 不變」為正確敘述。",
    mechanism="Elastin 破壞 → loss of elastic recoil → emphysema-like changes (senile emphysema)。Chest wall fibrosis → 壓迫減少 lung expansion。整體 TLC 維持不變或微增 (chest wall stiff 與 lung compliance↑ 互相平衡)。",
    options={
        "A": "錯誤。閉合容量 (closing capacity) 「上升」非下降；超過 FRC 引起 atelectasis。",
        "B": "正確 (本題答案)。TLC 大致不變或微增。",
        "C": "錯誤。FRC 「增加」非下降 (chest wall outward force unchanged + lung inward recoil↓)。",
        "D": "錯誤。ERV 「減少」非增加。",
    },
    guidelines=[
        "Respiratory aging predisposes 老年 to perioperative pulmonary complications。",
        "Pre-oxygenation more critical (faster desaturation due to ↑ closing capacity)。",
        "PEEP 5-10 cmH₂O 維持 FRC、 recruitment maneuver。",
    ],
    points=[
        "A-a gradient widens with age — expected PaO₂ formula: 100 − (age/3)",
        "Cough/swallow reflexes diminish → aspiration risk",
        "Sleep apnea prevalence high — screen and address",
    ],
    keyword="Respiratory aging, TLC, closing capacity",
    source="Stoelting's Co-existing Disease 7/e Ch. Aging",
)

# ===== Q63 (A) 老年 — LV 後負荷增加 =====
add(63,
    summary="老年生理變化：「LV 後負荷 (afterload) 增加」(動脈硬化 + arterial stiffness)；腦血流量「下降」；肺與胸壁順應力均「下降」；GFR「下降」。",
    mechanism="Aging arterial wall changes: elastin degradation + collagen deposition → stiff arteries → 系統收縮壓↑、 pulse pressure↑ → LV afterload↑ → LV concentric hypertrophy → diastolic dysfunction。",
    options={
        "A": "正確 (本題答案)。Arterial stiffness 引起 LV afterload↑。",
        "B": "錯誤。腦血流量「下降」非增加 (cerebral atrophy + vascular changes)。",
        "C": "錯誤。肺與胸壁順應力「均下降」(chest wall fibrosis、 lung elasticity 改變)。",
        "D": "錯誤。GFR「下降」非增加 (約 1 mL/min/yr after 40)。",
    },
    guidelines=[
        "ASA Brain Health Initiative：Perioperative neurocognitive disorders。",
        "Avoid Beers Criteria drugs：benzodiazepine、 anticholinergic、 meperidine。",
        "Dose adjustments: induction agents ↓ 30-50%; volatile ↓; opioid ↓。",
    ],
    points=[
        "Cr can be falsely normal (low muscle mass)；use Cockcroft-Gault 或 GFR formula",
        "Hypothermia risk high (low BMR、 thin skin)",
        "Frailty as predictor (Clinical Frailty Scale)",
    ],
    keyword="Geriatric physiology, LV afterload, arterial stiffness",
    source="Miller's Anesthesia 8/e Ch. 80",
)

# ===== Q64 (C) 老年 — TCA 抗膽鹼 =====
add(64,
    summary="三環抗憂鬱藥物 (TCA, e.g. imipramine、amitriptyline) 具「顯著抗膽鹼性作用」(antimuscarinic) → 老年人 cognitive impairment、 delirium、 urinary retention、 constipation。",
    mechanism="TCA 多重藥理：(1) NE/serotonin reuptake inhibition (antidepressant)；(2) Antimuscarinic (抗膽鹼)；(3) α-blockade (orthostatic hypotension)；(4) Na channel block (QT 延長、 arrhythmia)。老年 + polypharmacy 副作用累積。",
    options={
        "A": "錯誤。β-blocker 「降低」(非增加) 麻醉藥需求 (sympathetic tone↓)。",
        "B": "錯誤。長期酒精「增加」(非降低) 麻醉藥需求 (CYP induction + tolerance)。",
        "C": "正確 (本題答案)。TCA 具抗膽鹼作用 → cognitive、 GI、 GU 副作用。",
        "D": "錯誤。抗心律不整藥物 (lidocaine、amiodarone) 可能「增加」NMBA 作用，非降低。",
    },
    guidelines=[
        "Beers Criteria 2019 (AGS)：drugs to avoid or use with caution in elderly。",
        "STOPP/START Criteria：European version。",
        "Anticholinergic Cognitive Burden (ACB) scale。",
    ],
    points=[
        "Common offenders: diphenhydramine、 hydroxyzine、 amitriptyline、 oxybutynin",
        "Benzodiazepine 增加 falls、 fractures、 delirium",
        "NSAIDs renal、 GI、 cardiovascular concerns in elderly",
    ],
    keyword="Beers Criteria, TCA, anticholinergic",
    source="AGS Beers Criteria 2019",
)

# ===== Q65 (C) 肥胖 — PEEP ≥ 5 =====
add(65,
    summary="肥胖病人通氣建議「PEEP ≥ 5 cmH₂O」防止 alveoli 塌陷。TV 應依「IBW (理想體重)」非 TBW；lung-protective 不會引起 atelectasis 反而減少。",
    mechanism="肥胖 FRC ↓ (chest wall + abdominal mass)、 atelectasis、 shunt → 快速 desaturation。PEEP 維持 FRC、 recruit collapsed alveoli。Ideal body weight calculation 避免 over-distension。",
    options={
        "A": "錯誤。Lung-protective ventilation「減少」非引起 atelectasis (低 TV + PEEP + recruitment 合適搭配)。",
        "B": "錯誤。TV 應按「IBW」非「實際體重 (TBW)」；TBW 計算會 over-distension。",
        "C": "正確 (本題答案)。PEEP ≥ 5 cmH₂O 防止肺泡塌陷。",
        "D": "錯誤。Recruitment maneuvers 反而可能引起 transient hypotension (intrathoracic pressure↑)。",
    },
    guidelines=[
        "SOBA (Society for Obesity and Bariatric Anaesthesia) Guidelines。",
        "ARDS Network: low TV 4-6 mL/kg IBW for ARDS; 6-8 mL/kg IBW for healthy lung。",
        "Ramped position improves laryngoscopy + ventilation。",
    ],
    points=[
        "IBW (male) = 50 + 2.3 × (height in inches − 60); female = 45.5 + 2.3 × …",
        "Difficult mask ventilation in obese: BONES mnemonic",
        "OSA assessment: STOP-BANG questionnaire",
    ],
    keyword="Obesity ventilation, PEEP, IBW",
    source="SOBA Guidelines; ARDS Network",
)

# ===== Q66 (A) 肥胖 — 截石位 =====
add(66,
    summary="肥胖病人「截石位 (lithotomy)」會使腹腔內容物 cephalad 移向膈肌 → 減少肺容量 → 通氣不足。其他姿勢類似影響。",
    mechanism="Lithotomy + 肥胖：髖屈曲 + 腹腔內容物推向 diaphragm → FRC ↓、 atelectasis、 V/Q mismatch、 hypoxia。Trendelenburg 加重。",
    options={
        "A": "正確 (本題答案)。Lithotomy 使腹腔內容物移向膈肌、減少 FRC、 通氣不足。",
        "B": "錯誤。Lateral 可減輕腹部對橫膈壓力，但「不會降低咽部直徑」。",
        "C": "錯誤。Prone position 是「降低」FRC，但說法不完整。",
        "D": "錯誤。頭低腳高「加重」橫膈壓迫，不會改善呼吸功能。",
    },
    guidelines=[
        "SOBA Guidelines: 25-30° head-up tilt for pre-oxygenation。",
        "Ramped position: tragus aligned with sternal notch。",
        "Reverse Trendelenburg or sitting position improve FRC + ventilation。",
    ],
    points=[
        "Apneic time before desaturation 嚴重縮短 (FRC small、 O₂ consumption high)",
        "Pre-oxygenation 100% O₂ × 3-5 min + CPAP",
        "Intra-operative recruitment maneuvers maintain FRC",
    ],
    keyword="Obesity positioning, lithotomy, FRC",
    source="SOBA Guidelines",
)

# ===== Q67 (B) ERAS — 長效 NMBA 錯誤 =====
add(67,
    summary="ERAS 應使用「短效」NMBA + sugammadex 反轉，「不建議長效 NMBA」(延長甦醒、增加 PACU 時間)。",
    mechanism="ERAS 核心：rapid recovery、early extubation、early mobilization。長效 NMBA (pancuronium) 殘餘 effect 延長 PACU、 增加 PPC、 reintubation risk。Short-acting (rocuronium + sugammadex、 cisatracurium) 為首選。",
    options={
        "A": "正確。Short-acting anesthetics + analgesics 為 ERAS 標準。",
        "B": "錯誤 (本題錯誤)。應用「短效」NMBA，「不建議長效」。",
        "C": "正確。Zero-balance fluid management 為 ERAS 原則。",
        "D": "正確。Multimodal opioid-sparing 減少 opioid 副作用。",
    },
    guidelines=[
        "ERAS Society Pathways: Cardiac、 Colorectal、 Gynecology、 Orthopedic、 etc.。",
        "Pre-op: carbohydrate drink 2h、 multimodal pre-emptive。",
        "Intra-op: regional anesthesia preferred、 euvolemic goal-directed fluid、 normothermia。",
        "Post-op: early oral intake、 multimodal analgesia、 early mobilization。",
    ],
    points=[
        "Goal-directed fluid (SVV-guided) > liberal or restrictive",
        "PONV prophylaxis ≥ 2 agents in moderate risk (Apfel score)",
        "Regional anesthesia central to opioid-sparing",
    ],
    keyword="ERAS, NMBA, short-acting, sugammadex",
    source="ERAS Society Guidelines",
)

# ===== Q68 (B) Cefazolin 涵蓋 — 不僅 Gram+ =====
add(68,
    summary="Cefazolin (1st-gen cephalosporin) 涵蓋「Gram+ (Staph, Strep) + 部分 Gram-」 (E. coli、 Klebsiella、 Proteus)，「不僅」Gram+。所以「僅能預防革蘭氏陽性菌」為錯誤敘述。",
    mechanism="Cefazolin 為 1st-gen cephalosporin，主要 Gram+ coverage 但涵蓋部分 Gram- (PEK: Proteus、E. coli、Klebsiella)。為手術預防性 first choice (broad enough、low cost、low resistance)。",
    options={
        "A": "正確。Antibiotic timing：切皮前 60 min；vancomycin/fluoroquinolone 120 min。",
        "B": "錯誤 (本題錯誤)。Cefazolin 涵蓋 Gram+ + 部分 Gram-，「不僅 Gram+」。",
        "C": "正確。Neutrophil < 500 為 neutropenia，需延後 elective surgery。",
        "D": "正確。Anaphylaxis 立即停藥 + epinephrine。",
    },
    guidelines=[
        "ASHP/SHEA/IDSA Surgical Antibiotic Prophylaxis Guidelines 2013。",
        "CDC SSI Prevention Guidelines。",
        "Cefazolin standard for clean and clean-contaminated surgery。",
        "MRSA screening + vancomycin for high-risk patients。",
    ],
    points=[
        "Re-dose for prolonged surgery or large blood loss",
        "Hair removal: clipper not razor",
        "Normothermia + euglycemia + supplemental O₂ reduce SSI",
    ],
    keyword="Cefazolin, prophylactic antibiotic, Gram coverage",
    source="ASHP/SHEA/IDSA SSI Guidelines 2013",
)

# ===== Q69 (B) ASA NPO 兒童 =====
add(69,
    summary="ASA 2017 NPO Guidelines：清液 2h、 母乳 4h、 配方/非人類奶 6h、 light meal 6h、 fatty meal 8h。「配方牛奶 6h + 清液 2h」為正確敘述。",
    mechanism="Gastric emptying：clear liquid 最快、 milk + solid 較慢。Empty stomach 減少 aspiration risk。",
    options={
        "A": "錯誤。清液應為 2h，「不是 4h」。",
        "B": "正確 (本題答案)。Formula milk 6h + clear liquids 2h 為 ASA 標準。",
        "C": "錯誤。母乳應 4h，清液應 2h。",
        "D": "錯誤。母乳應 4h，「不是 6h」。",
    },
    guidelines=[
        "ASA Practice Guidelines for Preoperative Fasting 2017。",
        "APAGBI、 ESPNIC: longer fasting unnecessary, can lead to dehydration、 hypoglycemia in children。",
        "ERAS: 2h clear carbohydrate drink improves outcomes。",
    ],
    points=[
        "Diabetes、 GERD、 pregnancy、 obstruction → 延長禁食或 RSI",
        "Chewing gum considered clear liquid",
        "Black coffee, tea without milk → clear liquid",
    ],
    keyword="NPO, ASA fasting guidelines, pediatric",
    source="ASA Practice Guidelines for Preoperative Fasting 2017",
)

# ===== Q70 (D) Dopamine 首選錯誤 =====
add(70,
    summary="腹膜炎 + septic shock 升壓劑「首選 norepinephrine」非 dopamine。Dopamine 已退居 second-line (SOAP II trial：dopamine 死亡率較高、 arrhythmia 多)。",
    mechanism="Norepinephrine 對 α₁ + β₁ 親和；維持 MAP 同時避免 tachycardia。Dopamine 多重 receptor 作用、 dose-dependent → 高劑量副作用 (tachyarrhythmia、 increased mortality in shock)。",
    options={
        "A": "正確。Septic shock SVR 偏低、 distributive。",
        "B": "正確。Etomidate 維持 hemodynamics，RSI 合適。",
        "C": "正確。30 mL/kg crystalloid + vasopressor for MAP ≥ 65。",
        "D": "錯誤 (本題錯誤)。Septic shock 「首選 norepinephrine」非 dopamine。",
    },
    guidelines=[
        "Surviving Sepsis Campaign 2021。",
        "SOAP II Trial 2010：NE > dopamine in septic shock。",
        "Damage Control Surgery for septic peritonitis: source control + ICU optimization。",
    ],
    points=[
        "Avoid propofol high dose — cardiovascular collapse",
        "Awake intubation if extremely high aspiration risk + cooperative",
        "Aggressive fluid + early antibiotic + source control 為治療關鍵",
    ],
    keyword="Septic shock, dopamine, norepinephrine, SOAP II",
    source="Surviving Sepsis 2021; SOAP II",
)

# ===== Q71 (D) 困難呼吸道 — Sugammadex 200mg 錯誤 =====
add(71,
    summary="100 kg 病人 rocuronium 80 mg 後失敗插管，sugammadex 「immediate reversal」劑量為「16 mg/kg = 1600 mg」非「200 mg」(200 mg 不夠 reverse profound block)。",
    mechanism="Sugammadex 劑量依阻斷程度：moderate (TOF count 2-3) 2 mg/kg；deep (PTC ≥ 1) 4 mg/kg；immediate after rocuronium induction 16 mg/kg。100 kg × 16 = 1600 mg。",
    options={
        "A": "正確。求救 + 影像輔助 (video laryngoscope) 為 Plan B。",
        "B": "正確。LMA 為 Plan B/C (rescue ventilation)。",
        "C": "正確。Oral/nasal airway + 再次 mask 嘗試。",
        "D": "錯誤 (本題錯誤)。Sugammadex immediate reversal 需 16 mg/kg = 1600 mg；200 mg 不夠。",
    },
    guidelines=[
        "DAS 2015 Difficult Airway Guidelines。",
        "Sugammadex 16 mg/kg for emergency rocuronium reversal in CICO scenarios。",
        "Maximum 3 attempts at intubation; declare difficult airway。",
    ],
    points=[
        "Sugammadex 速度 < 3 min for reversal — 不能延誤 FONA",
        "Video laryngoscope as Plan A or B per institutional protocol",
        "Cannot Intubate Cannot Oxygenate (CICO) → FONA without delay",
    ],
    keyword="Difficult airway, sugammadex dosing, DAS algorithm",
    source="DAS 2015 Difficult Airway Guidelines",
)

# ===== Q72 (B) LAST — Lidocaine 治療 VF 錯誤 =====
add(72,
    summary="LAST 急救「禁忌 lidocaine」治療 VF (lidocaine 為 LA 一員，加重 toxicity)。應用 amiodarone；無 amiodarone 才考慮其他選項，但仍不應 lidocaine。",
    mechanism="Bupivacaine 高 lipid solubility → 心肌 Na channel + mitochondrial dysfunction → resistant 心律不整。Lidocaine 同樣 Na channel blocker，會加重 cardiotoxicity 與 conduction abnormalities。LAST ACLS：avoid vasopressin、 CCB、 β-blocker、 lidocaine、 procainamide。",
    options={
        "A": "正確。CPR 時 left uterine displacement 避免 IVC compression。",
        "B": "錯誤 (本題錯誤)。LAST 治療「禁忌 lidocaine」(加重 LA toxicity)。",
        "C": "正確。Defibrillation 120-200J biphasic。",
        "D": "正確。Lipid Emulsion 20% 1.5 mL/kg bolus + 0.25 mL/kg/min infusion。",
    },
    guidelines=[
        "ASRA Practice Advisory on LAST 2018 Checklist。",
        "20% Intralipid available in OR、 L&D, anywhere LA used。",
        "Total lipid emulsion ≤ 12 mL/kg。",
    ],
    points=[
        "Prevention: ultrasound guidance、 incremental injection、 test dose、 total dose calculation",
        "Bupivacaine total dose ≤ 2 mg/kg、 lidocaine ≤ 4.5 mg/kg (7 mg/kg with epi)",
        "Observe ≥ 12 hours after successful resuscitation",
    ],
    keyword="LAST, lipid emulsion, lidocaine contraindication",
    source="ASRA 2018 LAST Checklist",
)

# ===== Q73 (A) 擺位 — 手掌朝下錯誤 =====
add(73,
    summary="仰臥位手部擺放：「手掌朝上 (supinated) 或 thumb up (neutral)」為標準，避免尺神經受壓。「手掌朝地面 (pronated)」反而會「壓迫尺神經」。",
    mechanism="Ulnar nerve 走 cubital tunnel (內側肘部)。Pronation (手掌朝下) 時 ulnar nerve 易受 medial epicondyle 壓迫；Supination (手掌朝上) 或 neutral 保護神經。",
    options={
        "A": "錯誤 (本題錯誤)。手掌應「朝上 (supinated)」或 neutral，「不是朝地面 (pronated)」。",
        "B": "正確。Lateral 位 axillary roll 應在腋下「空隙」非腋下，避免 brachial plexus 壓迫。",
        "C": "正確。Lithotomy 應避免 common peroneal nerve at fibular head 壓迫。",
        "D": "正確。Prone 手部外展 > 90° 易 brachial plexus 損傷。",
    },
    guidelines=[
        "ASA Practice Advisory for Prevention of POVL 2019。",
        "ASA Practice Advisory for Prevention of Perioperative Peripheral Neuropathies 2018。",
    ],
    points=[
        "Common nerve injuries: ulnar (supine pronation)、 common peroneal (lithotomy)、 brachial plexus (lateral)",
        "POVL risk: prone、 long duration、 hypotension、 anemia",
        "Periodic position checks during long cases",
    ],
    keyword="Surgical positioning, ulnar nerve, supination",
    source="ASA Practice Advisories",
)

# ===== Q74 (B) Laryngospasm — NPPE 在「兒童青年」較多 =====
add(74,
    summary="Negative Pressure Pulmonary Edema (NPPE) 由「強壯的兒童/青年」inspiratory effort against closed glottis 引起，「不是虛弱老年人」。年輕健康肌力強者反而高風險。",
    mechanism="Laryngospasm + 強烈 inspiratory effort against closed glottis → markedly negative intrathoracic pressure → 增加 venous return + 肺微血管壓力 → fluid extravasation → pulmonary edema。年輕健康者肌力強，更易產生強烈 negative pressure。",
    options={
        "A": "正確。Jaw thrust + CPAP via tight mask 為標準。",
        "B": "錯誤 (本題錯誤)。NPPE「強壯青年」較多，「不是虛弱老人」。",
        "C": "正確。Propofol 0.5-1 mg/kg 加深麻醉、succinylcholine 0.1-0.5 mg/kg 解痙攣。",
        "D": "正確。拔管前常無症狀，拔管後 emerge stage 2 期間發生。",
    },
    guidelines=[
        "APAGBI Pediatric Difficult Airway 2015。",
        "PALS for severe desaturation。",
        "Prevention: smooth induction, avoid stage 2 manipulation, treat URI symptoms。",
    ],
    points=[
        "Larson's point: mandible behind earlobe",
        "Negative pressure pulmonary edema (NPPE) — post-laryngospasm complication",
        "URI symptoms: postpone elective surgery 2-4 wks",
    ],
    keyword="Laryngospasm, NPPE, young athletic",
    source="APAGBI Pediatric Difficult Airway 2015",
)

# ===== Q75 (B) Lethal triad — 不是低血氧 =====
add(75,
    summary="Trauma Lethal Triad：(1) 低體溫；(2) 代謝性酸中毒；(3) 凝血功能異常。「低血氧」「不屬」lethal triad (低血氧是 ABC 一部分，但非 triad 組成)。",
    mechanism="Hypothermia → enzyme function↓ → coagulation factor activity↓、 platelet dysfunction → coagulopathy。Hypoperfusion → anaerobic metabolism → lactic acidosis。三者互相惡化 → death spiral。",
    options={
        "A": "錯誤 (是 lethal triad 之一)。低體溫 < 35°C。",
        "B": "正確 (本題答案，不屬 lethal triad)。低血氧雖危險，但「不是 triad 組成」。",
        "C": "錯誤 (是 lethal triad 之一)。代謝性酸中毒 (lactate↑)。",
        "D": "錯誤 (是 lethal triad 之一)。Coagulopathy。",
    },
    guidelines=[
        "ATLS 10/e (2018) Damage Control Resuscitation。",
        "Permissive hypotension (SBP 80-90 unless TBI)、 1:1:1 transfusion、 TXA 1g within 3h、 active warming。",
    ],
    points=[
        "Active rewarming: warm fluids、 forced air warmer、 normothermia critical",
        "Massive transfusion protocol: 1:1:1 RBC:FFP:Platelet",
        "Tranexamic acid (CRASH-2)：within 3h",
    ],
    keyword="Lethal triad, hypothermia, acidosis, coagulopathy",
    source="ATLS 10/e Trauma Guidelines",
)

# ===== Q76 (A) 燒傷 — 48h 內可用 sux =====
add(76,
    summary="燒傷 「< 24-48 小時」內 succinylcholine 「仍可使用」(extrajunctional AChR up-regulation 尚未發生)。「> 24-48h 之後」才禁用 (high K release fatal)。題目說「48h 以內禁用」過於嚴格，為錯誤敘述。",
    mechanism="Burn → extrajunctional AChR up-regulation 需要時間 (24-48h 起逐漸明顯)。Succinylcholine 在受傷後極早期 (< 24h) 可用；之後直到 burn 完全癒合 + 1-2 年內為禁忌。",
    options={
        "A": "錯誤 (本題錯誤)。Sux 在燒傷「< 24-48h」內仍可用；「> 24h 後」才禁用。",
        "B": "正確。Severe burn 定義為 2°/3° > 20% TBSA。",
        "C": "正確。Parkland formula: 4 mL × kg × %TBSA over 24h。",
        "D": "正確。LR (balanced crystalloid) 較 NS 或 colloid 為偏好。",
    },
    guidelines=[
        "ABA (American Burn Association) Guidelines。",
        "燒傷對 nondepolarizing NMBA 有 resistance (受體增加 + 蛋白改變)，rocuronium 劑量需 ×2-3。",
        "Parkland formula: 4 mL × kg × %TBSA over 24h (1st half in 8h、 2nd half 16h)；LR preferred。",
        "Airway: 嚴重 face/neck burn 24h 內可快速 swelling，早期 prophylactic intubation。",
    ],
    points=[
        "Rocuronium dose ↑ 2-3× due to receptor up-regulation",
        "Hypermetabolic state weeks-months post-burn (high glucose、 protein turnover)",
        "Multiple operations + skin grafts over time",
    ],
    keyword="Burn anesthesia, succinylcholine timing, AChR upregulation",
    source="ABA Burn Guidelines; Miller's 8/e Ch. 81",
)

# ===== Q77 (A) MH — N2O 不是誘發因子 =====
add(77,
    summary="MH 誘發因子：「succinylcholine + 揮發性麻醉劑 (halothane、 isoflurane、 sevoflurane、 desflurane)」。「N₂O (笑氣) 不是 MH trigger」，為安全藥物。",
    mechanism="Volatile anesthetics + succinylcholine 觸發 RYR1 mutation 之 SR Ca²⁺ uncontrolled release。N₂O 不影響 RYR1，可安全用於 MH-susceptible 病人 (常用於 MH-safe anesthetic + TIVA)。",
    options={
        "A": "錯誤 (本題錯誤)。N₂O「不是 MH trigger」；可在 MH-susceptible 病人安全使用。",
        "B": "正確。早期症狀：tachycardia、 muscle rigidity (especially masseter)、ETCO₂↑。",
        "C": "正確。Hyperthermia → hyperkalemia → metabolic acidosis → multiorgan failure。",
        "D": "正確。Dantrolene (Dantrium) 為粉末，需 60 mL sterile water 配製 (Ryanodex 新型快速配製)。",
    },
    guidelines=[
        "MHAUS Protocol 2018：Dantrolene + supportive care + ICU。",
        "MHAUS Hotline: 1-800-MH-HYPER。",
        "Family screening: caffeine-halothane contracture test (CHCT) or genetic testing。",
    ],
    points=[
        "Ryanodex (new formulation) — quicker mixing (vs traditional Dantrium powder)",
        "ETCO₂ rise often earliest sign — even before hyperthermia",
        "Continue dantrolene infusion 24h after stabilization (recurrence)",
    ],
    keyword="Malignant hyperthermia, N2O, trigger agents",
    source="MHAUS Protocol 2018",
)

# ===== Q78 (B) PONV — 女 > 男 =====
add(78,
    summary="PONV 危險因子 (Apfel score)：女性、 不抽菸、 PONV/暈車病史、 術後 opioid。「女性 > 男性」(female 是 risk factor)，題目敘述「男性 > 女性」為錯誤。",
    mechanism="PONV 多因素：vestibular、 chemoreceptor trigger zone、 cortical、 GI。Volatile anesthetic、 opioid、 N₂O、 surgery type 都貢獻。女性 PONV 風險 2-3 倍於男性。",
    options={
        "A": "正確 (是事實)。年輕 > 老年 (老年 PONV 較少)。",
        "B": "錯誤 (本題錯誤)。PONV「女 > 男」，非男 > 女。",
        "C": "正確 (是事實)。不抽菸 > 抽菸 (吸菸者 PONV 風險低)。",
        "D": "正確 (是事實)。Sevoflurane (volatile) > propofol (anti-emetic property)。",
    },
    guidelines=[
        "SAMBA 4th Consensus Guidelines for Management of PONV 2020。",
        "Apfel Score: ≥ 2 risk factors → ≥ 2 prophylactic agents。",
        "High-risk surgery: gynecologic、 laparoscopic、 strabismus、 ENT。",
    ],
    points=[
        "TIVA propofol 較 volatile 低 PONV",
        "Adequate hydration、 minimize opioid (multimodal)、 regional anesthesia",
        "Rescue antiemetic: different class from prophylaxis",
    ],
    keyword="PONV, Apfel score, female, antiemetic",
    source="SAMBA 4th Consensus 2020",
)

# ===== Q79 (A) 肝移植 reperfusion 較不會 — 肺水腫 =====
add(79,
    summary="肝移植 reperfusion 階段「較不會出現大量血液回流肺水腫」(主要因素為 hypotension、hyperkalemia、 acidosis、 hypothermia)。Pulmonary edema 可能但非典型 reperfusion syndrome 表現。",
    mechanism="Liver transplant reperfusion: re-clamp release → cold preservation solution + 蓄積 lactate、K⁺ 等 vasoactive substances → 系統 hypotension + bradycardia + hyperkalemia + acidosis + hypothermia + 可能 cardiac arrest。",
    options={
        "A": "正確 (本題答案，較不會)。腹腔器官血液大量回流肺水腫「不是」reperfusion 典型表現。",
        "B": "錯誤 (會發生)。Preservation solution 含高 K + cold ischemia → hyperkalemia。",
        "C": "錯誤 (會發生)。冰冷保存液 → systemic hypothermia。",
        "D": "錯誤 (會發生)。Lactate、CO₂、acid 累積 → metabolic acidosis。",
    },
    guidelines=[
        "ISMETT / Liver Transplant Anesthesia Consensus。",
        "Pre-reperfusion: hyperventilate、 increase preload、 calcium、 bicarbonate、 vasopressor preparation。",
        "Post-reperfusion syndrome: > 30% MAP drop, lasting > 1 min。",
    ],
    points=[
        "Veno-veno bypass vs piggyback technique reduce caval clamp issues",
        "Coagulopathy management: TEG-guided product replacement",
        "Post-op ICU: graft function monitoring, immunosuppression",
    ],
    keyword="Liver transplant, reperfusion syndrome",
    source="ISMETT Liver Transplant Anesthesia",
)

# ===== Q80 (D) 腦死器捐 — 補糖錯誤 =====
add(80,
    summary="腦死器捐病人血糖目標應「< 180 mg/dL」 (避免 hyperglycemia 引起 osmotic diuresis、 graft dysfunction)。「< 250 mg/dL 為可接受」過寬，「補糖」為錯誤。",
    mechanism="腦死 → 失去 pituitary function → DI、 thyroid、 cortisol 失衡。Hyperglycemia 常見 (stress、 catecholamine、 steroid)，引起 osmotic diuresis 加重脫水、 影響 graft function。血糖應嚴格控制 < 180 mg/dL，「補糖」反而有害。",
    options={
        "A": "正確。輕度低體溫 34-35°C 可接受 (預防全身缺血損傷)。",
        "B": "正確。類固醇 (methylprednisolone 15 mg/kg) 改善肺功能、減少發炎。",
        "C": "正確。Voluven (HES) 有 AKI 風險，腎捐贈避免。",
        "D": "錯誤 (本題錯誤)。血糖應「< 180 mg/dL」嚴格控制；「補糖 + 250 mg/dL 可接受」為錯誤。",
    },
    guidelines=[
        "OPTN/UNOS Organ Procurement Protocols。",
        "Hormonal replacement therapy: T4 20 µg IV bolus + 10 µg/h infusion、 methylprednisolone 15 mg/kg、 vasopressin 1 U bolus + infusion 0.5-4 U/h、 insulin。",
        "Maintain physiologic parameters until organ retrieval。",
    ],
    points=[
        "Brain death determination: clinical + apnea test + ancillary (per local law)",
        "Spinal reflexes can occur — not signs of brain function",
        "Family communication and consent timing critical",
    ],
    keyword="Brain death, organ donation, glucose control",
    source="OPTN/UNOS Protocols; Miller's 8/e Ch. 82",
)

# Apply enhancements
with open('/tmp/np-anesthesia/questions.json') as f:
    qs = json.load(f)

updated = 0
for q in qs:
    if q['year'] != 114 or q['specialty'] != 'anesth_advanced':
        continue
    n = int(re.search(r'-A(\d+)$', q['id']).group(1))
    if n in E:
        q['explanation'] = E[n]
        # Update source from enhancement
        if 'source' in E[n]:
            q['source'] = E[n]['source']
        updated += 1

print(f"Enhanced {updated}/80 questions")

with open('/tmp/np-anesthesia/questions.json', 'w') as f:
    json.dump(qs, f, ensure_ascii=False, separators=(',', ':'))

import os
print(f"File size: {os.path.getsize('/tmp/np-anesthesia/questions.json')/1024:.0f}KB")
