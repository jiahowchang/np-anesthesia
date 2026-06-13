#!/usr/bin/env python3
"""Rebuild detailed explanations for 113 進階麻醉 80 questions based on verified official answers."""
import json, re

E = {}
def add(n, summary, mechanism, options, guidelines, points, keyword, source):
    E[n] = {"summary": summary.strip(), "mechanism": mechanism.strip(),
            "options": options, "guidelines": guidelines, "points": points,
            "keyword": keyword.strip(), "source": source.strip()}

# Q1 (B) 登革熱
add(1, summary="登革熱典型抽血變化：「血小板下降 (thrombocytopenia)」、WBC ↓ (leukopenia)、Hct ↑ (haemoconcentration)、肝酵素 ↑。",
    mechanism="登革病毒感染巨核細胞 + 抗體介導之 platelet destruction → thrombocytopenia (常 < 100K)；血漿外滲 → Hct 上升、albumin 下降；發燒期 4-7 天後進入危險期 (warning signs)。",
    options={"A":"錯誤。登革熱表現 leukopenia 非增加。","B":"正確。Thrombocytopenia 為經典與診斷標誌。","C":"錯誤。血漿外滲使 albumin「下降」。","D":"錯誤。ESR 可能上升或無顯著變化，非診斷重點。"},
    guidelines=["WHO 2009 Dengue Classification：dengue without/with warning signs、severe dengue。","台灣 CDC：NS1 抗原 (4 天內) + IgM/IgG (5 天後) 為診斷血清學。","警示徵：腹痛、嘔吐、出血、Hct↑伴 plt↓、嗜睡躁動。"],
    points=["重症登革熱：plasma leakage→shock；嚴重出血；器官衰竭","支持治療為主；輸液避免過量；避免 NSAIDs/aspirin (出血)","退燒首選 acetaminophen"],
    keyword="Dengue fever, thrombocytopenia, NS1",
    source="WHO Dengue Guidelines 2009; CDC Taiwan")

# Q2 (C) 高血鉀 EKG (圖)
add(2, summary="高血鉀典型 EKG 變化依序：peaked T wave → PR 延長 / P 波變平 → QRS 變寬 → sine wave → VF/asystole。本題選項 C 為高血鉀典型圖形。",
    mechanism="K↑ → 細胞外/細胞內 K 比降 → 靜止膜電位上升 (less negative) → Na channel 失活 → 傳導減慢 + 動作電位短化 → peaked T、wide QRS、sine wave。",
    options={"A":"錯誤。其他 EKG 變化 (e.g. 正常竇性、AF 等)，非高鉀典型。","B":"錯誤。","C":"正確 (本題答案)。Peaked T wave + wide QRS 為高鉀典型圖形。","D":"錯誤。"},
    guidelines=["KDIGO 2020 Hyperkalemia：K > 6.5 + EKG changes 立即 Ca gluconate 1g IV 穩定心肌。","ACLS：嚴重高鉀考慮 emergency dialysis。"],
    points=["Ca gluconate 穩定心肌但不降鉀","Shift: insulin/D50、β2-agonist、HCO₃","Remove: Kayexalate (slow)、loop diuretic、dialysis"],
    keyword="Hyperkalemia, peaked T wave, sine wave",
    source="KDIGO 2020 Hyperkalemia; ACLS Guidelines")

# Q3 (C) 低血鈉鑑別
add(3, summary="低血鈉鑑別應用「血清滲透壓」(分 hypo/iso/hyper-osmolar)、「尿液滲透壓」(評估 ADH 活性) 與「尿液鈉離子」(評估 volume status 或 SIADH)。「血鉀」非鑑別重點。",
    mechanism="低血鈉診斷流程：① 血清 osmolality 區分 true (低) vs pseudohyponatremia；② 尿 osmolality 區分 ADH-mediated (>100) vs primary polydipsia (<100)；③ urine Na 區分 hypovolemic (Na<20) vs euvolemic/SIADH (Na>40)。",
    options={"A":"錯誤。①②③：缺少血清滲透壓。","B":"錯誤。包含血鉀但缺尿鈉。","C":"正確 (本題答案)。①②④：尿鈉、尿滲透壓、血清滲透壓為三大鑑別工具。","D":"錯誤。"},
    guidelines=["European Society 2014 Hyponatremia Guidelines：基於 osmolality + volume status 流程。","SIADH 診斷：低 Na + 高 urine osmolality + 高 urine Na + euvolemia + 正常腎/腎上腺/甲狀腺。"],
    points=["急性 (<48h) 症狀性 hyponatremia：可較快矯正 (避免 cerebral edema)","慢性 hyponatremia：矯正 ≤ 8 mEq/L/24h 防 ODS (osmotic demyelination)","治療：水分限制 (SIADH)、3% saline (severe)、vaptan"],
    keyword="Hyponatremia, urine osmolality, urine sodium",
    source="ESI/ERA-EDTA Hyponatremia Guidelines 2014")

# Q4 (A) Neutropenic FUO
add(4, summary="絕對嗜中性白血球 < 500/mm³ + FUO = neutropenic FUO。FUO 分類：classic、nosocomial、neutropenic、HIV-associated。本題 ANC 250 顯著低於 500 屬 neutropenic FUO。",
    mechanism="Neutropenic patient (chemo、bone marrow disease) 防禦力低下 → 反覆 fever 多為機會性感染或菌血症。處置：empiric broad-spectrum antibiotic (e.g. cefepime、piperacillin-tazobactam) within 1 hr。",
    options={"A":"正確 (本題答案)。ANC 250 < 500 + FUO = neutropenic FUO。","B":"錯誤。Nosocomial FUO 需住院 ≥ 24h 入院時無 fever。","C":"錯誤。HIV-associated 需 HIV 證據。","D":"錯誤。Viral 為 specific cause 非 FUO category。"},
    guidelines=["IDSA Neutropenic Fever Guidelines 2010：empiric anti-pseudomonal β-lactam within 1 hr。","Durack/Street 修訂 FUO 分類：classic > 3 wks/3 visits、nosocomial、neutropenic、HIV。"],
    points=["MASCC score 評估 outpatient management 適合性","48-72h 無改善 + persistent fever → add antifungal (echinocandin)","Source identification 重要 — CT、blood culture、line evaluation"],
    keyword="Neutropenic FUO, empiric antibiotic",
    source="IDSA Neutropenic Fever Guidelines 2010")

# Q5 (B) 體溫過高
add(5, summary="體溫 > 41.5°C 為 hyperpyrexia，常見於 CNS 病變 (出血、感染、惡性高熱)。Hyperpyrexia 定義為 ≥ 41.5°C 非 39°C。",
    mechanism="Hypothalamus set point 改變產生 fever；CNS 出血、中樞性 hyperthermia (loss of thermoregulation)、heat stroke 為超高溫原因。體溫散熱主要透過 sweating、 vasodilation。",
    options={"A":"錯誤。Hyperpyrexia 為 ≥ 41.5°C，非 39°C。","B":"正確 (本題答案)。CNS 出血常見 hyperpyrexia。","C":"錯誤。發燒透過皮膚 vasodilation + sweating + respiration 散熱，非肌腎代謝。","D":"錯誤。Heat stroke 為 thermoregulation failure，acetaminophen 無效；需 active cooling。"},
    guidelines=["Heat stroke：core temp > 40°C + CNS dysfunction → cold water immersion、 fans、 ice packs。","WHO Fever Definition: oral ≥ 38°C；hyperpyrexia ≥ 41.5°C。"],
    points=["MH 屬 hypermetabolic state，需 Dantrolene","Heat stroke vs fever：fever 屬調節異常、heat stroke 屬調節失敗","NSAIDs/acetaminophen 對 heat stroke 無效"],
    keyword="Hyperpyrexia, heat stroke, CNS bleeding",
    source="Harrison's Internal Medicine; WHO Fever")

# Q6 (B) 退燒藥 — Acetaminophen
add(6, summary="慢性胃炎 + thrombocytopenia 病人退燒「首選 acetaminophen」(無 GI/出血副作用)。NSAIDs (aspirin、ibuprofen、naproxen) 因抑制 COX 與 platelet 功能皆禁忌。",
    mechanism="Acetaminophen：中樞作用 (COX-3?)，無顯著周邊 COX 抑制 → 無 GI 出血、無 platelet 抑制。NSAIDs 抑制 COX-1 → GI 黏膜保護下降 + platelet TXA2 ↓ 影響止血。",
    options={"A":"錯誤。Aspirin 為 irreversible COX inhibitor，加重出血。","B":"正確 (本題答案)。Acetaminophen 無 GI/出血副作用為首選。","C":"錯誤。Ibuprofen 為 NSAID，禁忌。","D":"錯誤。Naproxen 為 NSAID，禁忌。"},
    guidelines=["WHO Pain Ladder: paracetamol/NSAIDs as Step 1。","Acetaminophen max 4g/day (健康成人)、2g/day (肝病、酒精)。"],
    points=["Acetaminophen 過量 (>10g) → 急性肝衰竭，N-acetylcysteine 為解藥","NSAIDs 禁忌：GI bleed、平台 < 50K、 active bleeding、 renal failure","Reye syndrome：兒童病毒感染避免 aspirin"],
    keyword="Acetaminophen, thrombocytopenia, NSAID contraindication",
    source="WHO Pain Ladder; AAP/Stoelting's 7/e")

# Q7 (A) 細菌性腦膜炎
add(7, summary="CSF 表現：「混濁、pressure↑、WBC 10000 多核球為主、glucose 大幅下降、protein 顯著上升」= 典型細菌性腦膜炎。立即 empiric AB + dexamethasone。",
    mechanism="細菌感染 → 強烈嗜中性球反應 (neutrophilic pleocytosis)、 glucose 消耗、 protein leakage。Viral 為 lymphocytic、 glucose 正常；TB/fungal 為 lymphocytic + glucose 低 + protein 中等。",
    options={"A":"正確 (本題答案)。多核球 + 葡萄糖大幅↓ + protein↑↑ = bacterial。","B":"錯誤。TB 為 lymphocytic、 glucose 中等下降、 protein 中等上升、慢性進展。","C":"錯誤。Fungal (Cryptococcus) 類似 TB 但 latex agglutination 確診。","D":"錯誤。Viral 為 lymphocytic、 glucose 正常、 protein 輕微上升。"},
    guidelines=["IDSA Bacterial Meningitis Guidelines 2004：empiric AB 依年齡 (ceftriaxone + vancomycin + ampicillin if > 50y or immunocompromised)。","Dexamethasone 0.15 mg/kg q6h × 4 days 對成人肺炎鏈球菌腦膜炎降死亡率。","LP 前若無神經 deficits/papilledema 可不必先 CT。"],
    points=["三主徵 (fever + neck stiffness + AMS) 敏感度約 40%","Kernig、Brudzinski sign 較不敏感","Empiric AB 應在 LP 後 1 小時內給"],
    keyword="Bacterial meningitis, CSF analysis, ceftriaxone",
    source="IDSA Bacterial Meningitis Guidelines 2004")

# Q8 (C) 副甲狀腺切除 — 低血鈣
add(8, summary="副甲狀腺切除後 PTH 突降 → 血鈣下降 → Chvostek's sign (顏面神經敲擊) 與 Trousseau's sign (袖帶充氣 3 分後手痙攣) = 低血鈣 tetany 表現。",
    mechanism="PTH 維持血鈣 (osteoclast、 腎臟保鈣、 vitamin D 活化)。Total or subtotal parathyroidectomy → PTH↓ → Ca↓。Hypocalcemia 引起神經肌肉 hyperexcitability、 QT 延長、 tetany。",
    options={"A":"錯誤。Hypokalemia 引起 muscle weakness、 arrhythmia，非 tetany。","B":"錯誤。Hyperkalemia 引起 muscle weakness、 cardiac arrest。","C":"正確 (本題答案)。低血鈣為 Chvostek/Trousseau 經典原因。","D":"錯誤。Hypercalcemia 引起 stones、 bones、 groans、 psychiatric overtones，不為 tetany。"},
    guidelines=["Endocrine Society：post-thyroidectomy/parathyroidectomy 監測 Ca、 PTH。","Severe hypocalcemia (symptomatic 或 Ca < 7.5 mg/dL)：IV calcium gluconate 1-2g over 10-20 min + maintenance infusion。"],
    points=["Hungry bone syndrome：副甲狀腺切除後嚴重低 Ca + 低 Mg + 低 P","Vitamin D + Mg 同時補充","Permanent hypoparathyroidism：< 5% 經驗醫師中"],
    keyword="Hypocalcemia, Chvostek's sign, Trousseau's sign, parathyroidectomy",
    source="Endocrine Society Hypocalcemia Guidelines")

# Q9 (A) DKA 處置
add(9, summary="23 歲女性嘔吐、 BP 90/48、 HR 135、 血糖 585、 anion gap 高 + pH 7.14 + HCO₃ 8 = DKA。「應 ICU 嚴密監測」(此題選項「一般病房 + 嚴密追蹤」實為正確 — 雖然嚴重 DKA 應 ICU，但答案 A 強調監測重要性)。",
    mechanism="DKA：insulin 不足 → lipolysis → ketogenesis → ketone (β-hydroxybutyrate、 acetoacetate) → AG metabolic acidosis。Treatment：fluid + insulin + K replacement + glucose monitoring。",
    options={"A":"正確 (本題答案)。DKA 病人需密集監測 (V/S、 血糖 q1h、 K、 ABG q2-4h)。","B":"錯誤。DKA 必定 AG 上升 (ketone 為 anion)。","C":"錯誤。NaHCO₃ 非常規 (僅 pH < 6.9 考慮)；可能加重 hypokalemia。","D":"錯誤。Insulin 應持續 + 加 D5 維持血糖 150-200，不應停 insulin (否則 ketogenesis 復發)。"},
    guidelines=["ADA DKA Management：(1) IV fluid (NS 1L first hour、 then 0.45% NS);(2) Insulin infusion 0.1 U/kg/h after K > 3.3;(3) K replacement 早期;(4) 血糖 250-300 加 D5。","Bicarbonate only if pH < 6.9。"],
    points=["AG = Na - (Cl + HCO₃)；DKA AG 通常 20-30+","K 補充：K < 3.3 先 K (停 insulin) → K 3.3-5.0 同時 insulin + K → K > 5.0 暫不補","DKA 引發：infection、 missed insulin、 MI、 stroke"],
    keyword="DKA, anion gap, insulin infusion",
    source="ADA Standards of Medical Care in Diabetes")

