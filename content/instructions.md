## Informal instructions for contributors

Language contributors are linguists with expertise in the target language whose task is to elicit the necessary translations from native speakers and to provide them in the form accessible to "coders". Contributor’s main goal is to provide **adequate** translations of stimulus sentences and to identify **nominal causal markers** employed (if any).

Main **adequateness** criteria are semantic **precision** (the same meaning as in the stimulus sentence) and **naturalness**. Equivalents that fail to meet these criteria do not make their way into the database (but can be mentioned in comments).

Glosses should be provided in a separate line (no alignment needed). Grammatical labels must be in the upper case (ERG, PST, etc.).

If the sentence obtained is semantically different from the questionnaire stimulus, the actual back translation of the sentence obtained must be provided.

Alternative translational equivalents are welcome. If a given stimulus sentence has more than one equivalent, one of the equivalents must be marked as “main” (other equivalents will be marked “alternate”) based on their naturalness / frequency.

## Informal instructions for coders

A coder is a representative of the NoCaCoDa database who interacts with language contributors and is responsible for preparing spreadsheets that comply with the database’s substantive and technical conventions. The coder’s interaction with language contributors should result in two spreadsheets per language:
1) languagename_data.csv (e.g., “French_data.csv”): entries in this spreadsheet correspond to individual translations of the questionnaire sentences into the target language
2) languagename_markers.csv (e.g., “French_markers.csv”): entries in this spreadsheet correspond to all different nominal causal markers encountered in the languagename_data.csv spreadsheet

### Preparing the spreadsheet with translations (languagename_data.csv)

The following fields must be present in the spreadsheet

-   	“language_no”: 1, 2, etc.
-   	“language_name”: “Khmer”, “Russian”, etc.
-   	“stimulus_no”: “1”, “2”, ... “50”. Remember that alternative translational equivalents are welcome if provided by native speakers. In (29), for example, Russian should allow both iz-za + GEN and po vine + GEN
-   	“status”: “main” or “alternate”. For some calculations, alternative equivalents will be disregarded, in this case only equivalents marked as “main” will be taken into account. It is possible that this status (“main”) is given to a construction that does not meet the inclusion criteria (see below). For example, if the most neutral way to convey the relevant meaning in the target language is to use a verbal (bi-clausal) construction, but there is also a marginal nominal causal construction as an alternative, then the verbal construction is marked “main”, and the nominal construction is marked “alternate”. Even when there is no information on one of the several alternatives being more felicitous than the other(s), only one equivalent has to be coded as “main” and all other as “alternate”.
-   	“causal_marker”: “iz_GEN”, “INS”, etc. Causal markers are identified if and only if the adequate translation equivalent obtained meets the inclusion criteria. The main criteria are: i) the causing event is syntactically represented by a noun phrase. The minimal necessary condition is compatibility of its head with unquestionably nominal marking; thus, English gerunds can be considered “syntactically nouns” (“because of doing”), while English infinitives cannot (“*because of (to) do”). The condition, however, is not sufficient: a final decision on the interpretation of a particular form is taken based on the informed opinion of the language expert; ii) this noun phrase has approximately the same meaning as the English/Russian noun phrase in the stimulus sentence; iii) this noun phrase is not a syntactic subject (i.e., sentences like ‘The tears made the handkerchief wet’ are not included). Translational equivalents that do not meet the inclusion criteria should have “n.a.” in the causal_marker field. Rule of thumb: language-specific markers are given in the form of their main allomorph, no diacritics, lower case; category labels are given in upper case.
-   	“sentence”. One sentence in the target language. Words are separated by spaces, morpheme boundaries are shown as in the Leipzig glossing rules. Leave blank if no equivalent translation has been obtained.
-   	“glosses_en”. Use Leipzig glossing rules. Words are separated by spaces.
-   	“back_translation_en”. This is important because the sentence obtained can diverge in minor details from the stimulus given in the questionnaire.
-   	“glosses_ru”. Use Leipzig glossing rules. Words are separated by spaces.
-   	“back_translation_ru”. This is important because the sentence obtained can diverge in minor details from the stimulus given in the questionnaire.
-   	“comments”. This field is especially relevant if no adequate translation has been obtained, or it fails to meet the inclusion criteria, etc. Standard phrases should be used in similar situations.
-   	“comments_informal”. This field is intended for informal comments (possibly in Russian).

### Preparing the spreadsheet with nominal causal markers (languagename_markers.csv)

