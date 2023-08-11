## How to read the data

Each full entry in the database contains a stimulus sentence from the [questionnaire](https://nocacoda.info/questionnaire.html) translated into a target language and annotated for a number of parameters. The dataset containing all full entries in a single spreadsheet is available [here](https://nocacoda.info/data_in_one_spreadsheet.html). The annotations used in the database come from three sets:

1. Semantic parameters associated with individual stimulus sentences.
2. Parameters associated with individual translations into target languages.
3. Parameters associated with language-specific nominal causal markers.

Apart from this, the database also features generalized data pertaining to the level of individual languages. These data are visible in the aggregate table [here](https://nocacoda.info/langlist.html). The four sets of annotations are explained below.

### Inclusion criteria

The translations obtained are considered a part of the database only if they meet the inclusion criteria. Nonetheless, the translations that failed to meet the inclusion criteria are visible to database users (often this serves as a way to explain the nature of the difficulties encountered). Sentences that failed to meet the inclusion criteria are not tagged for their causal marker (see ‘Parameters associated with individual translations into target languages’ below) and do not participate in any calculations based on the data. 

The inclusion criteria are as follows:

1. The causing event is syntactically represented by a noun phrase. The minimal necessary condition is the compatibility of its head with unquestionably nominal marking; thus, English gerunds can be considered “syntactically nouns” (*because of doing*), while English infinitives cannot (* *because of (to) do*).
2. This noun phrase has approximately the same meaning as the English/Russian noun phrase in the stimulus sentence.  
3. This noun phrase is not a syntactic subject (i.e., sentences like ‘The tears made the handkerchief wet’ are not included).

### Semantic parameters associated with individual stimulus sentences

Stimulus sentences are identified by numeric codes (“stimulus_no”: 1, 2, … 54). The 54 stimulus sentences were preannotated for five semantic parameters:

- Semantic type: ontological vs. epistemic vs. logical vs. illocutive.
- Objective vs. subjective causes.
- Direct vs. indirect causes.
- Internal vs. external causes.
- Taxis: simultaneous vs. anterior.

These parameters are explained in the [Questionnaire](https://nocacoda.info/questionnaire.html) section. Their values ascribed to the stimulus sentences are inherited by the entries in the final dataset. 

### Parameters associated with individual translations into target languages

Each entry in the dataset contains the following fields:

- “language_no”   
This is a conventional number (1, 2, …) associated with a given language in the database (for example, 1 is English, 2 is Japanese, etc.). 
This field is mainly used for linking purposes.
 
- “language_name”  
“English”, “Japanese”, etc.
 
- “stimulus_no”  
A numeric code of the stimulus sentence (1, 2, … 54), primarily used for linking purposes.
 
- “status”  
This parameter has two values: “main” vs. “alternate”. For each combination of the stimulus sentence and target language exactly one entry is tagged as “main”. All other entries are tagged as “alternate” (their number is in principle unlimited). The choice of the “main” translation is driven by the criteria of naturalness (when possible, operationalized in terms of frequency) and translational accuracy.
 
- “causal marker”  
This is the main dependent variable in the database. In this field, language-specific markers are given in the form of their main allomorph, with no diacritics and in lower case; grammatical labels are given in upper case. E.g., the marker in the German sentence *Der Lehrer lobte den Schüler für seine Kleidung* ‘The teacher commended the student for his suit’ is tagged as “fur_ACC”. In case the translation obtained does not meet the inclusion criteria (see ‘Inclusion criteria’above) this field is filled in as “n.a.”.

- “sentence”  
The sentence in the target language with morpheme boundaries.
 
- “glosses_en”  
English glosses
 
- “back_translation_en”  
Back translation of the target-language sentence to English. This is useful if the meaning of the sentence obtained deviates from the questionnaire stimulus.
 
- “glosses_ru”  
Russian glosses.
 
- “back_translation_ru”  
Back translation of the target-language sentence to Russian. This is useful if the meaning of the sentence obtained deviates from the questionnaire stimulus.
 
- “comments”  
This field contains additional information that is deemed important for the database user. If the sentence obtained fails to meet the inclusion criteria this field contains an explanation.

- “comments_informal”  
Any additional comments intended for internal use only (possibly in Russian).
 
### Parameters associated with language-specific nominal causal markers
 
Each language-specific causal marker was tagged for its morphosyntactic type, degree of explicitness, and polysemy/syncretism. These values are inherited by the full database entries. The following fields belong to this set of annotations:
 
- “language_no”: see above
 
- “language_name”: see above
 
- “causal_marker”: see above
 
- “morphosyntactic type”  
The following values are possible: “adposition” (possibly in combination with a specific case) and “affix” (typically a case marker, but also any other kind of affix).
 
- “explicitness”  
The rationale behind this parameter is that some translations do meet the acceptance criteria for the inclusion in the dataset, but the relevant nominal markers cannot explicitly convey causal meaning *sensu stricto*. This parameter can take three values:
  - no (= contextual causal marker) — causal interpretation, if present, is only an implicature, e.g., Fr. *sous* ‘under’ in *La branche s’est cassée sous le poids de l’oiseau*, lit. ‘The branch broke under the weight of the bird’ (note that the causal meaning can be cancelled in a wider context, along the lines of *Quoique la branche se soit cassée sous le poids de l’oiseau, c’était en fait parce qu'elle était desséchée et déjà morte* ‘Although the branch broke under the weight of the bird, it was in fact because it was dried out and already dead’).
  - yes (= explicit causal marker) — the marker has, at least in part of its usages, an explicitly causal meaning that cannot be cancelled, e.g., Eng. *from* in *The man died from electric shock*. Oblique markers that signal non-agentive effectors / natural forces (e.g., the Instrumental case in Rus. *Derev-o povali-l-o vetr-om* \[tree(N)-ACC.SG bring.down(PFV)-PST-N.SG wind(M)-INS.SG\], ‘The tree fell due to the wind’) are considered explicit.
  - uncertain — the explicitness cannot be satisfactorily estimated for the time being.

**Fields related to non-causal meanings of markers**

Many nominal markers attested in the dataset can convey non-causal (e.g., spatial) meanings as well. For explicit causal markers, it can result in syncretism, while contextual causal markers have other meaning(s) “by definition”. The most salient and context-independent meanings are classified into five macro-types, labelled “goal”, “instrument”, “source”, “location”, and “object”. Each macro-type comprises one or several meanings, the name of the macro-type being the name of one of its meanings. These macro-types are not mutually exclusive: a certain marker can display more than one syncretic non-causal meaning. There is also an additional sixth type “other”, a residual category that covers relatively rare non-causal meanings. Each marker is tagged with “yes” or “no” for each of the macro-types; “yes” is chosen if the marker in question is productively used with at least one of the macro-type meanings. A marker with six “no”s is a dedicated causal marker.

- “goal”  
Endpoint of motion, e.g., Eng. *to* in *He went to the village*. This macrotype also includes the following meanings:
  - Recipient — participant who receives something as a result of the transition, e.g., Eng. *to* in *He gave the book to Mary*.
  - Beneficiary — participant who is (dis)advantaged as a result of the action, e.g., Eng. *for* in *He bought a present for Mary*.
  - Purpose (non-spatial Goal)  — aim or intention of an action, e.g., Eng. *for* in *He is saving money for a trip abroad*.

- “instrument”  
Entity that is used by the agent to perform the action but remains unaffected, e.g., Eng. *with* in *He writes with a pen*. This macrotype also includes the following meanings:
  - Means — entity that is indirectly used to perform the action, e.g., Eng. *through* in *He gained support through bribes*.
  - Path — location along/over/through which the motion takes place, e.g., Eng. *through* in *He walked through the forest*.
  - Pattern — entity in conformity with which the situation unfolds, e.g., Eng. *under* in *He was fined under the new law*.
  - Comitative — co-participant of the action, e.g., Eng. *with* in *He came with Mary*.

- “location”  
Stative location relative to some other participant or entity (landmark), e.g., Eng. *in* in *He stays in bed*.
 
- “object”  
P-participant in the basic transitive construction, e.g., Eng. object pronoun form *me* in *He hit me*. This macrotype also includes the following meaning:
  - Matter — participant or entity under consideration or discussion, e.g., Eng. *about* in *They talked about the trip*.
 
- “source”  
Starting point of the motion, e.g., Eng. *from* in *He moved from there last year*. This macrotype also includes the following meanings:
  - Temporal starting point — entity designated as temporal reference for the situation, e.g., Eng. *since* in *He has been waiting since morning*.
  - Anterior reference — entity designated as temporally anterior to the situation, e.g., Eng. *after* in *He sold the car after the accident*.
 
- “other”  
Non-causal meanings not covered under any other macro-type. The “yes” value is only chosen in cases where the marker in question has distinct non-causal meanings none of which falls under the macro-types above; for dedicated causal markers, this parameter should have “no”; if at least one other macro-type is applicable, this parameter is marked as “n.a.”.
 
- “other_details”  
Explication of the non-causal meanings defined in “other” (given in prose: no preset values).
 
### Parameters associated with individual languages

Several parameters are identified at the level of individual languages. Some of them were predefined, while others summarize the results obtained with the help of the database. The spreadsheet with the values of these parameters can be seen [here](https://nocacoda.info/langlist.html). The following parameters are used:
 
- “Language”
 
- “Glottocode”
 
- “Macroarea”  
We use the following partition of the world into macroareas: Australia; East and Southeast Asia; Europe; Mesoamerica; North Africa; North America; North and Central Asia; Papunesia; South America; South Asia; Sub-Saharan Africa; West Asia and the Caucasus.
 
- “Family (WALS)”  
Genealogical affiliation of the language according to the two-level classification given in WALS, where “Family” is the top level (e.g., Indo-European).
 
- “Genus (WALS)”  
Genealogical affiliation of the language according to the two-level classification given in WALS, where “Genus” is the bottom level (e.g., Baltic).
 
- “Latitude”  
Language coordinates typically follow WALS or Glottolog.
 
- “Longitude”  
Language coordinates typically follow WALS or Glottolog.
 
- “Contact language”  
The language of the questionnaire that was used for eliciting the data, mainly English or Russian.
 
- “Main”  
The total number of translations obtained that met the inclusion criteria and were tagged as “main”.
 
- “Alternate”  
The total number of translations obtained that met the inclusion criteria and were tagged as “alternate”.
 
- “Explicit”  
The total number of translations obtained that met the inclusion criteria and were simultaneously tagged as “main” and “explicit”.
 
- “Implicit”  
The total number of translations obtained that met the inclusion criteria and were simultaneously tagged as “main” and “implicit”.
 
- “Goal”, “Instrument”, “Location”, “Object”, “Source”, “Other”, “Dedicated”  
These seven fields summarize the types of syncretism observed in the language’s dataset. By default, these fields display the total number of the target-language sentences with causal markers displaying the given syncretism type. Only translations that met the inclusion criteria and were simultaneously tagged as “main” and “explicit” were taken into consideration. In case a marker used in a given translation simultaneously displays several types of syncretism, its score of “1” is divided by the number of its syncretism patterns (for example, a sentence with the English preposition *by* contributes 0.5 as its “instrument” score and 0.5 as its “location” score).
 
- “markers”  
The total number of different explicit causal markers observed in the language’s dataset.