# Q10 (D) Fentanyl 機制
add(10, summary="Fentanyl 為 μ-opioid receptor agonist，作用於 CNS (脊髓 dorsal horn + supraspinal) → 抑制 pain transmission。Transdermal patch 提供持續釋放適合 chronic cancer pain。",
    mechanism="μ-opioid receptor → G-protein coupled → inhibits adenyl cyclase → cAMP↓ → presynaptic Ca channel 抑制 + postsynaptic K channel 活化 → neuronal hyperpolarization → 抑制 neurotransmitter release (substance P、 glutamate)。",
    options={"A":"錯誤。Na channel inhibition 為 local anesthetic 機制。","B":"錯誤。NMBA (e.g. succinylcholine、 rocuronium) 作用於 NMJ。","C":"錯誤。Benzodiazepine 增強 GABA-A。","D":"正確 (本題答案)。μ-opioid receptor 是 fentanyl 主要作用點。"},
    guidelines=["WHO Pain Ladder Step 3：strong opioid for severe cancer pain。","Transdermal fentanyl：25 µg/h ≈ oral morphine 60 mg/day；onset 12-24h、 duration 72h。"],
    points=["副作用：respiratory depression、 nausea/vomiting、 constipation、 sedation、 dependence","劑量轉換需注意各 opioid equivalence","Fentanyl lollipop / spray 用於 breakthrough pain"],
    keyword="Fentanyl, μ-opioid receptor, transdermal patch",
    source="WHO Cancer Pain Guidelines; Stoelting's Pharmacology 5/e")

# Q11 (A) 安寧緩和 — 喉頭咕嚕聲
add(11, summary="末期病人「Death rattle」(死前喉頭咕嚕聲) 由於唾液 + 分泌物在 oropharynx 與意識下降 + 吞嚥反射喪失而產生。處置：scopolamine、 glycopyrrolate 減少分泌物 + 家屬說明。",
    mechanism="Terminal phase 意識下降 + 吞嚥反射消失 → secretions 在 hypopharynx 隨呼吸氣流震動 → 「咕嚕」聲。聽起來不舒服但通常病人本身無 distress。",
    options={"A":"正確 (本題答案)。喉肌鬆弛 + 無效吞嚥 = 唾液積聚震動聲。","B":"錯誤。PAIN: P=palliative/provocative、 A=quality、 I=intensity、 N=non-pharmacological — 此為 PQRST 不同記憶法。","C":"錯誤。Ascites 通常需 ≥ 500-1000 mL 才能 US 偵測，clinical 需 ≥ 1500 mL。","D":"錯誤。Cheyne-Stokes 為「漸深漸快 → 漸淺漸慢 → 短暫呼吸停止」週期，題目敘述相反。"},
    guidelines=["EAPC Palliative Care Guidelines：death rattle 處置 scopolamine 0.4 mg SQ 或 glycopyrrolate。","Anticipatory grief support 對家屬重要。"],
    points=["Death rattle 對家屬比病人困擾更大","體位 (lateral) 可幫助減少分泌物積聚","減少 IV fluid 可降低 secretions"],
    keyword="Death rattle, terminal care, hospice",
    source="EAPC Palliative Care Guidelines")

# Q12 (B) 骨頭轉移 — Calcitonin
add(12, summary="癌症骨轉移引起的骨痛輔助止痛：「Calcitonin」抑制 osteoclast 活性、減少骨重塑 + 中樞鎮痛機制。其他選項主要用於 neuropathic pain (TCA、 anticonvulsant)、發炎性疼痛 (steroid)。",
    mechanism="Calcitonin (salmon-derived) 抑制 osteoclast → 減少骨吸收、 釋放鈣、 prostaglandin → 減輕骨痛。中樞作用機制可能透過 serotonin 與 endogenous opioid 系統。",
    options={"A":"錯誤。TCA 用於 neuropathic pain (burning、 shooting)，非骨痛首選。","B":"正確 (本題答案)。Calcitonin 為骨痛輔助止痛。","C":"錯誤。Anticonvulsant (gabapentin、 pregabalin) 用於 neuropathic pain。","D":"錯誤。Steroid 對骨痛有效 (尤其 spinal cord compression)，但長期副作用多。"},
    guidelines=["WHO Pain Ladder Step 3 + adjuvants for bone pain。","Bisphosphonate (zoledronate) + denosumab 為現代主要骨痛/SRE 預防藥物。","Radiotherapy 為 localized bone metastasis 第一線。"],
    points=["Bone metastasis 多為 lytic (multiple myeloma、 breast、 lung) 或 blastic (prostate)","Hypercalcemia of malignancy 同時處理","Opioid + NSAID + adjuvant 多模式"],
    keyword="Bone pain, calcitonin, bisphosphonate",
    source="WHO Cancer Pain Guidelines; ASCO Guidelines")

# Q13 (C) Free air — Bowel perforation
add(13, summary="80 歲 DM + HTN + CVA + 急性腹痛 + 左側臥 KUB 顯示「橫膈下 free air」= 腹腔積氣 (pneumoperitoneum)，提示「中空臟器破裂」(perforated viscus，最常見 perforated peptic ulcer)。",
    mechanism="Hollow viscus perforation → 氣體進入 peritoneal cavity → upright/decubitus 影像橫膈下見 free air。Left lateral decubitus 為老年/臥床病人偵測 free air 之首選 (右側肝陰影對比氣體)。",
    options={"A":"錯誤。腹水為 fluid 影像不是 free air。","B":"錯誤。Bowel obstruction 為 distended loops + air-fluid levels，不是 free air。","C":"正確 (本題答案)。Free air 提示中空臟器破裂，需立即手術。","D":"錯誤。Free air 為異常 emergency finding，非正常影像。"},
    guidelines=["WSES Perforated Peptic Ulcer Guidelines：emergency surgery + broad-spectrum AB。","CT 較 X-ray 敏感 (90% vs 50-70%)。"],
    points=["最常見 perforation 部位：duodenum (NSAID/aspirin、 H. pylori)","老年人 perforation 死亡率高 (30%+)","麻醉考量：full stomach、 RSI、 sepsis、 大量輸液"],
    keyword="Pneumoperitoneum, perforated viscus, free air",
    source="WSES Perforated Peptic Ulcer Guidelines; Sabiston Surgery")

# Q14 (B) Boerhaave / 胃內容物外漏
add(14, summary="化療 + 嚴重嘔吐後左胸痛 + 胸水顯示「low glucose、 high amylase (380)、 neutrophil 80%」= Boerhaave syndrome (食道破裂) 或 chemotherapy 引起 esophageal perforation。處置「胸管引流 + 禁食」+ broad AB。",
    mechanism="嚴重嘔吐 → 食道內壓上升 → distal esophagus rupture (Boerhaave)。胃液 (酸性 + 含 amylase) 漏入 pleural space → empyema/mediastinitis。低 glucose + 高 amylase + neutrophil 為 esophageal perforation 典型 pleural effusion 表現。",
    options={"A":"錯誤。TB pleural effusion 為 lymphocytic、 adenosine deaminase 高、 amylase 不高。","B":"正確 (本題答案)。Esophageal rupture 治療：drainage、 NPO、 IV nutrition、 surgery/stent、 broad AB。","C":"錯誤。Chest pain 不是 angina，NTG 無效。","D":"錯誤。利尿劑對 effusion 從食道漏出無效。"},
    guidelines=["Mortality 為 esophageal rupture 高 (25-50%)，依 timely diagnosis。","CT with oral contrast 為主要影像。"],
    points=["Mackler triad：vomiting + chest pain + subcutaneous emphysema","早期 (<24h) surgical primary repair 預後較好","Esophageal stent 為 alternative for late presentations"],
    keyword="Boerhaave syndrome, esophageal perforation, pleural effusion",
    source="Sabiston Surgery; ACG Guidelines")

# Q15 (B) ACS — CK-MB
add(15, summary="現代 NSTEMI 診斷「Troponin 為主」，CK-MB 已退居輔助 (因 troponin 敏感度與特異度都高、可早期偵測)。「CK-MB 為 NSTEMI 初步診斷之良好指標」為不適當敘述。",
    mechanism="Troponin (cTnI/cTnT) 為心肌專一蛋白，AMI 後 3-6h 開始上升、 12-24h 高峰、 5-14 天恢復。CK-MB 在 4-6h 上升、 24h 高峰、 48-72h 恢復 — 對 re-infarction 較有用。",
    options={"A":"正確。Troponin 為心肌損傷 gold standard。","B":"錯誤 (本題不適當)。CK-MB 已被 troponin 取代為 first-line。","C":"正確。BNP↑ 在 ACS 預後較差 (more LV dysfunction)。","D":"正確。CK-MB 半衰期短，適合追蹤 re-infarction (troponin 半衰期長不適合)。"},
    guidelines=["ESC/AHA NSTEMI Guidelines：High-sensitivity troponin 為首選；CK-MB 已不推薦。","Type 1 (atherosclerotic) vs Type 2 (supply-demand mismatch) MI。"],
    points=["Troponin elevation 鑑別：MI、 myocarditis、 PE、 sepsis、 CKD、 heart failure","HEART Score、 TIMI、 GRACE 為風險分層","DAPT (aspirin + ticagrelor/prasugrel) 為標準治療"],
    keyword="Troponin, CK-MB, NSTEMI",
    source="ESC/AHA NSTEMI Guidelines")

# Q16 (D) Complete AV block (圖)
add(16, summary="EKG 圖 P 波獨立於 QRS、 atrial 與 ventricular rate 各自 regular 但無關聯 = Complete AV block (third-degree AV dissociation)。需 transcutaneous pacing → permanent pacemaker。",
    mechanism="AV node 或 His-Purkinje 完全阻斷 → atria 與 ventricles 各自為政；ventricular escape rhythm (junctional 40-60、 ventricular 20-40 bpm)。",
    options={"A":"錯誤。First-degree：PR > 200ms 但每 P 跟 QRS。","B":"錯誤。Mobitz I：PR 漸長後 dropped。","C":"錯誤。Mobitz II：PR 固定、 間歇 dropped。","D":"正確 (本題答案)。Complete AV block：P 與 QRS 完全 dissociated。"},
    guidelines=["ACC/AHA/HRS 2018 Bradycardia：symptomatic AV block 為 permanent pacemaker class I。","Atropine 對 infranodal block 效果有限。"],
    points=["完全 AV block 常見於 inferior MI (RCA territory)、 calcific 退化、 Lyme","暫時 transcutaneous pacing 為急救","Permanent pacemaker：DDD/VVI 依需求"],
    keyword="Complete AV block, third degree, pacemaker",
    source="ACC/AHA/HRS 2018 Bradycardia Guidelines")

# Q17 (D) 孕婦 DKA
add(17, summary="孕婦 DKA 處置原則「與非孕婦相同」(fluid + insulin + K + glucose monitoring)。孕婦 DKA 可發生於較低血糖 (<200) — 因 pregnancy 增加 ketogenesis。",
    mechanism="孕婦 insulin resistance 增加 + accelerated starvation ketogenesis → 較易在較低血糖出現 DKA。胎兒在 DKA 期間 acidosis 風險高，但矯正母體 acidosis 對胎兒有益。",
    options={"A":"錯誤。孕婦 DKA 可發生於血糖 <200，不能以血糖排除。","B":"錯誤。DKA 急性期不引產，先穩定母體 (穩定後再評估)。","C":"錯誤。應矯正 pH 與酸中毒，胎兒受益於母體穩定。","D":"正確 (本題答案)。孕婦 DKA 治療原則與非孕婦相同。"},
    guidelines=["ACOG Guidelines：孕婦 DKA 緊急處理，monitor 胎兒、 母體血糖、 ABG、 K、 electrolyte。","Continuous fetal monitoring during DKA management。"],
    points=["孕婦 DKA 死亡率 ~1%；胎兒死亡率 9-35%","Diabetic ketoacidosis in pregnancy 較易發生於 T1DM、 GDM 罕見","誘因：感染、 missed insulin、 medication (steroid、 β-mimetics)"],
    keyword="DKA in pregnancy, euglycemic DKA",
    source="ACOG Practice Bulletin; ADA Standards")

# Q18 (C) 肝功能 — ALP、 AST/ALT
add(18, summary="③ ALP 在肝、 腎、 腸、 骨均可偵測；④ AST/ALT 在肝損傷上升、 AST 在 rhabdomyolysis 也升 — 為正確。①AFP 對肝癌敏感度約 60-65% (不是 90%+)；②溶血性貧血為 indirect bilirubin 上升 (非 direct)。",
    mechanism="ALP isoenzymes 來自不同組織；GGT 同時上升提示肝源。AST 存在心、肝、骨骼肌、 RBC；ALT 較肝特異。Hemolysis：unconjugated bili → indirect 上升。",
    options={"A":"錯誤。①②均錯。","B":"錯誤。②錯：溶血為 indirect。","C":"正確 (本題答案)。③④均對。","D":"錯誤。①錯：AFP 對 HCC 敏感度 60-65%，不到 90%。"},
    guidelines=["AASLD HCC Surveillance：US + AFP 每 6 月 (高風險族群)。","AFP > 200 ng/mL 高度懷疑 HCC；AFP > 400 ng/mL 即診斷 (有 chronic liver disease)。"],
    points=["Cholestatic pattern：ALP > 2×ULN + GGT↑","Hepatocellular pattern：AST/ALT > 2×ULN","R ratio = (ALT/ULN) / (ALP/ULN) > 5 hepatocellular, < 2 cholestatic"],
    keyword="ALP, AST/ALT, hepatic function, AFP",
    source="AASLD HCC Guidelines; Harrison's")

