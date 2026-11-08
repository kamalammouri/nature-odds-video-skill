# Agents du format Depth Theory (delta sur `$AH/references/agents.md`)

Le brief générique de chaque rôle est dans `$AH/references/agents.md` (lire la seule section du rôle : `grep -n '^###' $AH/references/agents.md`). Ce fichier dit **ce qui change** ; il prime. Chaque agent écrit son livrable dans un fichier du dossier de travail et ne rend que ≤ 10 lignes : verdict, chemin, points bloquants.

| Rôle | Agent (`subagent_type`, modèle) | Ce qui change pour Depth Theory |
|---|---|---|
| Story architect | `story-architect`, sonnet | 3 angles, chacun = un titre au gabarit `norms.md` §2 + la scène d'ouverture « you » (où, quelle profondeur, ce que tu sens) + 3 paliers de danger + la rencontre humaine réelle + le twist (« the real danger » : c'est nous la menace, ou le renversement d'idée reçue). Écarter tout animal déjà publié sur la chaîne de l'utilisateur. |
| Fact-checker | `fact-checker`, sonnet | Chaque record (taille, décibels, profondeur, force de morsure) avec la fourchette de l'étude, jamais le chiffre viral ; chaque rencontre humaine : date, lieu, média source. Les reconstitutions d'espèces fossiles marquées « estimation (auteur, année) ». |
| Script writer | `general-purpose`, sonnet | Gabarit `norms.md` §4. Voix : un ami qui sait, phrases courtes, « you » dans la scène d'ouverture et dans « What would you actually do? », narration factuelle ailleurs ; humour sec, jamais de cri. Aucun CTA avant l'outro. |
| Script critic | `general-purpose`, haiku | Vérifie : scène « you » avant 0:20, promesse dite avant 1:30, un palier de danger par chapitre, au moins une comparaison d'échelle concrète par chapitre (bus, éléphants, ta main), twist présent, outro ≤ 4 phrases. |
| Render router / Visual director | `visual-director`, haiku | Familles et proportions de `norms.md` §5 (au lieu de 50/30/15/5) ; tout chiffre, échelle, comparaison ou liste = carte `html` bleu nuit ; aucune image Flow avec du texte. |
| Image director | `general-purpose`, sonnet | Style `depth-flat` ; le plongeur « you » toujours minuscule face à l'animal ; anatomie juste (dents sur la seule mâchoire inférieure du cachalot, etc.) ; photos réelles par `openverse.py` pour fossiles, musées, archives. |
| Image QC | `image-qc`, haiku | Phrase de contrôle = champ `qc` du style `depth-flat` + « anatomie conforme à l'espèce nommée ». |
| Audio director | `general-purpose`, haiku | Cibles `norms.md` §1 (débit, f0, pauses, pas de musique, ~8 effets/min) au lieu de celles de Mahoos. |
| Motion designer | `general-purpose`, sonnet | Cartes `norms.md` §5 : fond bleu nuit à grille fine, petites capitales espacées, rouge `#e21e24` pour le danger, cyan pour les mesures ; crédit photo en bas à gauche, petit, gris. Pas de sous-titres permanents (la chaîne n'en a pas) sauf demande. |
| Packaging strategist | `packaging-strategist`, sonnet | Titres au gabarit `norms.md` §2 ; texte miniature 2 à 4 mots en « IT [VERBE] YOU.. » ou une question courte (« Still King? ») ; lint par `$DT/scripts/thumb_depth.py`. |
| SEO / description | `seo-metadata-editor`, sonnet | Gabarit `norms.md` §3. Voir `norms.md` §3 (tags proposés, écart au modèle signalé). |
| English copy editor / Publication checker | `general-purpose`, haiku | Remplacer dans le brief générique : « titre en deux questions » → `norms.md` §2 ; « miniature troll-caveman + !! » → §6 ; « 8 à 10 chapitres » → 6 à 13 chapitres, le premier = la scène d'ouverture, le dernier = « What would you actually do? » ou le twist. |
| Sensitivity checker | non lancé par défaut | Seulement si le script raconte une mort humaine réelle : aucun détail gore, nom de la victime seulement s'il est public. |
| Community manager | `general-purpose`, haiku | Inchangé (`$AH/references/publication-seo.md` §8) ; images carrées par `$DT/scripts/thumb_depth.py --force` sur une image Flow. |
