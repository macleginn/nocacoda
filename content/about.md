## Project description

### Background and goals

All languages we are aware of possess *nominal causal constructions*, that is, constructions where the causing event is syntactically represented by a noun phrase, cf. *The woman woke up from \[the noise\]* or *The woman can’t fall asleep because of \[the mosquitoes\]* in English. Any nominal causal construction minimally involves a causal noun phrase (such as *the noise* and *the mosquitoes* in the examples above) and, crucially, a nominal causal marker (such as *from* and *because of* in the examples above). In some languages, nominal causal constructions seem to play a relatively minor role and the causal meaning is for the most part rendered by clausal causal constructions, such as *The woman can’t fall asleep because there are mosquitoes*, which are commonly believed to be the basic syntactic type for expressing causal semantics (Zaika 2019; Say in print). Nominal causal constructions display some parallelism with clausal causal constructions.

(While there is no generally accepted non-circular definition of the causal meaning as such, and some even think such a definition is not feasible, there is some degree of consensus as to which syntactic constructions should be considered causal. For the purposes of this project, the causal meaning will be viewed as a semantic primitive).

There is ample cross-lingual evidence to the effect that languages typically possess several competing nominal causal constructions that carve out different, even if overlapping, parts in the semantic domain of cause, as exemplified by the two introductory examples from English above. A significant number of detailed studies have identified semantic parameters that govern the choice between nominal causal constructions in individual languages, such as English (Radden 1985; Dirven 1995), Russian (Iordanskaia, Mel'chuk 1996; Levontina 2003; Klangová 2017), Serbian (Ivić 1954; Kovačević 1988), Czech (Klangová 2017), Lithuanian (Valiulytė 1998). However, we are not aware of similar studies based on less well studied languages outside of Europe; large-scale typological inquiries in this domain are also lacking. 

Our goal is to partially fill this gap. In particular, we aim at answering the following questions:

- What morphosyntactic types of markers (case affixes, adpositions, and less common variants) are involved in nominal causal constructions in the languages of the world?
- What types of spatial and non-spatial cognitive schemas are involved in the grammaticalization and semantic-change patterns, as manifested in the polysemy patterns displayed by individual nominal causal markers, such as cases and adpositions?
- What semantic parameters condition the choice between competing nominal causal constructions in individual languages?
- To what extent are systems of nominal causal constructions (dis)similar across languages?
- To what extent are these (dis)similarities conditioned by genealogical, areal, and more general typological factors, such as word order, richness of nominal morphology, preference for balanced/deranked dependent clauses, etc.

### General design of the database

The cornerstone of the database is the [questionnaire]({{ site_url_j }}/questionnaire.html) containing 54 stimulus sentences. These sentences were designed in such a way that their translational equivalents in individual languages are expected to meet our definition of the nominal causal construction with considerable likelihood. However, there can be no *a priori* guarantee that this would be the case because individual languages can prefer other types of structures, e.g. clausal causal constructions, for the expression of some of the meanings covered in the questionnaire. The translations that did not meet the definition were marked as such and excluded from calculations.

Language-specific studies focused on the distribution of nominal causal constructions in languages such as English and Russian (see the references above) often describe these distributions in terms of specific semantic parameters and their values, such as, e.g., the contrast between direct and indirect causes, external and internal causes, etc. Theoretically, a typological questionnaire could be based on such parameters rather than exemplar sentences. However, we decided against implementing such an approach for the following three reasons:

- It necessarily presupposes identical semantic contrasts in individual languages;
- It relies on the assumption that constructions characterized by the same set of gross semantic values should necessarily involve the same markers;
- It would make it impossible to discover relevant contrasts that are not known from a few major European languages.

At the same time, we expected to see some typological relevance in the semantic parameters that were known from previous language-specific studies. As a compromise, we compiled our questionnaire of 54 sentences such that:

- It does cover various combinations of the semantic parameters known from the literature. The 54 stimulus sentences were annotated for five semantic parameters on *a priori* grounds.
- Each combination of values is contextualized in the form of one or several specific sentences, which should provide for a more robust data collection process and make it possible to probe for further potentially relevant parameters.

### Workflow

The data sets for individual languages were provided by specialists in respective languages, who are referred to as *contributors*. The data sets are fully based on primary data elicited from native speakers (in some cases, contributors were native speakers themselves). It was the contributor’s responsibility to prepare a coherent data set, to interlinearize the examples, to identify nominal causal markers employed in individual translations, and to help with further annotations when necessary. The contributors were instructed to register multiple translational equivalents when they were available. However, for each stimulus sentence a maximum of one translation was tagged as “main” based on criteria of naturalness and/or frequency, whereas all other translations, if provided, were tagged as “alternate”. The distinction between “main” and “alternate” translation can be relevant for data interpretation, as some of the statistical techniques employed do not easily take variability into account.

At the next stage of data processing, each nominal causal marker was tagged for its morphosyntactic type, degree of explicitness, and polysemy / syncretism as discussed in [How to read the data]({{ site_url_j }}/howtoreadthedata.html). This markup as well as the final technical preparation of the data set for the inclusion in the database was done by *coders*, namely [Natalia Logvinova, Sergey Say, or Elizaveta Zabelina]({{ site_url_j }}/team.html). Whenever possible, the coders consulted available grammatical descriptions and discussed controversial cases with the contributors.

The data collected within the framework of the project are subject to analysis in a multitude of perspectives: semantic, cognitive, areal, etc. Some results of these endeavors are available in the [Publications]({{ site_url_j }}/publications.html) section.

### History of the project

NoCaCoDa emerged as part of the research project “Causal Constructions in World Languages (Semantics and Typology)” supported by a grant from the Russian Science Foundation (grant No. 18-18-00472, Principal Investigator V. S. Xrakovskij). This database was envisaged during the first stage (2018–2020) of the project and actually created and made publicly available during its second stage (2021–2022). Throughout this period, Natalia Zaika co-ordinated the project at large; she was also responsible for a similar subproject devoted to clausal causal constructions. Sergey Say bears primary responsibility for preparing the [questionnaire]({{ site_url_j }}/questionnaire.html) used for NoCaCoDa, which was discussed with other members of the grant project. NoCaCoDa’s team also includes Natalia Logvinova and Elizaveta Zabelina as core members, as well as language contributors, see [Team]({{ site_url_j }}/team.html) for further details. Despite the official completion of the RSF-funded project in 2022, NoCaCoDa is expected to further grow in its coverage and new results are to appear in print.

### References

* Dirven, R. 1995. The construal of cause: The case of cause prepositions. In: J. R. Taylor , R. MacLaury (eds.). Language and the cognitive construal of the world. Berlin, New York: Mouton de Gruyter. 95–118.
* Iordanskaia, L. N., I. A. Mel'chuk. 1996. Towards the semantics of Russian causal prepositions (IZ-ZA liubvi ~ OT liubvi ~ IZ liubvi ~ * S liubvi ~ PO liubvi). Moskovskii lingvisticheskii zhurnal, 2 (1), 162–211. (in Russian)
* Ivić, M. 1954. Causal constructions with prepositions zbog, od, iz in the modern literary language. Naš jezik, 5–6: 186–194. (in Serbo-Croatian)
* Klangová, L. 2017. Expression of causal relations in Russian and Czech. Ph.D. dissertation. Brno: Masarykova univerzita. (in Russian)
* Kovačević, M. 1988. Causal semantic field. Sarajevo: Svjetlost. (in Serbo-Croatian)
* Levontina, I. B. 2003. IZ-ZA 4, IZ 8.1, OT 6, colloquial PO I.7, colloquial S I.10, dated or bookish ZA II.8, BLAGODARIa, bookish PO PRIChINE, bookish VSLEDSTVIE, non-colloquial V REZUL''TATE, bureaucratic VVIDU, bookish V SILU ‘by the reason that’. In: Ju. D. Apresian et al. (eds.). Novyi ob"iasnitel'nyi slovar' russkogo iazyka. Moskva: Iazyki russkoj kul’tury. 430–437. (in Russian)
* Radden, G. 1985. Spatial metaphors underlying prepositions of causality. In: W. Paprotté, R. Dirven (eds.). The ubiquity of metaphor. Amsterdam, Philadelphia: John Benjamins. 177–207.
* Say, S. S. Nominal causal constructions: parameters of typological variability and a research questionnaire. To appear in N. M. Zaika (ed.). Typology of causal constructions. St. Petersburg: ILS RAS.
* Valiulytė, E. 1998. Syntactic synonyms in the modern Lithuanian language. Circumstances of place, time and reason. Vilnius: Mokslo ir enciklopedijų leidybos institutas. (in Lithuanian)
* Zaika, N.M. 2019. Polypredicative causal constructions in the languages of the world: the space of typological possibilities. Voprosy iazykoznaniia, 4: 7–32. (in Russian)