# Q19 (D) Unstable VT → 同步整流
add(19, summary="心跳 154 + BP 80/50 + 意識改變 = unstable wide-complex tachycardia (assumed VT)。「立即 synchronized cardioversion 120J」為 ACLS 標準處置。",
    mechanism="Unstable tachycardia (hypotension、 AMS、 chest pain、 heart failure) → 不論 mechanism 立即 synchronized cardioversion。Adenosine 僅用於 stable narrow QRS。",
    options={"A":"錯誤。β-blocker 在 hypotension 為禁忌。","B":"錯誤。Adenosine 用於 stable narrow QRS PSVT；wide QRS 不適合。","C":"錯誤。Inotrope 不解決 arrhythmia。","D":"正確 (本題答案)。Unstable wide QRS → synchronized cardioversion 120-200J biphasic。"},
    guidelines=["AHA ACLS Tachycardia Algorithm：Unstable → cardioversion；Stable wide → amiodarone or procainamide。","Polymorphic VT (Torsades) → unsynchronized defibrillation。"],
    points=["Synchronized 避免 R-on-T VF","Sedation if conscious (etomidate、 propofol)","Post-cardioversion monitor + treat underlying cause"],
    keyword="VT, synchronized cardioversion, ACLS",
    source="AHA 2020 ACLS Guidelines")

# Q20 (B) Neurogenic shock
add(20, summary="跳水後 SCI + 乳頭以下感覺運動喪失 + BP 70/40 + HR 40 + 暖週邊 = neurogenic shock (high spinal cord injury → 交感神經 outflow 喪失 → vasodilation + bradycardia)。",
    mechanism="High spinal cord injury (T6 以上) → 失去 sympathetic outflow (T1-L2) → 血管擴張 + 失去代償 tachycardia + 暖週邊。BP↓ + HR↓ + 暖週邊為 neurogenic shock 經典三聯。",
    options={"A":"錯誤。腦幹出血 (Cushing reflex) 為高血壓 + bradycardia + 呼吸異常。","B":"正確 (本題答案)。SCI 引起 sympathetic loss → neurogenic shock。","C":"錯誤。胸腔出血為 cold shock + tachycardia (代償)。","D":"錯誤。Drowning 引起 cardiogenic shock 罕見且不符。"},
    guidelines=["ATLS Spinal Cord Injury：early stabilization + fluid + vasopressor (norepinephrine for vasodilation)。","Target MAP > 85 for 7 days 改善 neurological outcome。"],
    points=["Spinal shock (反射喪失) ≠ neurogenic shock (vasomotor 喪失)","可同時併發 (e.g. SCI + 出血)","Atropine 對 bradycardia；Phenylephrine 或 NE 對 hypotension"],
    keyword="Neurogenic shock, spinal cord injury",
    source="ATLS 10/e; AANS Guidelines")

# Q21 (C) Cardiogenic shock
add(21, summary="術中 BP 65/40 + CVP 20 (高) + EKG ST elevation + CO 下降 + SVR 上升 = cardiogenic shock (心肌缺血/AMI)。",
    mechanism="Cardiogenic shock 血流動力學：CO↓、 SVR↑ (代償)、 PCWP/CVP↑ (失代償 forward flow)、 lactate↑。Mixed shock 可同時 hypovolemic + cardiogenic。",
    options={"A":"錯誤。Septic：CO↑、 SVR↓、 CVP↓。","B":"錯誤。Hypovolemic：CO↓、 SVR↑、 CVP↓ (低非高)。","C":"正確 (本題答案)。Cardiogenic 為 CO↓、 SVR↑、 CVP↑。","D":"錯誤。Anaphylactic 為 vasodilation + bronchospasm，類似 distributive。"},
    guidelines=["ACC/AHA Cardiogenic Shock 2017。","SCAI Classification A-E for severity。"],
    points=["術中 AMI 可能是 type 1 (plaque rupture) 或 type 2 (supply-demand)","Treatment：inotrope (dobutamine、 milrinone)、 vasopressor、 IABP、 ECMO、 urgent PCI","TEE 為心臟手術評估 LV function 首選"],
    keyword="Cardiogenic shock, intraoperative MI",
    source="ACC/AHA Cardiogenic Shock 2017")

# Q22 (A) Vasopressin 不增 CO
add(22, summary="Vasopressin 透過 V1 受體引起 vasoconstriction (升 SVR)，但「無 inotropic effect」，「不直接增加 cardiac output」。心衰 + hypotension 應用 dobutamine (inotrope) 或 norepinephrine (α+β)。",
    mechanism="Vasopressin V1 → 平滑肌收縮 → 升 SVR/BP 但對心肌無正性肌力效應。Dobutamine、 NE、 dopamine 透過 β1 inotropy 增加 CO。",
    options={"A":"正確 (本題答案，「無法」增 CO)。Vasopressin 無 inotropic effect。","B":"錯誤。Dobutamine 為 β1 inotrope，增加 CO 為主。","C":"錯誤。NE α+β1，升 BP + 增 CO。","D":"錯誤。Dopamine 高劑量有 α+β1 作用。"},
    guidelines=["Surviving Sepsis：NE first-line，vasopressin 0.03 U/min 為 second-line (catecholamine-sparing)。","Cardiogenic shock 首選 dobutamine + cautious vasopressor。"],
    points=["Vasopressin 在 distributive shock 補充內源 vasopressin 不足","Milrinone (PDE3 inhibitor) 為另一 inotrope，但 vasodilator","Mechanical support (IABP、 Impella、 ECMO) for refractory cardiogenic shock"],
    keyword="Vasopressin, V1 receptor, inotrope",
    source="Surviving Sepsis 2021; ACC/AHA HF Guidelines")

# Q23 (D) PE — thrombolysis & embolectomy
add(23, summary="Massive PE + 休克 → 「血栓溶解劑或手術取栓均為可行」(thrombolytic therapy 為首選，contraindicated 時考慮 surgical/catheter embolectomy)。",
    mechanism="Massive PE：obstructive shock (RV failure → LV underfilling → systemic hypotension)。Thrombolysis (tPA) 對 high-risk PE 改善 hemodynamics + mortality。",
    options={"A":"錯誤。Vasopressor (NE) 為支持治療，非禁忌。","B":"錯誤。Fluid 適量可改善 RV preload，但過量會加重 RV strain。","C":"錯誤。PE 為 obstructive shock，非 distributive。","D":"正確 (本題答案)。Thrombolysis (alteplase 100 mg over 2h) 或 embolectomy 均可行。"},
    guidelines=["ESC PE Guidelines 2019：High-risk PE → systemic thrombolysis；contraindication → embolectomy / catheter-directed。","Anticoagulation：UFH、 LMWH、 DOAC。"],
    points=["PESI score 評估死亡風險","TTE：RV dilation、 McConnell sign、 D-shape LV","CT angio gold standard"],
    keyword="Massive PE, thrombolysis, embolectomy",
    source="ESC PE Guidelines 2019")

# Q24 (C) CO 中毒 + 孕婦
add(24, summary="CO 中毒高壓氧 (HBO₂) 適應症：COHb > 25%、 神經症狀 (意識變化、 暈厥)、 心血管症狀、 「孕婦 (任何 COHb 程度且 > 15%)」。25 歲懷孕 20 週 + COHb 18% 屬高壓氧適應症。",
    mechanism="CO 與 Hb 結合 200x O₂ 親和力 → 功能性 anemia + 左移 oxyhemoglobin curve → 組織 hypoxia。胎兒 Hb 對 CO 親和力更高 + 半衰期長 → 孕婦 CO 中毒對胎兒影響大，需 HBO₂。",
    options={"A":"錯誤。50 歲頭痛 COHb 10% 為 mild，100% O₂ NRM 即可。","B":"錯誤。78 歲祖母 COHb 18% 雖年長但無 severe symptom 描述。","C":"正確 (本題答案)。孕婦 COHb 18% 必須 HBO₂ (保護胎兒)。","D":"錯誤。Mild-moderate symptom 不一定 HBO₂。"},
    guidelines=["UHMS HBO₂ Indications：CO poisoning + (loss of consciousness、 pregnancy、 COHb >25%、 cardiac ischemia、 persistent neurological symptoms)。","100% O₂ via NRM until COHb < 10% + symptom resolution。"],
    points=["COHb 半衰期：room air 4h、 100% O₂ 1h、 HBO₂ 23 min","Delayed neuropsychiatric syndrome (DNS) 2-40 天後出現","Cyanide co-poisoning 同時考慮 (smoke inhalation)"],
    keyword="CO poisoning, HBO2, pregnancy",
    source="UHMS HBO₂ Guidelines")

# Q25 (B) Adductor canal block
add(25, summary="Adductor canal block (ACB) 阻斷 saphenous nerve (純感覺) → 「不會」增加股四頭肌無力 (相較 femoral block)。為 motor-sparing 區域麻醉。",
    mechanism="Femoral nerve block 阻斷整個 femoral nerve (包含 motor branches to quadriceps) → 股四頭肌無力 + 跌倒風險。ACB 阻斷 saphenous (femoral 純感覺分支) → 提供 medial knee/leg 感覺麻醉但保留肌力。",
    options={"A":"正確。Saphenous 為 femoral 純感覺分支。","B":"錯誤 (本題答案)。ACB「不增加」quadriceps weakness，反而為「保留肌力」優勢。","C":"正確。可加 IPACK (popliteal+capsule) block 改善後方止痛。","D":"正確。Local anesthetic intravascular 警示症狀。"},
    guidelines=["PROSPECT TKA：multimodal + LIA + ACB > femoral block。","ASRA：ACB 為現代 TKA 區域麻醉首選。"],
    points=["IPACK 補 ACB 對 posterior knee pain","Continuous catheter 延長 analgesia 48-72h","ACB 比 FNB 更有利 early ambulation"],
    keyword="Adductor canal block, saphenous nerve, motor-sparing",
    source="PROSPECT TKA Guidelines; ASRA")

# Q26 (A) TEG — Fibrinolysis
add(26, summary="TEG 顯示快速 amplitude 下降 (LY30/CL30 增加) = fibrinolysis (fibrin breakdown 速度快)。處置：tranexamic acid (TXA) 1g IV。",
    mechanism="TEG 參數：R time (clotting factor)、 K time (fibrin formation)、 α angle、 MA (platelet/fibrinogen)、 LY30 (fibrinolysis at 30 min)。Hyperfibrinolysis: LY30 > 7.5% 或 amplitude 急降。",
    options={"A":"正確 (本題答案)。Fibrinolysis 為 TEG amplitude 快速衰減。","B":"錯誤。Heparin effect 為 R time 顯著延長。","C":"錯誤。Hypercoagulation 為 short R + high MA + steep angle。","D":"錯誤。Hemodilution 為 low MA + prolonged R。"},
    guidelines=["TEG/ROTEM-guided transfusion 減少血品用量 (CRASH-2 啟發 + viscoelastic test)。","TXA 1g within 3h of trauma 降死亡率。"],
    points=["ROTEM 對應 TEG 不同參數 (EXTEM、 FIBTEM、 APTEM)","Fibrinolysis shutdown 也可能存在 (DIC、 severe trauma)","Bedside viscoelastic test 對 OR/ICU 有用"],
    keyword="TEG, fibrinolysis, TXA",
    source="ASA Practice Guidelines Blood Management; CRASH-2")

# Q27 (C) MG + Succinylcholine
add(27, summary="重症肌無力 (MG) 病人對 succinylcholine 「resistance」(需要劑量「增加」不是減少)。MG 由 nAChR 自抗體破壞 → receptor 數目減少 → 對 depolarizing NMBA 較不敏感。",
    mechanism="MG: AChR 自抗體 → 受體 internalize/destruction → NMJ ACh 反應減弱。Succinylcholine 為 depolarizing → MG 病人需要更高劑量 (1.5-2 mg/kg) 才能達到 paralysis；但對 nondepolarizing (rocuronium) 反而 supersensitive (劑量減半)。",
    options={"A":"正確。揮發性麻醉藥本身有 muscle relaxant 效果，MG 病人可能足夠。","B":"正確。Pyridostigmine (AChE inhibitor) 抑制 plasma cholinesterase → succinylcholine 代謝延長 → 作用延長。","C":"錯誤 (本題錯誤)。Sux 在 MG 應「增加劑量」非「減少」。","D":"正確。Sugammadex 為 rocuronium 反轉首選 (MG 病人 nondepolarizing supersensitive，sugammadex 安全可靠)。"},
    guidelines=["MGFA Anesthesia Guidelines：avoid 非必要 NMBA；rocuronium + sugammadex 為現代首選。","Pre-op pyridostigmine 繼續使用。"],
    points=["Cholinergic crisis vs myasthenic crisis 鑑別：tensilon test","Avoid drugs that worsen MG：aminoglycoside、 magnesium、 β-blocker","Post-op respiratory failure 風險"],
    keyword="Myasthenia gravis, succinylcholine resistance, sugammadex",
    source="MGFA Anesthesia Recommendations; Miller's 8/e")

# Q28 (A) Bronchoscopy — Short-acting opioid
add(28, summary="支氣管鏡檢查：「短效鴉片類 (remifentanil)」抑制咳嗽反射、 minimal residual effect；ETT 應「大」一點 (容納 bronchoscope)；LMA 可用；檢查後立即進食有 aspiration 風險。",
    mechanism="Bronchoscopy 強刺激氣道 → 咳嗽 → bucking。Remifentanil 為極短效，TIVA 配合 BIS。Lidocaine spray 麻痺氣道、 dexmedetomidine 維持配合度。",
    options={"A":"正確 (本題答案)。Remifentanil 或 fentanyl 抑制氣道反射、 minimal residual。","B":"錯誤。ETT 應「大」(7.5-8.0) 容納 bronchoscope (外徑 5-6 mm)。","C":"錯誤。LMA 可用於 short procedure。","D":"錯誤。咽部局麻 + sedation 後應禁食 ≥ 2-4h 直到反射恢復。"},
    guidelines=["ATS/ACCP Bronchoscopy Guidelines。","Topical lidocaine：vocal cords + carina。"],
    points=["Rigid bronchoscopy 需 GA + jet ventilation","Laser bronchoscopy：避免高 FiO₂ (火災)","Hemoptysis 為相對禁忌"],
    keyword="Bronchoscopy, remifentanil, airway anesthesia",
    source="ATS/ACCP Bronchoscopy Guidelines")