Two spreadsheets per language: languagename_data.csv and languagename_markers.csv (e.g. “Russian_data.csv” and “Russian_markers.csv”) 
This document introduces the tags used for annotating causal markers. Each marker is annotated for i) whether it can explicitly convey the causal semantics and ii) the basic non-causal meaning macro-types it displays. 
Fields in languagename_markers.csv:
Column A: “language_no”
Column B: “language_name”
Column C: “causal_marker” 
All markers should be identified and spelled in exactly the same way as in languagename_data; see Instructions_coders_languagename_data for detailed guidelines
Column D: “morphosyntactic_type”
The following types are possible
adposition (possibly in combination with a specific case)
affix (typically a case marker, but also any other kind of affix)
Column E: explicitness
The rationale behind this parameter is that some translations do meet the acceptance criteria for the inclusion in the nominal causal constructions dataset, but the relevant nominal markers cannot explicitly convey causal meaning sensu stricto.  This parameter allows three values.
no (= contextual causal marker) — causal interpretation, if present, is only an implicature, e.g., Fr. sous ‘under’ as in La branche s’est cassée sous le poids de l’oiseau, lit. ‘The branch broke under the weight of the bird’ (note that the causal meaning can be cancelled in a wider context, along the lines of Quoique la branche se soit cassée sous le poids de l’oiseau, c’était en fait parce qu'elle était desséchée et déjà morte). Criteria for tagging a marker as contextual (= “no”) are as follows. A) Markers that can only signal a cause-like noun phrase in the context of specific verbs, i.e. verbs where the relevant NP is an argument (is implied by the verb’s meaning), are considered contextual. Russian na + Accusative case, as in Žen-a rasserdi-l-a-sʹ na slov-a muž-a [wife(F)-NOM.SG get.mad(PFV)-PST-F.SG-REFL on word(N)-ACC.PL husband(M)-GEN.SG], (13) ‘The wife was angered <by> [her husband’s words]’), is a case in point. B) Other criteria are taken into account only if the marker is not lexically restricted in terms of governing verbs. These criteria are B1) cancellability (see French sous above), and B2) lack of overt mentioning of cause among the marker’s meanings in available dictionaries or grammars. NB: None of the “non-causal” meanings (discussed below) should be taken into account while estimating the explicitness of a marker. Thus, markers such as Rus. soglasno + DAT ‘according to’ are also considered contextual (their basic meaning is classified as belonging to the Instrument macro-type, see section “pattern” below). 
yes (= explicit causal marker) — the marker has, at least in part of its usages, an explicitly causal meaning that cannot be cancelled, e.g., Eng. from as in The man died from electric shock. Oblique markers that signal non-agentive effectors / natural forces (as, e.g., the Instrumental case in Rus. Derev-o povali-l-o vetr-om [tree(N)-ACC.SG bring.down(PFV)-PST-N.SG wind(M)-INS.SG], (6) ‘The tree fell due to the wind’) are considered explicit. Criteria for tagging a marker as explicit are as follows. A) The marker must be found in some semantically causal contexts where the choice of the marker is not determined by the governing pattern of a specific verb. If this criterion is met, two further criteria are B1) uncancellability and B2) a straightforward indication of the causal meaning in a dictionary or a grammar description. Meeting any of the criteria B1 or B2 is sufficient for considering a marker explicit (“yes”).
uncertain — the explicitness can not be satisfactorily estimated for the time being. This decision should be taken if either it is not clear whether the marker can be used to signal cause other than in the contexts of specific verbs where the cause is part of the argument frame (criterion A) or if the A criterion for explicitness is met, but there is not enough reliable information for criteria B1) and B2).
Columns F-L: non-causal meanings
Many nominal markers attested in the dataset can convey non-causal (e.g., spatial) meanings as well. For explicit causal markers, it can result in syncretism, while contextual causal markers have other meaning(s) “by definition”. The most salient and context-independent meanings are classified into five macro-types, labelled  “goal”, “instrument”, “source”, “location”, and “object”. Each macro-type comprises one or several meanings, the name of the macro-type being the name of one of its meanings. The grouping into macro-types is based on typological knowledge on semantic proximity between specific meanings, as represented in the form of, e.g., semantic maps. These macro-types are not mutually exclusive: a certain marker can display more than one syncretic non-causal meaning. There is also an additional sixth type “other”, a residual category that covers relatively rare non-causal meanings. Each marker is tagged with “yes” or “no” for each of the macro-types, “yes” is chosen if the marker in question is productively used at least in one of the macro-type meanings. A marker with six “no”s is a dedicated causal marker.
goal — endpoint of the motion, as Eng. to in He went to the village.
This macrotype also includes the following meanings:
Recipient — participant who receives something as a result of the transition, as Eng. to in He gave the book to Mary. 
Beneficiary — participant who is (dis)advantaged as a result of the action, as Eng. for in He bought a present for Mary.
Purpose (non-spatial Goal)  — aim or intention of an action, as Eng. for in He is saving money for a trip abroad.
instrument — entity that is used by the agent to perform the action but remains unaffected, as Eng. with in He writes with a pen.
This macrotype also includes the following meanings:
Means — entity that is indirectly used to perform the action, as Eng. through in He gained support through bribes.
Path — location along / over / through which the motion takes place, as Eng. through in He walked through the forest.
Pattern — entity in conformity with which the situation unfolds, as Eng. under in He was fined under the new law.  
Comitative — co-participant of the action, as Eng. with in He came with Mary.
location — stative location relative to some other participant or entity (landmark), as Eng. in in He stays in bed.
object —P-participant in the basic transitive construction, as Eng. object pronoun form, e.g. me, in He hit me.
This macrotype also includes the following meanings:
Matter — participant or entity under consideration or discussion, as Eng. about in They talked about the trip.
source — starting point of the motion, as Eng. from in He moved from there last year. 
This macrotype also includes the following meanings:
Temporal starting point — entity designated as temporal reference for the situation, as Eng. since in He has been waiting since morning.
Anterior reference — entity designated as temporally anterior to the situation, as Eng. after in He sold the car after the accident.
other — non-causal meanings not covered under any other macro-type. The positive value of this parameter is mutually exclusive with that in the other macro-types: the “yes” value is only chosen in cases where the marker in question has distinct non-causal meanings none of which falls under the macro-types above. For dedicated causal markers, this parameter should have “no”, in all other cases, “n.a.”.
other_details — explication of the non-causal meanings defined in “other” (given in prose: no preset values).


