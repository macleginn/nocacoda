## Instructions for contributors

Language contributors are linguists with expertise in the target language whose task is to elicit the necessary translations from native speakers and to provide them in the form accessible to "coders". Contributor’s main goal is to provide **adequate** translations of stimulus sentences and to identify **nominal causal markers** employed (if any).

Main **adequateness** criteria are semantic **precision** (the same meaning as in the stimulus sentence) and **naturalness**. Equivalents that fail to meet these criteria do not make their way into the database (but can be mentioned in comments).

Glosses should be provided in a separate line (no alignment needed). Grammatical labels must be in the upper case (ERG, PST, etc.).

If the sentence obtained is semantically different from the questionnaire stimulus, the actual back translation of the sentence obtained must be provided.

Alternative translational equivalents are welcome. If a given stimulus sentence has more than one equivalent, one of the equivalents must be marked as “main” (other equivalents will be marked “alternate”) based on their naturalness / frequency.

## Instructions for coders

A coder is a representative of the NoCaCoDa database who interacts with language contributors and is responsible for preparing spreadsheets that comply with the database’s substantive and technical conventions. The coder’s interaction with language contributors should result in two spreadsheets per language:

1) languagename_data.csv (e.g., “French_data.csv”): entries in this spreadsheet correspond to individual translations of the questionnaire sentences into the target language.

2) languagename_markers.csv (e.g., “French_markers.csv”): entries in this spreadsheet correspond to all distinct nominal causal markers found in theprevious spreadsheet.

### Preparing the spreadsheet with translations (languagename_data.csv)

The following fields must be present in the spreadsheet:

- “language_no”: 1, 2, etc.
- “language_name”: “Khmer”, “Russian”, etc.
- “stimulus_no”: “1”, “2”, ... “50”. Remember that alternative translational equivalents are welcome if provided by native speakers. In (29), for example, Russian should allow both *iz-za* + GEN and *po vine* + GEN, and the two entries must have the same "stimulus_no".
- “status”: “main” or “alternate”. For some calculations, alternative equivalents will be disregarded, in this case only equivalents marked as “main” will be taken into account. It is possible that this status (“main”) is given to a construction that does not meet the inclusion criteria (see below). For example, if the most neutral way to convey the relevant meaning in the target language is to use a verbal (bi-clausal) construction, but there is also a marginal nominal causal construction as an alternative, then the verbal construction is marked “main”, and the nominal construction is marked “alternate”. Even when there is no information on one of the several alternatives being more felicitous than the other(s), only one equivalent has to be coded as “main” and all other as “alternate”.
- “causal_marker”: “iz_GEN”, “INS”, etc. Causal markers are identified if and only if the adequate translation equivalent obtained meets the inclusion criteria. The main criteria are: i) the causing event is syntactically represented by a noun phrase. The minimal necessary condition is compatibility of its head with unquestionably nominal marking; thus, English gerunds can be considered “syntactically nouns” (“because of doing”), while English infinitives cannot (“*because of (to) do”). The condition, however, is not sufficient: a final decision on the interpretation of a particular form is taken based on the informed opinion of the language expert; ii) this noun phrase has approximately the same meaning as the English/Russian noun phrase in the stimulus sentence; iii) this noun phrase is not a syntactic subject (i.e., sentences like ‘The tears made the handkerchief wet’ are not included). Translational equivalents that do not meet the inclusion criteria should have “n.a.” in the causal_marker field. Rule of thumb: language-specific markers are given in the form of their main allomorph, no diacritics, lower case; category labels are given in upper case.
- “sentence”. One sentence in the target language. Words are separated by spaces, morpheme boundaries are shown as in the Leipzig glossing rules. Leave blank if no equivalent translation has been obtained.
- “glosses_en”. Use Leipzig glossing rules. Words are separated by spaces.
- “back_translation_en”. This is important because the sentence obtained can diverge in minor details from the stimulus given in the questionnaire.
- “glosses_ru”. Use Leipzig glossing rules. Words are separated by spaces.
- “back_translation_ru”. This is important because the sentence obtained can diverge in minor details from the stimulus given in the questionnaire.
- “comments”. This field is especially relevant if no adequate translation has been obtained, or it fails to meet the inclusion criteria, etc. Standard phrases should be used in similar situations.
- “comments_informal”. This field is intended for informal comments (possibly in Russian).

### Preparing the spreadsheet with nominal causal markers (languagename_markers.csv)

The following fields must be present in the spreadsheet:
- “language_no” (as in languagename_data.csv).
- “language_name” (as in languagename_data.csv).
- “causal_marker”. All markers should be identified and spelled in exactly the same way as in languagename_data.csv.
- “morphosyntactic_type”. See howtoreadthedata for details.
- "explicitness". See howtoreadthedata for details.
- non-causal meanings (Columns F-L). See howtoreadthedata for details.