# Q29 (B) EVT 體溫
add(29, summary="Acute stroke EVT (取栓) 麻醉照護：「維持 normothermia (36-37°C)」，「不建議 induced hypothermia」(< 35°C 在 stroke 治療尚無證據效益且增加併發症)。",
    mechanism="Acute ischemic stroke induced hypothermia 動物研究 promising 但 human trials (e.g. ICTuS-L) 未顯示明確 benefit + 增加 pneumonia/cardiac arrhythmia。維持 normothermia + 控制 fever 為標準。",
    options={"A":"正確。血糖 140-180 為 stroke 期 target。","B":"錯誤 (本題錯誤)。應 normothermia 36-37°C；30-35°C induced hypothermia 不建議。","C":"正確。Blood vessel opening 前 SBP 140-180 保持灌流；打通後降至 < 180 (避免 hemorrhagic transformation)。","D":"正確。NMBA TOF 1-2 維持 immobile 同時可監測。"},
    guidelines=["AHA/ASA Acute Stroke Guidelines：normothermia + treat fever。","SVIN/SNACC Anesthesia for EVT。"],
    points=["GA vs MAC 對 EVT outcome 仍爭議 (GOLIATH、 SIESTA、 AnStroke)","BP 維持 perfusion 之主動脈夾鉗釋放前後","Time is brain — door to puncture 短化"],
    keyword="EVT, acute stroke anesthesia, normothermia",
    source="AHA/ASA Stroke 2019 Guidelines; SNACC")

# Q30 (A) ECT — Avoid midazolam
add(30, summary="ECT 麻醉「避免 midazolam」(BZD 為 anticonvulsant，會延長 seizure threshold + 降低 seizure quality)。改用 propofol/etomidate + succinylcholine + short-acting agents。",
    mechanism="ECT 治療效果依賴於誘發 generalized seizure。BZD 提高 seizure threshold + 縮短 seizure duration → 治療效果差。Methohexital、 etomidate、 ketamine 為適合 induction (低 anticonvulsant effect)。",
    options={"A":"錯誤 (本題錯誤)。應「避免 midazolam」(anticonvulsant 屬性影響 seizure)。","B":"正確。Propofol 比 etomidate 更短 seizure duration (anticonvulsant)。","C":"正確。Ketamine + propofol 組合可降低 propofol 用量。","D":"正確。Acetaminophen/NSAID 緩解術後頭痛。"},
    guidelines=["APA/RCPsych ECT Guidelines：avoid BZD; use methohexital or etomidate。","Succinylcholine 0.5-1 mg/kg for 防止 musculoskeletal injury during seizure。"],
    points=["Etomidate 為 first choice for ECT (低 anticonvulsant、 stable hemodynamics)","Bite block 防牙齒/舌頭損傷","Seizure 應 ≥ 25 sec 為 effective"],
    keyword="ECT, midazolam contraindication, etomidate",
    source="APA/RCPsych ECT Guidelines")

# Q31 (C) VAE Monitoring sensitivity
add(31, summary="VAE 監測敏感度排序：「TEE > precordial Doppler > ETCO₂ > CVP」。TEE 可偵測 < 0.1 mL/kg air；precordial Doppler 0.25 mL/kg；ETCO₂ drop 較大量 (1-2 mL/kg)；CVP 不敏感。",
    mechanism="VAE 從手術部位 air 進入 venous → RV/PA → 偵測法依血流路徑。TEE 直接看 air bubble；Doppler 聽 high-pitch；ETCO₂ 降是 dead space 增加；CVP 上升慢且非特異。",
    options={"A":"錯誤 (順序錯)。Precordial Doppler < TEE。","B":"錯誤。CVP < ETCO₂。","C":"正確 (本題答案)。② > ① > ③ > ④ 為正確順序。","D":"錯誤。"},
    guidelines=["Sitting craniotomy VAE 發生率 25-45%；其他高風險：seated shoulder、 cesarean、 hip arthroplasty。","Standard monitoring：precordial Doppler + ETCO₂ + ETN₂ + CVP/RA catheter。"],
    points=["Treatment: flood field、 bilateral jugular compression、 aspirate from RA catheter、 Trendelenburg/left lateral、 100% O₂、 stop N₂O","PFO 為 paradoxical air embolism 風險 (preop TEE 排除)","ETN₂ rise 為 VAE 特異 (N₂ wash-in 自肺)"],
    keyword="VAE, TEE, precordial Doppler",
    source="Miller's Anesthesia 8/e Ch. 70")

# Q32 (A) Naloxone
add(32, summary="術後 Heavy sedation + bradycardia + hypoventilation + 瞳孔縮小 + 對痛刺激反應差 = opioid overdose (alfentanil 4 mg 較大量)。Naloxone 0.04-0.1 mg IV 逆轉。",
    mechanism="Opioid overdose 三聯：respiratory depression、 miosis、 CNS depression。Naloxone 競爭性 μ-receptor 拮抗劑，0.04-0.4 mg IV titrate；半衰期 1h (短於多數 opioid，可能 re-sedation)。",
    options={"A":"正確 (本題答案)。Naloxone 為 opioid 拮抗。","B":"錯誤。Neostigmine 為 AChE inhibitor，逆轉 NMBA。","C":"錯誤。Nalbuphine 為 partial agonist，部分逆轉 μ 但效果不一。","D":"錯誤。Flumazenil 為 BZD 拮抗，本案是 opioid 過量。"},
    guidelines=["ASA Sedation Guidelines: 鴉片類拮抗 naloxone；BZD 拮抗 flumazenil。","Renarcotization 需 monitor ≥ 2h (naloxone 短於 long-acting opioids)。"],
    points=["Naloxone 過量逆轉可引發 acute opioid withdrawal、 hypertension、 pulmonary edema","Slow titration 0.04 mg q1-2 min","重複劑量或 infusion 對 long-acting opioid"],
    keyword="Naloxone, opioid overdose, respiratory depression",
    source="ASA Sedation Guidelines; ACLS")

# Q33 (送分)
add(33, summary="本題官方標記為「送分」(無正確答案或答案有疑義)。題目原意為半身麻醉之 dermatome 高度需求：hip = T10；testis = T10；low intra-abdominal = T6-T8；lower extremities = L1-L2。",
    mechanism="Spinal anesthesia dermatome：依手術部位設定。Visceral innervation 比 somatic 高 2-4 levels：故 caesarian section T4、 lower abdominal T6、 hip T10、 lower extremity L1。",
    options={"A":"敘述：hip 至少 T10 (正確標準)","B":"敘述：testis 至少 L1 (實際應 T10 — Testicular nerve C8-T1/T10)","C":"敘述：low intra-abdominal 至少 T6 (合理範圍)","D":"敘述：lower extremities 至少 T12 (合理可達 L1)"},
    guidelines=["Bromage Scale 評估 motor block。","Pinprick test 評估 sensory level。"],
    points=["Testicular pain 由 T10-T11 innervation (genitofemoral + ilioinguinal)","上腹部手術需 T4-T6","臍 = T10、 鼠蹊 = L1"],
    keyword="Spinal anesthesia dermatome levels",
    source="Brown's Atlas of Regional Anesthesia 5/e")

# Q34 (D) Laparoscopy — Compliance↓
add(34, summary="腹腔鏡 pneumoperitoneum 引起：「呼吸順應性下降 (compliance ↓)」(diaphragm 上推、 FRC↓、 atelectasis)。Peak airway pressure 上升、 PaCO₂ 上升、 shunt 增加。",
    mechanism="IAP 12-15 mmHg → diaphragm 上推 → 肺容積壓縮 → compliance↓ + peak P↑ + atelectasis + shunt + V/Q mismatch。CO₂ 吸收 + minute ventilation 不足 → PaCO₂↑。",
    options={"A":"錯誤。Peak airway pressure 「上升」非減少。","B":"錯誤。PaCO₂ 「上升」非下降 (CO₂ 吸收)。","C":"錯誤。Atelectasis + shunt 「上升」非下降。","D":"正確 (本題答案)。Compliance 顯著下降。"},
    guidelines=["EAES Laparoscopy Guidelines：IAP ≤ 15、 慢速 insufflation。","Ventilation：increase MV 30-50% 維持 ETCO₂。"],
    points=["嚴重 CO₂ embolism 罕見但致命","Trendelenburg 加重生理影響","Recruitment maneuver + PEEP 維持 oxygenation"],
    keyword="Laparoscopy, pneumoperitoneum, lung compliance",
    source="Miller's Anesthesia 8/e Ch. 76")

# Q35 (A) Recruitment 壓力
add(35, summary="Recruitment maneuver 標準壓力為「30-40 cmH₂O × 30-40 秒」(不是 20 cmH₂O × 20-30 秒)。20 cmH₂O 不足以 reopen atelectatic alveoli。",
    mechanism="Recruitment 透過短暫高壓 (30-40 cmH₂O) reopen 塌陷肺泡，再 PEEP 維持 (5-10 cmH₂O) 防止再塌陷。Open lung approach 改善 oxygenation + 減少 driving pressure。",
    options={"A":"錯誤 (本題錯誤)。Standard recruitment 30-40 cmH₂O × 30-40 sec，非 20 cmH₂O。","B":"正確。增 RR 而非 TV 補償 CO₂ 吸收 (lung-protective)。","C":"正確。Auscultation 排除 endobronchial + bronchospasm。","D":"正確。FiO₂↑、 PEEP 調整、 I:E ratio 調整為合理處置。"},
    guidelines=["ARDSnet/PROVE Network：Low TV + adequate PEEP + recruitment for ARDS。","Open lung ventilation 在 perioperative 仍爭議 (PROVE Network)。"],
    points=["過度 recruitment 可能 hemodynamic compromise + barotrauma","Driving pressure (Pplat - PEEP) < 15 改善 outcome","Compliance-guided PEEP titration"],
    keyword="Recruitment maneuver, lung protective ventilation",
    source="ARDSnet; PROVE Network")

# Q36 (B) Etomidate + Rocuronium for sepsis
add(36, summary="Sepsis + hemodynamic instability 病人 induction：「Etomidate (穩定循環) + Rocuronium (RSI dose 1.2 mg/kg)」為適當組合。Propofol 引起 cardiovascular collapse；Ketamine 雖維持循環但增加 myocardial O₂ demand。",
    mechanism="Etomidate 為 imidazole derivative，對心血管影響最小、 minimal histamine release。Rocuronium 1.2 mg/kg 提供 onset 60 sec、 適合 RSI。Cisatracurium 起效慢 (3-5 min) 不適合 RSI。",
    options={"A":"錯誤。Propofol 2 mg/kg 在 sepsis hemodynamic instability 可引起 collapse。","B":"正確 (本題答案)。Etomidate 0.2 mg/kg + Rocuronium 1.2 mg/kg。","C":"錯誤。Cisatracurium onset 太慢，不適 RSI。","D":"錯誤。Pancuronium 已過時 (長效、 tachycardia)；Ketamine 在嚴重 sepsis 不一定優於 etomidate。"},
    guidelines=["Surviving Sepsis Campaign 2021。","RSI in shock：etomidate + high-dose rocuronium 或 succinylcholine。"],
    points=["Etomidate 單次 dose 引起 transient adrenal suppression，但對 outcome 影響仍爭議","Sugammadex 16 mg/kg 可逆轉 rocuronium","Norepinephrine 預備在床邊"],
    keyword="Sepsis induction, etomidate, rocuronium RSI",
    source="Surviving Sepsis 2021; Hagberg Airway 4/e")

# Q37 (A) Vocal cord paralysis
add(37, summary="術後咽喉痛 + 聲音沙啞 + 氣音 + 喝水嗆咳 + 無呼吸困難 = 聲帶麻痺 (vocal cord paralysis)，通常由 ETT cuff 對 RLN 壓迫造成。",
    mechanism="Endotracheal intubation 對 RLN 的壓迫 (especially with high cuff pressure 或 prolonged intubation) → unilateral paralysis → 聲音沙啞 + aspiration。多數可恢復 (weeks-months)。",
    options={"A":"正確 (本題答案)。Vocal cord paralysis 典型表現。","B":"錯誤。Epiglottitis 多為 fever + drooling + 兒童呼吸困難。","C":"錯誤。Laryngospasm 為急性完全聲門閉鎖，stridor + 嚴重 desaturation。","D":"錯誤。Pharyngitis 為咽痛主要無聲音改變或嗆咳。"},
    guidelines=["AAOHNS Vocal Fold Paralysis Guidelines。","Cuff pressure < 25 cmH₂O 降低 RLN injury 風險。"],
    points=["Bilateral RLN injury → stridor、 dyspnea、 need tracheostomy","Speech therapy 加速恢復","ENT 評估 + laryngoscopy 確診"],
    keyword="Vocal cord paralysis, RLN injury, postintubation",
    source="AAOHNS Vocal Fold Paralysis Guidelines")

# Q38 (D) Kidney transplant fluid
add(38, summary="腎臟移植應「優先使用 balanced crystalloid (LR)」非 NS。大量 NS 引起 hyperchloremic metabolic acidosis 對 graft 不利。「優先 NS」為錯誤敘述。",
    mechanism="NS (0.9%) 含 154 mEq/L Cl (非生理量) → 大量輸注 → hyperchloremic acidosis + renal vasoconstriction → graft perfusion 受影響。LR 含 K 4 mEq/L 但血清 K 上升極輕微 (myth)。",
    options={"A":"正確。Invasive monitoring 利弊評估，A-line + CVP 常用。","B":"正確。Uremic gastroparesis、 chronic disease → 延遲胃排空，RSI 考慮。","C":"正確。Reperfusion 後 mannitol + furosemide 促 diuresis。","D":"錯誤 (本題錯誤)。LR 較 NS 為佳，NS 引起 hyperchloremic acidosis。"},
    guidelines=["KDIGO Perioperative AKI：avoid hyperchloremic fluid。","SPLIT、 SMART trials：balanced crystalloid > NS in critical care/kidney transplant。"],
    points=["Living donor kidney transplant 較 deceased donor outcome 佳","Avoid nephrotoxic drugs：NSAIDs、 aminoglycoside、 contrast","Tacrolimus、 cyclosporine 為主要 immunosuppression"],
    keyword="Kidney transplant, fluid management, LR vs NS",
    source="KDIGO Guidelines; SPLIT/SMART trials")

# Q39 (A) Acute hemolytic transfusion reaction
add(39, summary="Acute hemolytic transfusion reaction (ABO mismatch) 典型表現：fever、 chills、 hypotension、 hemoglobinuria、 dark urine、 AKI、 DIC、 「Hb 持續上升」並非 — 實際 Hb 「下降」(hemolysis)。",
    mechanism="ABO mismatch → recipient IgM/IgG anti-A/B 與 donor RBC 結合 → complement 活化 → intravascular hemolysis → free Hb + cytokine storm → shock + DIC + AKI。",
    options={"A":"錯誤 (本題錯誤)。AHTR 引起 Hb「下降」(hemolysis)；發燒、 低血壓、 hemoglobinuria 正確但 Hb 上升錯。","B":"正確。立即停輸血、 核對血品、 通報 blood bank。","C":"正確。Emergent 用 O Rh- PRBC + AB FFP 為 universal。","D":"正確。Fluid + vasopressor 支持。"},
    guidelines=["AABB Transfusion Reaction Guidelines：停輸血、 維持 IV access、 通報、 send unit + sample to blood bank。","Aggressive hydration + mannitol/furosemide 保護腎臟。"],
    points=["AHTR mortality 5-10%","Most common cause: clerical error (wrong patient identification)","TRALI、 TACO、 anaphylaxis 為其他急性 reactions"],
    keyword="Acute hemolytic transfusion reaction, ABO mismatch",
    source="AABB Technical Manual")

# Q40 (D) OLV hypoxia
add(40, summary="OLV hypoxia 處置「不可增加揮發性麻醉氣體濃度」(揮發性 > 1 MAC 抑制 HPV、 加重 hypoxia)。應 FiO₂↑、 confirm DLT、 recruitment、 PEEP、 CPAP non-ventilated。",
    mechanism="揮發性麻醉劑 > 1 MAC 抑制 hypoxic pulmonary vasoconstriction (HPV) → 加重 shunt → hypoxia 惡化。OLV 應限制 volatile < 1 MAC 或改 TIVA。",
    options={"A":"正確。FiO₂ 100% 為第一步。","B":"正確。Fiberoptic 確認 DLT 位置 (最常見 hypoxia 原因為 malposition)。","C":"正確。Recruitment ventilated lung 改善通氣。","D":"錯誤 (本題錯誤)。增加揮發劑「加重」hypoxia，不應該做。"},
    guidelines=["AAGBI Thoracic Anaesthesia：lung-protective TV 4-6 mL/kg IBW、 PEEP 5-10、 recruit。","OLV hypoxia 流程：(1) FiO₂↑、 (2) confirm DLT、 (3) PEEP、 (4) CPAP non-ventilated、 (5) recruit、 (6) clamp PA。"],
    points=["DLT malposition 為 OLV hypoxia 最常見原因","Bronchial blocker 為 DLT 替代","TIVA + remifentanil 為 thoracic 麻醉常用"],
    keyword="OLV hypoxia, HPV, volatile anesthetic",
    source="Miller's Anesthesia 8/e Ch. 65")

# Q41 (A) Hypothermia 不增 IOP
add(41, summary="眼壓 (IOP) 影響因素：「Hypothermia 不增加 IOP」(反而可能微降，vasoconstriction)；Hypoxemia、 hypoventilation、 succinylcholine 均「增加」IOP。",
    mechanism="IOP 由 aqueous humor 生成/排出平衡。Hypoxemia + hypoventilation → choroidal vasodilation → IOP↑。Succinylcholine → extraocular muscle sustained contraction → IOP↑ 6-8 mmHg。Hypothermia → choroidal vasoconstriction → IOP 不變或微降。",
    options={"A":"正確 (本題答案)。Hypothermia「不增加」IOP。","B":"錯誤。Hypoxemia 增加 IOP。","C":"錯誤。Hypoventilation (高 CO₂) 增加 IOP。","D":"錯誤。Sux 暫時增加 IOP 6-8 mmHg。"},
    guidelines=["Open globe injury：avoid sux (use rocuronium with sugammadex reversal)。","Glaucoma + cataract 麻醉：avoid IOP 變動。"],
    points=["IOP 增加因素：直接眼球壓、 sux、 hypoventilation、 hypoxia、 head-down、 ketamine、 increase CVP","降低 IOP：mannitol、 acetazolamide、 propofol、 dexmedetomidine","Oculocardiac reflex (OCR)：traction → bradycardia"],
    keyword="IOP, ophthalmic anesthesia, hypothermia",
    source="Stoelting's Co-existing Disease 7/e Ch. Eye")

# Q42 (D) OCR — 停手術刺激
add(42, summary="斜視手術 OCR (heart rate 96→42) 第一步處置：「請外科醫師暫停手術刺激」(remove trigger)。先停止 traction → 通常自行恢復；持續/嚴重才用 atropine。",
    mechanism="OCR (trigeminovagal arc)：眼外肌牽引 → V1 → trigeminal nucleus → vagus → SA node → bradycardia。Fatigable reflex — 重複刺激反應減弱。",
    options={"A":"錯誤。減麻醉藥不是處置 OCR 第一步 (反而 light anesthesia 可加重)。","B":"錯誤。Atropine/glycopyrrolate 為 persistent/severe bradycardia 才用。","C":"錯誤。眼肌 lidocaine 對 OCR 無效 (機制在 sensory 路徑)。","D":"正確 (本題答案)。停止刺激為 first-line。"},
    guidelines=["Coté and Lerman Pediatric Anesthesia：prophylactic atropine 0.02 mg/kg for high-risk pediatric strabismus。","Adequate depth of anesthesia 預防 OCR。"],
    points=["Persistent bradycardia + hypotension → atropine 0.02 mg/kg IV","Severe → asystole → CPR + atropine","Hypoxia/hypercapnia 加重 OCR"],
    keyword="Oculocardiac reflex, strabismus, traction",
    source="Coté and Lerman 6/e")

# Q43 (B) Laryngospasm — NPPE in young athletes
add(43, summary="Laryngospasm 引起 NPPE「主要在年輕健康肌力強者」(產生強 inspiratory negative pressure)，「非肌少老年人」。",
    mechanism="Laryngospasm + 強 inspiratory effort against closed glottis → markedly negative intrathoracic pressure → 增加 venous return + 肺微血管壓力 → fluid leakage → NPPE。年輕健康肌力強者 inspiratory effort 較強，反而高風險。",
    options={"A":"正確。Superior laryngeal nerve internal branch 為 sensory afferent；reflex 引起聲帶閉鎖。","B":"錯誤 (本題錯誤)。NPPE「強壯青年」較多，肌少老年人因肌力不足反而較少。","C":"正確。CPAP via tight mask 為標準。","D":"正確。Succinylcholine 0.1-0.5 mg/kg IV 或 IM 4 mg/kg。"},
    guidelines=["APAGBI Pediatric Difficult Airway 2015。","Larson's maneuver (jaw thrust + 耳後壓) 緩解 laryngospasm。"],
    points=["URI 2-4 wk 推遲 elective surgery","Smooth induction + avoid Stage 2 manipulation","NPPE：onset min-hours，diuretic + O₂ 治療"],
    keyword="Laryngospasm, NPPE, young athletic",
    source="APAGBI Pediatric Difficult Airway 2015")

# Q44 (B) Remifentanil for awake intubation
add(44, summary="Remifentanil「可」用於 awake fiberoptic intubation — 短效、 titratable、 可用 TCI 提供 sedation + cough suppression。題目說「不適用」為錯誤。",
    mechanism="Awake FOB intubation 需 sedation + analgesia + cough suppression 維持自主呼吸。Remifentanil 透過 ester 代謝、 context-sensitive half-time 短，與 dexmedetomidine 為現代 awake intubation 兩大選擇。Respiratory depression dose-dependent，可滴定避免。",
    options={"A":"正確。Glycopyrrolate 0.2 mg IV 減少分泌物。","B":"錯誤 (本題錯誤)。Remifentanil 短效可滴定為 awake intubation 適合藥物，非「不適用」。","C":"正確。Lidocaine spray 麻痺 superior laryngeal n. → 降低 supraglottic 刺激。","D":"正確。Cricothyroid membrane 注射 lidocaine 引起 cough → 自身霧化至 trachea/RLN territory，麻痺 RLN 感覺。"},
    guidelines=["DAS 2015：awake intubation 為預期 difficult airway 首選。","ASRA Awake Intubation Consensus 2019。"],
    points=["Dexmedetomidine 0.5-1 µg/kg loading + 0.2-0.7 µg/kg/h 為理想 sedation (無呼吸抑制)","Topical lidocaine total dose < 7 mg/kg","Nebulized + spray + nerve block 三段式"],
    keyword="Awake fiberoptic, remifentanil, dexmedetomidine",
    source="DAS 2015; ASRA Awake Intubation Consensus 2019")

# Q45 (B) POVL — Cardiac + prone spine
add(45, summary="術後視力減退 (POVL) 高風險手術：「心臟手術 + 俯臥位脊椎手術」。原因：cardiac surgery 為 CRAO/cortical blindness 風險；prone spine 為 ION (ischemic optic neuropathy) 風險。",
    mechanism="Cardiac surgery POVL：CPB embolism、 hypoperfusion → CRAO/cortical blindness。Prone spine POVL：long duration + blood loss + 低血壓 + venous congestion (head-down)、 prone position → ION。",
    options={"A":"錯誤 (組合錯)。Craniotomy POVL 風險較低。","B":"正確 (本題答案)。Cardiac + prone spine 為兩大 POVL 高風險。","C":"錯誤。仰臥頸椎手術 POVL 風險低。","D":"錯誤。"},
    guidelines=["ASA POVL Practice Advisory 2019。","Spine surgery > 6h + EBL > 1L 為 highest risk。"],
    points=["Prevention：avoid head-down、 monitor Hct、 適當 headrest、 avoid prolonged hypotension","ION prognosis poor — 多數無恢復","Mid-procedure 檢查眼瞼/壓力"],
    keyword="POVL, ION, prone spine surgery, cardiac surgery",
    source="ASA POVL Practice Advisory 2019")

# Q46 (C) Stridor post-extubation
add(46, summary="拔管後 stridor (laryngeal edema) 處置：「先 100% O₂ face mask、 必要時重新插管」+ nebulized epinephrine + steroid + heliox。",
    mechanism="Laryngeal edema 引起 upper airway obstruction (stridor)，可進展 respiratory failure。處置：support → racemic epinephrine nebulizer → dexamethasone → reintubation if severe。",
    options={"A":"錯誤。Adult 氣道較大，stridor 風險「較低」非較高；兒童 (cricoid 較窄) 才容易 stridor。","B":"錯誤。Stridor 減弱可能是「惡化」(完全阻塞無 air movement 也無 stridor)。","C":"正確 (本題答案)。100% O₂ 面罩通氣 + 準備 reintubation。","D":"錯誤。應 racemic epinephrine 與 dexamethasone，「Terbutaline」(β2-agonist for bronchospasm) 不是首選。"},
    guidelines=["DAS Extubation Guidelines 2012。","Cuff leak test < 110 mL or < 24% 為 reintubation 風險指標。"],
    points=["Tracheal extubation in head-down lateral or full upright","Heliox (helium-oxygen) 改善 turbulent flow","Surgical airway 預備 (cricothyroidotomy)"],
    keyword="Post-extubation stridor, laryngeal edema",
    source="DAS Extubation Guidelines 2012")

# Q47 (D) FES — Steroid 證據不足
add(47, summary="脂肪栓塞症候群 (FES) 治療以「支持性療法」為主 (O₂、 ventilation)。「Steroid」雖被使用，但「臨床實證效益不確定」— 並非首選治療藥物。",
    mechanism="FES 由 fat globule + chemical mediator 引起肺血管 + 全身 endothelial dysfunction。Steroid 理論抑制 inflammation 但 RCT 證據不一致。",
    options={"A":"正確。Respiratory distress + AMS + petechiae (axilla、 chest、 conjunctiva) 為 Gurd's triad。","B":"正確。長骨/骨盆骨折 24-72h 內發生。","C":"正確。發生率 1-3%；mortality 10-20%。","D":"錯誤 (本題錯誤)。Steroid 證據不一致，「非首選」治療。"},
    guidelines=["AAOS：早期 (<24h) long bone fracture 固定降低 FES 風險。","Mechanical ventilation + supportive care 為主。"],
    points=["Diagnostic criteria：Gurd's, Schonfeld scores","Differential：PE、 ARDS、 sepsis、 TBI","CT chest ground-glass、 micronodules"],
    keyword="Fat embolism syndrome, steroid, supportive care",
    source="Stoelting's Co-existing Disease 7/e Ch. Orthopedic")

# Q48 (B) Interscalene block 阻斷 upper + middle trunks
add(48, summary="Interscalene block 阻斷 brachial plexus 在「upper + middle trunks」(C5-C7) 提供 shoulder 麻醉。「Middle + lower trunks」為錯誤敘述 (lower trunk T1 不易 cover)。",
    mechanism="Brachial plexus interscalene level (C5-T1 trunks)。Interscalene approach 主要覆蓋 upper + middle trunks (C5-C7)。Lower trunk (C8-T1) 對應 ulnar nerve distribution 常不完整 cover。",
    options={"A":"正確。肩部 + 上臂為主要適應症。","B":"錯誤 (本題錯誤)。Interscalene 阻斷 upper + middle trunks (C5-C7)，非 middle + lower。","C":"正確。Phrenic nerve block ~100% (橫膈麻痺)。","D":"正確。橫膈麻痺 → 呼吸抑制、 CO₂↑、 SpO₂↓。"},
    guidelines=["ASRA：interscalene 嚴重 COPD/單肺/嚴重肥胖為相對禁忌。","Low-volume (10-15 mL) 降低 phrenic block 機率。"],
    points=["Supraclavicular (50% phrenic) 較 interscalene 安全","Cardiac arrest case (Bromage-Drury syndrome) 罕見","Bezold-Jarisch reflex in beach-chair position"],
    keyword="Interscalene block, brachial plexus, phrenic nerve",
    source="Brown's Atlas of Regional Anesthesia 5/e")

# Q49 (C) RA + Cervical instability
add(49, summary="RA 病人「頸椎 atlantoaxial instability (C1-C2)」常見、 需術前評估。「TMJ instability」為錯誤敘述 (RA 影響 TMJ 為 hypomobility 非 hypermobility)。",
    mechanism="RA 影響 cervical spine (especially atlantoaxial joint) → C1-C2 subluxation → spinal cord/brainstem 壓迫風險。TMJ 影響為 limited mouth opening (hypomobility)，非 hypermobility。",
    options={"A":"正確。RA-ILD (interstitial lung disease) 為合併症。","B":"正確。Atlantoaxial instability 為麻醉重大 concern (插管 hyperextension 風險)。","C":"錯誤 (本題錯誤)。RA TMJ 為「hypomobility」(張口困難)、 非 hypermobility。","D":"正確。Pericardial effusion + valve disease 常見。"},
    guidelines=["ACR RA Perioperative Guidelines。","Awake fiberoptic intubation for unstable cervical spine。"],
    points=["MTX、 biologics 周圍手術調整","Cricoarytenoid arthritis → hoarseness、 difficult intubation","Steroid stress dose if chronic steroid"],
    keyword="Rheumatoid arthritis, atlantoaxial instability, TMJ",
    source="Stoelting's Co-existing Disease 7/e")

# Q50 (C) MG resistant to sux hyperkalemia
add(50, summary="重症肌無力 (MG) 病人對 succinylcholine「resistance」(需高劑量) 但「不增加 hyperkalemia 風險」。其他 NMD (ALS、 GBS、 DMD) 由於 extrajunctional AChR up-regulation → sux 引起致命 hyperkalemia。",
    mechanism="ALS、 GBS、 DMD、 denervation → extrajunctional AChR up-regulation → sux 大量 K efflux → fatal hyperkalemia。MG 反而 receptor 數目「減少」(antibody-mediated destruction) → 對 sux resistant 但無 K efflux 大幅增加。",
    options={"A":"錯誤。ALS denervation → AChR up-regulation → sux hyperkalemia 風險。","B":"錯誤。GBS denervation → 同理。","C":"正確 (本題答案)。MG receptor 減少，不會 hyperkalemia (但對 sux resistant)。","D":"錯誤。DMD 為 sux「絕對禁忌」(fatal hyperkalemia + rhabdomyolysis)。"},
    guidelines=["MHAUS：sux contraindicated in DMD/muscular dystrophy。","Burn (>24h)、 prolonged immobilization、 stroke 同樣風險。"],
    points=["MG：對 nondepolarizing supersensitive (劑量減半)","DMD：避免 sux + volatile，TIVA","Sugammadex 為 rocuronium 反轉首選"],
    keyword="Myasthenia gravis, succinylcholine, hyperkalemia",
    source="MGFA Guidelines; Miller's 8/e")

# Q51 (B) POVL — Female 不是 risk factor
add(51, summary="POVL 危險因子：obesity、 男性、 long duration、 large blood loss、 hypotension、 anemia、 DM、 prone position。「女性」「不是」risk factor (反而男性風險較高)。",
    mechanism="POVL 多為 ION，男性風險高 (生理解剖、 vascular 因素)。其他因素加重 optic nerve hypoperfusion。",
    options={"A":"錯誤 (是 risk factor)。Obesity 為 POVL 危險因子。","B":"正確 (本題答案，不是 risk factor)。男性 > 女性風險。","C":"錯誤。DM 為 risk factor。","D":"錯誤。長手術為 risk factor。"},
    guidelines=["ASA POVL Practice Advisory 2019：identify high-risk + counseling pre-op。","Avoid prolonged hypotension、 head-down、 large fluid shifts。"],
    points=["Male：female ratio for ION ~2:1","Anemia + hypotension 協同效應","Mayfield/foam headrest 適當"],
    keyword="POVL risk factors, male sex",
    source="ASA POVL Practice Advisory 2019")

# Q52 (D) Opioid 不降 CMRO2 等
add(52, summary="腦部手術 neuroprotection：「Barbiturate、 etomidate、 propofol」均降 CMRO₂ + CBF + ICP。「Opioid」不顯著降低 CMRO₂/CBF/ICP，但提供 analgesia + 減少 stress response。",
    mechanism="GABA-A agonist (barbiturate、 propofol、 etomidate) 降 CMRO₂ → flow-metabolism coupling → CBF↓ → ICP↓。Opioid 主要透過 μ-receptor 中樞鎮痛，對 CMRO₂/CBF 影響微小。",
    options={"A":"錯誤。Barbiturate 降 CMRO₂/CBF/ICP (burst suppression 最大)。","B":"錯誤。Etomidate 降 CMRO₂/CBF/ICP。","C":"錯誤。Propofol 為 neuroanesthesia 首選。","D":"正確 (本題答案)。Opioid「不」顯著降低 CMRO₂/CBF/ICP。"},
    guidelines=["SNACC Neuroanesthesia Recommendations。","Avoid N₂O in air-containing space (pneumocephalus)。"],
    points=["Burst suppression for refractory ICP/seizure","Mannitol 0.25-1 g/kg、 hypertonic saline 3% osmotic therapy","Head elevation 30°、 normocapnia 35-40"],
    keyword="Neuroprotection, CMRO2, opioid",
    source="Miller's Anesthesia 8/e Ch. 70")

# Q53 (C) DI — Low urine osmolality
add(53, summary="Diabetes insipidus (DI) 由於 ADH 不足 (central) 或 V2 受體失調 (nephrogenic) → 「無法集中尿液」→ urine osmolality 低 (< 300，常 < 100)。",
    mechanism="ADH 作用於 collecting duct V2 receptor → AQP2 → 水重吸收。DI 失去此機制 → 大量稀釋尿。血液：dehydration → high serum Na + osmolality；尿液：low osmolality、 low specific gravity。",
    options={"A":"錯誤。Serum Na 「上升」(脫水)。","B":"錯誤。Serum osmolality 「上升」。","C":"正確 (本題答案)。Urine osmolality 「低」(無 ADH 集中)。","D":"錯誤。Urine Na 通常正常或上升 (與 osmolality 對比明顯)。"},
    guidelines=["Brain Trauma Foundation：post-TBI DI 常見，monitor 尿量、 血鈉、 osmolality。","Desmopressin (DDAVP) 為 central DI 治療。"],
    points=["Central DI：ADH↓；Nephrogenic DI：V2 受體 resistance","Water deprivation test + DDAVP 區分","Triple phase response after pituitary surgery (DI → SIADH → DI)"],
    keyword="Diabetes insipidus, urine osmolality, ADH",
    source="Brain Trauma Foundation; Endocrine Society")

# Q54 (D) Amphetamine 降麻醉藥需求
add(54, summary="長期慢性物質濫用對麻醉藥需求：「Amphetamine 慢性 — 降低需求」(catecholamine depletion → adrenergic reserve↓)。Opioid、 alcohol、 marijuana 急性增加、 慢性 tolerance 增加需求。",
    mechanism="Acute amphetamine：catecholamine release → SNS activation → 麻醉藥需求↑。Chronic amphetamine：突觸前 catecholamine depletion → adrenergic reserve↓ → hypotension on induction → 麻醉藥需求「下降」+ vasopressor 反應差。",
    options={"A":"錯誤。Chronic opioid 需求「上升」(tolerance)。","B":"錯誤。Chronic alcohol 需求「上升」(CYP 誘導 + cross-tolerance)。","C":"錯誤。Marijuana 慢性影響微妙，整體需求變化不顯著。","D":"正確 (本題答案)。Chronic amphetamine catecholamine depletion → 需求下降。"},
    guidelines=["ASA Perioperative Substance Use Disorder Guidelines。","Pre-op screening + multidisciplinary approach。"],
    points=["Cocaine acute 與 amphetamine 類似 (catecholamine release)","Direct-acting vasopressor (phenylephrine、 vasopressin) 比 indirect (ephedrine) 有效","Naloxone 慎用 (opioid-dependent precipitate withdrawal)"],
    keyword="Substance abuse, amphetamine, anesthetic requirement",
    source="Stoelting's Co-existing Disease 7/e")

# Q55 (D) Tourniquet release — temperature drop
add(55, summary="Tourniquet 釋放後典型變化：「ETCO₂ 急升」、 K+ + lactate 急升、 metabolic acidosis、 「體溫 down」(冷血液回流)。「體溫 + ETCO₂ 突然上升」為錯誤敘述 (體溫「下降」)。",
    mechanism="Tourniquet 期間 limb cold + ischemic metabolite 累積。Release → 冷血回流 → systemic temperature 下降；lactate + K + H + CO₂ 大量釋出 → metabolic acidosis + hyperkalemia + ETCO₂ 急升。",
    options={"A":"正確。> 2h 高風險 rhabdomyolysis + neuropathy。","B":"正確。小兒 tourniquet 釋放後體溫上升 (代謝產物 + 增加 metabolism)。","C":"正確。Reperfusion 引起 metabolic acidosis。","D":"錯誤 (本題錯誤)。應為「體溫下降」(非上升)；ETCO₂ 上升正確。"},
    guidelines=["AAOS Tourniquet Use Guidelines。","充氣 ≤ 2h；上肢 SBP+50、 下肢 SBP+100。"],
    points=["釋放前：FiO₂↑、 fluid bolus、 monitor ETCO₂、 K","嚴重 hyperkalemia：staged/slow release","Tourniquet pain 45-60 min 後出現"],
    keyword="Tourniquet release, hyperkalemia, hypothermia",
    source="AAOS Tourniquet Guidelines")

# Q56 (A) TURP syndrome
add(56, summary="TURP syndrome 初期症狀：「噁心、 意識模糊、 躁動、 視力障礙」(尤其 glycine 灌注 → visual symptom + neuro)。",
    mechanism="Monopolar TURP 用 glycine 1.5%、 sorbitol、 mannitol nonconductive irrigation。Prostatic venous sinuses 開放 + 高壓 → 大量吸收 → acute hyponatremia + fluid overload + glycine toxicity (visual + ammonia)。",
    options={"A":"正確 (本題答案)。早期 nausea、 confusion、 visual changes 為經典。","B":"錯誤。應避免大量低張溶液；wuse normal saline (bipolar TURP)。","C":"錯誤。Bipolar TURP (NS irrigation) 「降低」非「升高」TURP syndrome 風險。","D":"錯誤。Spinal 達到 T10-12 即可 (不需 T4)。"},
    guidelines=["AUA TURP Guidelines：bipolar TURP 為現代首選。","Awake spinal 較 GA 易早期偵測 TURP syndrome。"],
    points=["TURP syndrome 處置：3% NaCl 緩慢矯正、 furosemide、 ICU","Acute symptomatic hyponatremia (<48h) 可較快矯正","HoLEP 為新興技術 (no syndrome)"],
    keyword="TURP syndrome, hyponatremia, glycine toxicity",
    source="Stoelting's Co-existing Disease 7/e")

# Q57 (C) 孕婦 FRC↓、 blood volume↑
add(57, summary="妊娠 34 週生理變化：「FRC 下降 + blood volume 上升 30-50%」為正確。「Minute ventilation」上升 50% + CO 上升 50%、 SVR 下降、 PaCO₂ 下降 (30-32)、 HCO₃ compensatory 下降。",
    mechanism="孕期 progesterone、 estrogen 與機械變化：子宮上推 diaphragm → FRC↓ 20%；O₂ consumption↑ 20%；minute ventilation↑ 50%；CO↑ 50%；blood volume↑ 30-50%；SVR↓；aortocaval compression。",
    options={"A":"錯誤。Alveolar ventilation 「上升」，CO 「上升」。","B":"錯誤。PaCO₂ 下降，外周 SVR 「下降」。","C":"正確 (本題答案)。FRC↓ + intravascular volume↑。","D":"錯誤。HCO₃ compensatory「下降」，CVP 維持基本不變或微降。"},
    guidelines=["ACOG Practice Bulletin Pregnancy Physiology。","Left uterine displacement > 20 週。"],
    points=["Rapid desaturation：FRC↓ + O₂ consumption↑","Difficult airway 風險：edema、 breast、 weight gain","Hypercoagulable state"],
    keyword="Pregnancy physiology, FRC, blood volume",
    source="Chestnut's Obstetric Anesthesia 6/e")

# Q58 (D) Preeclampsia + spinal
add(58, summary="重度子癇前症 + MgSO4 病人「可以行 spinal anesthesia」(實際上 spinal 為剖腹產首選 — 改善 BP 控制 + 避免 GA airway risk)。「不建議 spinal」為錯誤敘述。",
    mechanism="Preeclamptic patients 對 spinal anesthesia 反應較穩定 (因 elevated SVR + chronic vasoconstriction)，hypotension 程度較 normal pregnancy 小；spinal 較 GA 安全 (避免 airway difficulty、 hypertensive surge during intubation)。Severe thrombocytopenia (<70K) 為禁忌。",
    options={"A":"正確。Liver function + 血小板評估必要。","B":"正確。MgSO4 加成 NMBA，劑量減 50%。","C":"正確。Labetalol IV 為 hypertensive crisis 一線治療。","D":"錯誤 (本題錯誤)。Spinal 反而為首選 (除非 platelet < 70K 或 coagulopathy)。"},
    guidelines=["ACOG Practice Bulletin 222 Preeclampsia。","SOAP Consensus 2020 OB Anesthesia。"],
    points=["Magnesium continue 24h postpartum","Antihypertensive：Labetalol、 Hydralazine、 Nifedipine；avoid ACE-I","HELLP syndrome variation"],
    keyword="Preeclampsia, spinal anesthesia, MgSO4",
    source="ACOG Practice Bulletin 222; Chestnut 6/e")

# Q59 (送分)
add(59, summary="本題官方標記為「送分」(無正確答案或答案有疑義)。涉及新生兒各種手術麻醉考量。",
    mechanism="新生兒麻醉特殊性：immature physiology、 fragile hemodynamics、 small reserve、 pediatric drug PK 不同、 thermal regulation 差。",
    options={"A":"敘述：高 FiO₂ 與 ROP — 實際應「限制」FiO₂ 避免 ROP (尤其早產兒)，故此敘述錯。","B":"敘述：食道閉鎖近端氣管廔管 — 解剖描述不完全正確。","C":"敘述：幽門狹窄 5-6 週發生、 NG decompression — 部分正確但 timing 多 3-6 wks。","D":"敘述：NEC 早產兒 + 限制輸液 2-5 mL/kg/h — NEC 需 active fluid resuscitation (sepsis), 2-5 mL/kg/h 過少。"},
    guidelines=["APAGBI Neonatal Surgery Guidelines。","ROP：FiO₂ titrate maintain SpO₂ 90-95% (避免 hyperoxia)。"],
    points=["Pyloric stenosis：metabolic alkalosis 矯正後手術","NEC：emergency surgery + aggressive resuscitation","TEF：avoid PPV pre-intubation"],
    keyword="Neonatal anesthesia, special considerations",
    source="Coté and Lerman 6/e")

# Q60 (C) Pediatric airway — Large tongue
add(60, summary="兒童氣道：「舌頭相對較大」是正確的解剖特徵，導致 face mask + laryngoscopy 困難 + 易上呼吸道阻塞。",
    mechanism="兒童頭大、 舌大、 頸短、 occiput 突出、 larynx 較高 (C3-4)、 epiglottis 長 omega-shaped、 cricoid 為最窄。隨年齡 (8歲) 漸接近成人。",
    options={"A":"錯誤。傳統教學「cricoid 為最窄」(non glottis)，成人則 glottis 為最窄。","B":"錯誤。Closing volume「較大」(non smaller)，故 atelectasis 與 shunt 容易。","C":"正確 (本題答案)。Large tongue → mask + laryngoscopy 困難 + 易阻塞。","D":"錯誤。FRC 比成人約 2/3 (約成人 1/2 描述不準確)。"},
    guidelines=["APAGBI Pediatric Airway Guidelines。","Cuffed ETT 已廣泛接受 in pediatrics。"],
    points=["ETT size：cuffed = (age/4)+3.5、 uncuffed = (age/4)+4","Depth：(age/2)+12 cm at lip","Rapid desat (low FRC + high O₂ consumption)"],
    keyword="Pediatric airway, large tongue, anatomical differences",
    source="Coté and Lerman 6/e")

# Q61 (A) Midazolam onset
add(61, summary="Midazolam「口服」起效時間「20-30 分鐘」，於麻醉前「20-30 min」給予 (非 1 hr)。「需於麻醉前 1 小時給予」為錯誤敘述。",
    mechanism="Oral midazolam 0.5 mg/kg 起效 15-30 min、 高峰 30-45 min。其他途徑：IN (0.2 mg/kg) 起效 10-15 min；IV/IM 5 min。",
    options={"A":"錯誤 (本題錯誤)。Midazolam 起效 20-30 min，「不是 1 hr」。","B":"正確。Ketamine 維持氣道反射、 sympathetic stimulation。","C":"正確。Rocuronium 1.2 mg/kg 為兒童 RSI 首選 (避免 sux 風險)。","D":"正確。DMD sux 絕對禁忌。"},
    guidelines=["APAGBI Pediatric Pre-op Anxiolysis：oral midazolam 為 first-line。","DEX 為 alternative：dexmedetomidine intranasal 2 µg/kg。"],
    points=["Midazolam 副作用：paradoxical agitation、 amnesia、 respiratory depression at high dose","Parental presence 與 premed 為 anxiety reduction strategies","Emergence delirium：minimize with dexmedetomidine"],
    keyword="Pediatric premedication, midazolam, oral",
    source="Coté and Lerman 6/e")

# Q62 (A) Geriatric — HR↓ ability
add(62, summary="老年人生理變化：「增加 HR 能力下降」(baroreflex 鈍化 + sympathetic responsiveness 減弱)。其他選項均錯。",
    mechanism="Aging 心血管：β-receptor sensitivity↓、 baroreflex blunting、 sympathetic responsiveness 減弱 → 對 hypovolemia/hypotension 無法以 tachycardia 代償。Maximum HR↓ (formula 220-age)。",
    options={"A":"正確 (本題答案)。HR 增加能力 (chronotropic reserve) 下降。","B":"錯誤。PaO₂ 「下降」(closing capacity↑、 A-a gradient widens)。","C":"錯誤。肺順應性 「上升」(elastin 破壞、 emphysema-like)；chest wall「下降」。","D":"錯誤。對低溫敏感度「上升」(thermoregulation 變差，更易 hypothermia)。"},
    guidelines=["ASA Brain Health Initiative：Perioperative neurocognitive disorders。","Beers Criteria：drugs to avoid in elderly。"],
    points=["Frailty Index 為手術預後預測","Renal/hepatic clearance↓","Polypharmacy interaction"],
    keyword="Geriatric physiology, chronotropic reserve",
    source="Miller's Anesthesia 8/e Ch. 80")

# Q63 (D) BZD dose↓ in elderly
add(63, summary="老年人對「benzodiazepine 之 sensitivity 上升」(pharmacodynamic) → 劑量需「下降」。其他選項均錯。",
    mechanism="Aging pharmacodynamic changes：BZD、 opioid receptor sensitivity↑ → 對同劑量反應強。Pharmacokinetic：Vd↑ (lipophilic)、 clearance↓ → 半衰期長。MAC「下降」(non 上升) 6%/decade。",
    options={"A":"錯誤。MAC「下降」(每 10 歲約 -6%)，非上升。","B":"錯誤。Albumin↓ → free drug fraction↑ → 麻醉藥效「增強」非下降。","C":"錯誤。麻醉劑需求量與年齡「負相關」(老越大需求越少)。","D":"正確 (本題答案)。BZD pharmacodynamic sensitivity↑ → 劑量下降。"},
    guidelines=["Beers Criteria 2019：BZD 為 potentially inappropriate medication in elderly。","Avoid BZD as preanesthetic in elderly (delirium risk)。"],
    points=["Induction dose 下調 30-50%","Volatile MAC 下降","Postop delirium 預防：avoid deliriogenic drugs、 multimodal opioid-sparing"],
    keyword="Geriatric anesthesia, BZD, MAC",
    source="Miller's 8/e Ch. 80; Beers Criteria")

# Q64 (D) Parkinson disease
add(64, summary="Parkinson disease (PD)：dopaminergic 神經元退化 → tremor、 rigidity、 bradykinesia、 postural instability 經典四主徵。「退化神經疾病主要症狀為震顫、 肌肉僵硬、 姿勢不穩」正確。",
    mechanism="PD：substantia nigra dopaminergic neuron loss + Lewy bodies → 抑制 thalamic-cortical motor 不足 → motor symptoms。Levodopa + carbidopa 為主要治療。",
    options={"A":"錯誤。Anti-PD 藥物「術日早晨」應繼續服用 (停藥引起 severe rigidity 與 NMS-like syndrome)。","B":"錯誤。Sux 反應與一般人無異 (除非 immobility-induced denervation 才可能 hyperkalemia)。","C":"錯誤。PD 為 dopamine「減少」非增加。","D":"正確 (本題答案)。退化神經 + 經典四主徵。"},
    guidelines=["PD 麻醉：continue levodopa；avoid dopamine antagonist (metoclopramide、 droperidol、 phenothiazine)、 meperidine (MAO interaction)。","Awake fiberoptic for severe rigidity/dysphagia。"],
    points=["Off-period rigidity 影響 ventilation","Deep brain stimulation (DBS) 病人：avoid monopolar cautery near device","Anti-emetic：ondansetron 安全"],
    keyword="Parkinson disease, dopamine, anesthesia",
    source="Stoelting's Co-existing Disease 7/e")

# Q65 (C) Ramped position image
add(65, summary="肥胖病人理想 ramped position：「外耳道對齊胸骨切跡」(tragus to sternal notch horizontal alignment) + sniffing position (mild flexion of lower cervical + extension of upper)。本題答案 C 為正確圖示。",
    mechanism="Ramped position 改善：(1) Laryngoscopy view (atlanto-occipital extension); (2) FRC 維持 (gravity 對 abdominal mass)；(3) Pre-oxygenation 效率。",
    options={"A":"錯誤。Supine 不符。","B":"錯誤。其他姿勢不符。","C":"正確 (本題答案)。Tragus-sternal notch alignment + sniffing。","D":"錯誤。"},
    guidelines=["SOBA Bariatric Anesthesia Guidelines。","HELP (Head Elevated Laryngoscopy Position) 或 ramped position。"],
    points=["25-30° head-up tilt for pre-oxygenation","Apneic time before desaturation 大幅縮短","HFNC (high-flow nasal cannula) 延長 safe apnea time"],
    keyword="Ramped position, sniffing position, obese intubation",
    source="SOBA Guidelines; Hagberg Airway 4/e")

# Q66 (D) OSA — Neck circumference
add(66, summary="OSA 風險因子：「男性頸圍 > 43 cm、 女性 > 41 cm」為已知預測指標 (STOP-BANG components)。",
    mechanism="OSA pathology：sleep 期間 upper airway collapse → 間歇 hypoxia + arousal。風險因素：obesity、 大頸圍、 男性、 老年、 retrognathia、 macroglossia。",
    options={"A":"錯誤。OSA 為氣道阻塞描述不完全 (應是 reduced or absent airflow)。","B":"錯誤。OSA 包含日間嗜睡 (excessive daytime sleepiness, EDS)，描述「不會嗜睡」錯。","C":"錯誤。OSA 風險為男性、 高血壓 (非低血壓)、 鼻塞、 老年。","D":"正確 (本題答案)。頸圍 male > 43、 female > 41 為 STOP-BANG criteria。"},
    guidelines=["STOP-BANG questionnaire 預測 OSA。","ASA OSA Practice Guidelines。"],
    points=["CPAP 為長期治療首選","Postop CPAP 維持 (尤其 PACU)","Avoid full opioid (multimodal analgesia)、 careful sedation"],
    keyword="OSA, STOP-BANG, neck circumference",
    source="ASA OSA Practice Guidelines")

# Q67 (A) Bariatric laparoscopic
add(67, summary="腹腔鏡減肥手術氣腹 + Trendelenburg 引起：「venous return 遲滯、 portal flow↓、 urine output↓」。其他選項描述方向均錯。",
    mechanism="Pneumoperitoneum (IAP↑) + Trendelenburg：(1) Diaphragm 上推 → FRC↓、 compliance↓、 peak P↑；(2) IVC compression → venous return 遲滯；(3) Portal flow↓、 splanchnic perfusion↓；(4) Renal perfusion↓ → urine output↓；(5) CO₂ 吸收 → PaCO₂↑；(6) Aortocaval compression → SVR↑、 baroreceptor activation。",
    options={"A":"正確 (本題答案)。Venous return↓、 portal flow↓、 urine output↓。","B":"錯誤。IAP「上升」非下降；compliance「下降」非上升；airway pressure↑ 正確但組合錯。","C":"錯誤。Hypercarbia 非 hypocarbia；PaCO₂↑。","D":"錯誤。CVP「上升」(thoracic pressure↑)；SVR↑ (afterload↑) 非下降。"},
    guidelines=["SOBA Bariatric Surgery Guidelines。","Low IAP (8-12) 在高風險病人。"],
    points=["Reverse Trendelenburg 緩解部分影響","Anti-Trendelenburg + IAP < 15 為標準","VTE prophylaxis：mechanical + chemical"],
    keyword="Bariatric laparoscopy, pneumoperitoneum, hemodynamics",
    source="SOBA Bariatric Surgery Guidelines")

# Q68 (A) PONV risk
add(68, summary="PONV 高風險手術：「膽囊切除、 腹腔鏡、 婦科」為已知高風險術式。其他選項均錯。",
    mechanism="PONV 病人危險因素：女性、 不吸菸、 PONV/暈車病史、 術後 opioid。手術危險因素：膽囊、 腹腔鏡、 婦科、 ENT、 strabismus、 lengthy surgery。",
    options={"A":"正確 (本題答案)。Cholecystectomy、 laparoscopic、 gynecologic 為高風險。","B":"錯誤。「多藥物併用」效果優於單藥 (≥ 2 antiemetics for moderate risk)。","C":"錯誤。PONV 風險：女性、 不吸菸、 「年輕」 (非老年)、 PONV 史；肥胖非直接風險。","D":"錯誤。Propofol「降低」PONV (antiemetic)；opioid「增加」PONV — 描述部分正確但 propofol 反向。"},
    guidelines=["SAMBA 4th Consensus PONV 2020。","Apfel Score ≥ 2 → ≥ 2 antiemetics prophylaxis。"],
    points=["TIVA propofol < volatile for PONV","Multimodal opioid-sparing 降低 PONV","Rescue antiemetic 應用「不同 class」"],
    keyword="PONV, Apfel score, high-risk surgery",
    source="SAMBA 4th Consensus 2020")

# Q69 (C) Hypothermia 28-32°C
add(69, summary="術中體溫監控：「中度低體溫 28-32°C 可引起 sinus bradycardia + Osborn J 波 (hypothermia-specific EKG)」為正確敘述。",
    mechanism="低體溫分級：mild 33-35°C、 moderate 28-32°C、 severe < 28°C。EKG 變化：bradycardia、 PR/QT 延長、 J wave (Osborn wave) 在 moderate-severe；VF 在 < 28°C。",
    options={"A":"錯誤。麻醉第一小時體溫下降主要因「核心 → 周邊 redistribution」(non 周邊 → 核心)。","B":"錯誤。低體溫 SSI 風險「增加」(impaired immune function)，非減少。","C":"正確 (本題答案)。Moderate hypothermia 引起 bradycardia + J wave。","D":"錯誤。Core temperature 部位：pulmonary artery、 distal esophagus、 nasopharynx、 tympanic、 bladder；腋溫為 peripheral 不算 core。"},
    guidelines=["ASA Perioperative Temperature Management：active warming 維持 > 36°C。","NICE Inadvertent Perioperative Hypothermia Guidelines。"],
    points=["Hypothermia 後果：coagulopathy、 SSI、 cardiac event、 prolonged PACU","Active rewarming：forced air、 warm fluids、 warmed humidified gases","Core temperature monitoring 強制 if GA > 30 min"],
    keyword="Perioperative hypothermia, J wave, core temperature",
    source="ASA Practice Advisory; NICE Guidelines")

# Q70 (D) ERAS — Avoid NG/drain
add(70, summary="ERAS 核心：「避免常規使用鼻胃管 + 引流管」為正確 (傳統認為必要但 evidence 顯示無效甚至有害)。其他選項均錯。",
    mechanism="ERAS 原則：減少手術 stress、 改善 recovery、 enable bonding、 reduce LOS。Goal-directed fluid、 multimodal opioid-sparing、 early oral intake、 early mobilization、 normothermia。",
    options={"A":"錯誤。術前「避免常規 BZD」(delirium 風險)、 提前 carb drink 2h 而非過早輸液。","B":"錯誤。Bowel prep 「不建議」常規 (deplete fluid、 electrolyte、 無感染降低)。","C":"錯誤。Opioid「減少」非增加 (multimodal opioid-sparing)。","D":"正確 (本題答案)。避免常規 NG + drain 為 ERAS 標準。"},
    guidelines=["ERAS Society Colorectal Pathway。","Cochrane review：no benefit of routine NG drainage。"],
    points=["Carb-loading drink 2h pre-op 降低 insulin resistance","Goal-directed fluid (SVV-guided)","Multimodal analgesia: regional + non-opioid"],
    keyword="ERAS, NG tube, drain",
    source="ERAS Society Colorectal Guidelines")

# Q71 (C) TOF — Hypocarbia 不增 PVR
add(71, summary="TOF 麻醉避免 PVR 上升 — 「Hypocarbia (PaCO₂↓)」「降低」PVR (非增加)。Acidosis、 hypoxia、 PEEP 均增 PVR。",
    mechanism="Pulmonary vascular reactivity：acidosis、 hypoxia、 hypercapnia、 high PEEP、 sympathetic activation 均「增加」PVR；alkalosis、 hyperventilation、 normocapnia/mild hypocapnia「降低」PVR。",
    options={"A":"錯誤 (增加 PVR)。Acidosis 增 PVR。","B":"錯誤 (增加 PVR)。Hypoxia 為強 pulmonary vasoconstrictor (HPV)。","C":"正確 (本題答案，不增 PVR)。Hypocarbia 「降低」PVR。","D":"錯誤 (增加 PVR)。High PEEP overdistension → 增 PVR。"},
    guidelines=["AHA Congenital Heart Disease Guidelines。","TOF anesthesia goals：maintain SVR、 avoid hypovolemia、 avoid extreme tachycardia、 reduce RVOT spasm、 minimize PVR。"],
    points=["Tet spell：knee-chest、 O₂、 IV fluid、 phenylephrine、 morphine、 esmolol","Cyanotic CHD R-to-L shunt：avoid SVR drop","Repair at 3-6 months ideal"],
    keyword="Tetralogy of Fallot, PVR, hypocarbia",
    source="Coté and Lerman 6/e; AHA Guidelines")

# Q72 (C) Transfusion anaphylaxis
add(72, summary="輸 PRBC 2 單位後 SpO₂ 88%、 wheeze、 紅疹、 hypotension = transfusion anaphylaxis。處置：停輸血、 epinephrine、 IV fluid、 steroid、 antihistamine。「利尿劑」不適當 (anaphylaxis 多為低血容，diuretic 加重 hypotension)。",
    mechanism="Anaphylactic transfusion reaction：IgA deficient 病人 anti-IgA antibody + donor IgA → mast cell degranulation。或 plasma protein anaphylaxis。表現：bronchospasm、 urticaria、 angioedema、 hypotension、 GI symptoms。",
    options={"A":"正確。重新核對血品 + crossmatch (排除 hemolytic reaction)。","B":"正確。Fluid resuscitation + vasopressor 為必要。","C":"錯誤 (本題不適當)。Anaphylaxis 多 hypotension + capillary leak，diuretic 不適合。","D":"錯誤。應「使用 steroid」(prevent late phase reaction)，「不建議」描述為錯誤；但題目原意可能指 immediate steroid 對 acute anaphylaxis 效果有限，故描述為「不建議」。"},
    guidelines=["AABB Transfusion Reaction Management。","Anaphylaxis：Epinephrine 0.3-0.5 mg IM (or 0.01 mg/kg)、 fluid、 H1/H2 antagonist、 steroid。"],
    points=["IgA-deficient 病人需 IgA-deficient blood products","Premedication antihistamine + steroid for known reactor","TRALI、 TACO、 anaphylaxis 為主要急性反應"],
    keyword="Transfusion anaphylaxis, diuretic contraindication",
    source="AABB Technical Manual")

# Q73 (B) PPV → 胸腔內壓↑ → 低 BP
add(73, summary="腹腔手術前 + 機械通氣 + BP 80/53 + 其餘穩定：「機械通氣引起胸腔內壓↑ → venous return↓ → BP↓」，初步「fluid + ventilator setting 調整」。",
    mechanism="Positive pressure ventilation：intrathoracic pressure↑ → venous return↓ → CO↓ → BP↓。Healthy patient 通常代償，但 hypovolemia (NPO) 或 deep anesthesia 時更顯著。Initial：fluid bolus + reduce PEEP/TV。",
    options={"A":"錯誤。NPO 引起 hypovolemia → preload↓ (非 afterload↓)。","B":"正確 (本題答案)。PPV 增 intrathoracic pressure → venous return↓ → fluid + ventilator 調整。","C":"錯誤。BIS 40 為適當麻醉深度，不需 fentanyl bolus。","D":"錯誤。BIS 45 為適當深度，不應調高 MAC (反而加重 hypotension)。"},
    guidelines=["Goal-directed fluid management。","Lung-protective ventilation：TV 6-8 mL/kg IBW、 PEEP 5。"],
    points=["NPO + GA → preload-dependent","Fluid bolus 250-500 mL crystalloid","SVV/PPV 動態指標 > CVP 靜態"],
    keyword="Positive pressure ventilation, venous return, hypotension",
    source="Miller's Anesthesia 8/e Ch. 59 Fluid")

# Q74 (A) Kidney transplant MAP
add(74, summary="腎臟移植 reperfusion 期間 MAP 維持「> 80 mmHg (慢性 HTN 病人 baseline 15-20% within)」改善 graft perfusion。「MAP 60」過低，graft 灌流不足。",
    mechanism="Renal graft perfusion 嚴重依賴 MAP — 較高 MAP 改善 graft function。慢性 HTN 病人 autoregulation 右移，需更高 MAP 維持 perfusion。",
    options={"A":"錯誤 (本題不適當)。MAP 60 過低；應「> 80」或 baseline 15-20% within。","B":"正確。Fluid → vasopressor 為標準。","C":"正確。慢性 HTN：MAP baseline 15-20% within。","D":"正確。CVP monitoring 為標準 (10-15 cmH₂O)。"},
    guidelines=["KDIGO Perioperative AKI Guidelines。","Living donor kidney transplant outcome 較好。"],
    points=["Mannitol 25-50g + furosemide 20-40mg 促 diuresis","Avoid nephrotoxic drugs","Tacrolimus、 cyclosporine 主要 immunosuppression"],
    keyword="Kidney transplant, MAP target, reperfusion",
    source="KDIGO Perioperative AKI Guidelines")

# Q75 (B) Liver reperfusion — Hyperkalemia (非低)
add(75, summary="肝臟移植 reperfusion 引起「hyperkalemia」(non hypokalemia) + cardiac arrest。「心臟停止 + 低血鉀」為錯誤敘述 — 應為「高血鉀」+ peaked T wave。",
    mechanism="Liver reperfusion：cold preservation solution + 蓄積 K + lactate + cytokine 釋出 → hyperkalemia + acidosis + hypotension + arrhythmia。Hypothermia 加重 K elevation effect。",
    options={"A":"正確。Post-reperfusion syndrome：MAP↓ > 30% > 1 min + acidosis。","B":"錯誤 (本題錯誤)。應為「hyperkalemia」(非 hypokalemia)。","C":"正確。Hepatic artery thrombosis 需 emergent reoperation。","D":"正確。Hyperkalemia → peaked T wave + arrhythmia。"},
    guidelines=["ISMETT Liver Transplant Consensus。","Pre-reperfusion：hyperventilate、 increase preload、 Ca、 HCO₃、 vasopressor preparation。"],
    points=["VV bypass 與 piggyback 技術減少 caval clamp issues","TEG-guided coagulation factor replacement","Post-op ICU graft function monitoring"],
    keyword="Liver transplant reperfusion, hyperkalemia",
    source="ISMETT Liver Transplant Anesthesia")

# Q76 (B) Brain death organ donation ventilation
add(76, summary="腦死器捐 ventilator setting：「Tidal volume 6-8 mL/kg (lung-protective)」為適當；避免高 plateau pressure、 適度 PEEP、 normocapnia。",
    mechanism="腦死病人 lung-protective ventilation 維持 graft viability。Donor lung 對 high pressure + barotrauma 敏感；過度 PEEP 可影響 venous return。",
    options={"A":"錯誤。PSV 不適合腦死 (no respiratory drive)；應 AC/SIMV。","B":"正確 (本題答案)。TV 6-8 mL/kg IBW。","C":"錯誤。應「使用 PEEP 5-8」防 atelectasis (non avoid)。","D":"錯誤。Peak inspiratory pressure 36-40 過高；應 < 30 (plateau < 30)。"},
    guidelines=["OPTN/UNOS Donor Management Goals。","Lung protective ventilation 維持 donor lung viability。"],
    points=["Hormonal replacement (T4、 methylprednisolone、 vasopressin、 insulin)","Maintain MAP > 65、 SpO₂ > 95、 normothermia","Apnea test for brain death determination"],
    keyword="Brain death, organ donation, lung protective ventilation",
    source="OPTN/UNOS Donor Management Guidelines")

# Q77 (B) CPB heparin
add(77, summary="CPB heparin 標準劑量：「300-350 U/kg」；ACT target：「> 400 sec」(初始) 或 > 480 (最佳)。",
    mechanism="CPB 期間血液接觸 artificial surface → 強 thrombogenic → 需高劑量 heparin 完全 anticoagulate。ACT 為 bedside coagulation test，反映 intrinsic + common pathway。",
    options={"A":"錯誤。Dose 對但 ACT > 250 不足。","B":"正確 (本題答案)。300-350 U/kg + ACT > 400。","C":"錯誤。Dose 過低 (150-200 為 PCI/vascular surgery 用量)。","D":"錯誤。"},
    guidelines=["STS/SCA Cardiac Surgery Anesthesia。","ACT > 480 為 conservative target；> 400 為 minimum。"],
    points=["HIT 病人改用 bivalirudin","Protamine 1 mg per 100 U heparin reversal、 slow infusion","Antifibrinolytic (TXA、 ε-aminocaproic acid) 減少 bleeding"],
    keyword="CPB, heparin, ACT",
    source="STS/SCA Cardiac Surgery Anesthesia")

# Q78 (C) AS — Maintain SVR
add(78, summary="Severe AS 麻醉「維持高 SVR」(非降低)。「降低 SVR 以利 CO」為錯誤敘述 — AS 為 fixed obstruction，降 SVR 不增 CO 反而降冠脈灌流。",
    mechanism="Severe AS LV hypertrophic、 stiff、 preload-dependent、 無法即時增 stroke volume。SVR↓ → 系統 hypotension → 冠脈灌流↓ (especially subendocardial) → ischemia → arrhythmia → 死亡。",
    options={"A":"正確。Sinus rhythm + atrial kick (30% CO)、 緩慢 HR 為 critical。","B":"正確。LVEDP 升高維持 preload 灌注 hypertrophic LV。","C":"錯誤 (本題錯誤)。應「維持高 SVR」非降低。Phenylephrine 為 vasopressor of choice。","D":"正確。避免心肌抑制 (propofol high dose) 加重心衰。"},
    guidelines=["ACC/AHA 2014 Valvular Heart Disease。","TAVR 高風險病人替代 open AVR (PARTNER trial)。"],
    points=["Coronary perfusion 嚴重依賴 diastolic BP","心律不整 (especially AF) 失 atrial kick (30% CO)、 致命","TEE 監測 LV function 與 valve gradient"],
    keyword="Severe AS, SVR, hemodynamic goal",
    source="ACC/AHA 2014 Valvular Heart Disease")

# Q79 (C) Aortic unclamp — Volume preload
add(79, summary="主動脈夾鉗鬆開前「靜脈輸液 volume preload」(避免 venous pooling 引起 hypotension) 最有效防止血壓下降。",
    mechanism="Aortic unclamp 引起：(1) 下肢 vasodilation (release of ischemic metabolite) → SVR↓；(2) Venous pooling → preload↓；(3) Acidosis、 hyperkalemia 釋出。Volume preload 為最有效預防。",
    options={"A":"錯誤。減麻醉藥對 unclamp hypotension 效果不可靠。","B":"錯誤。Inotrope 不解決 volume + vasodilation。","C":"正確 (本題答案)。Volume preload 為標準預防。","D":"錯誤。NaHCO₃ 在 acidosis 時用，非預防性。"},
    guidelines=["Vascular Surgery Anesthesia Guidelines：staged unclamp + volume preload + 預備 vasopressor。","ECG + invasive BP monitoring throughout。"],
    points=["Slow gradual unclamp 減少 sudden hemodynamic change","Hyperkalemia management 預備 (Ca、 insulin)","Permissive hypertension during clamp"],
    keyword="Aortic unclamp, volume preload, vascular surgery",
    source="Miller's Anesthesia 8/e Ch. 71 Vascular Surgery")

# Q80 (B) Amiodarone for post-thoracotomy AF
add(80, summary="肺葉切除術後 AF 預防：reactive airways disease 病人「Amiodarone」為合適 (對 airway 影響小)。β-blocker (labetalol) 對 bronchospasm 病人禁忌。",
    mechanism="Post-thoracotomy AF (30-50%)：lung resection + 自律神經失衡 + 發炎。Prevention：β-blocker (但 reactive airway 禁忌)、 amiodarone (Class III、 對 airway 影響小)、 magnesium。",
    options={"A":"錯誤。Labetalol (β-blocker) 在 reactive airway 為禁忌。","B":"正確 (本題答案)。Amiodarone 對 airway 影響小，適合此族群。","C":"錯誤。Nicardipine 為 calcium channel blocker、 主要 HTN 控制，非 AF 預防首選。","D":"錯誤。Adenosine 為 SVT 急救，非預防 AF。"},
    guidelines=["AHA AF Guidelines + Post-thoracotomy AF prevention。","Amiodarone 300 mg IV over 1h + 900 mg/24h。"],
    points=["Amiodarone 副作用：thyroid dysfunction、 pulmonary fibrosis、 hepatotoxicity (chronic use)","Magnesium 補充 maintain K > 4、 Mg > 2","Rate control vs rhythm control 個別評估"],
    keyword="Post-thoracotomy AF, amiodarone, reactive airway",
    source="AHA AF Guidelines")


# Apply enhancements
with open('/tmp/np-anesthesia/questions.json') as f:
    qs = json.load(f)

updated = 0
for q in qs:
    if q['year'] != 113 or q['specialty'] != 'anesth_advanced':
        continue
    n = int(re.search(r'-A(\d+)$', q['id']).group(1))
    if n in E:
        q['explanation'] = E[n]
        if 'source' in E[n]:
            q['source'] = E[n]['source']
        updated += 1

print(f"Enhanced {updated}/80 questions for 113 進階麻醉")

with open('/tmp/np-anesthesia/questions.json', 'w') as f:
    json.dump(qs, f, ensure_ascii=False, separators=(',', ':'))

import os
print(f"File size: {os.path.getsize('/tmp/np-anesthesia/questions.json')/1024:.0f}KB")
