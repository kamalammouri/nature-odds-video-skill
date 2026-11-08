---
name: oxygen-odds-video
description: Use when the user wants a YouTube video, script, title, description, thumbnail or Short for their ocean channel Oxygen Odds (@OxygenOdds) — survival-game explainers where "you" dive with an oxygen gauge and survival odds, choose A/B/C at each level, and meet sperm whales, sharks, orcas, giant squid, polar bears, deep-sea monsters or prehistoric seas — or says "Oxygen Odds", "vidéo océan", "prédateur marin", "can you survive…", "survival simulator", "HUD néon", "comme Depth Theory", even without naming a skill. Also use to check a draft for cloning or YouTube policy risks, or to break a reference ocean video down with rea-video.
---

# Oxygen Odds Video

Chaque vidéo est **une partie** de 10 à 15 min en anglais (public US) : tu plonges avec 100 % d'oxygène, un HUD néon affiche ta jauge et tes chances, tu choisis A/B/C à chaque niveau et chaque choix est tranché par un fait sourcé. Identité complète : `references/identity.md`. Réponses à l'utilisateur en français, livrables en anglais.

## Trois règles qui priment sur tout
1. **Original, jamais un clone.** La chaîne étudiée (Depth Theory, `references/reference-depth-theory.md`) n'apporte que des principes. Ses titres, sa miniature, ses tournures, son outro et sa palette sont interdits ; `$DT/scripts/originality.py` le vérifie, et l'agent Originality checker bloque un épisode qui échoue.
2. **Jamais deux épisodes pareils.** Rotation des 4 formats (`identity.md` §2) et une mécanique de HUD neuve par épisode : c'est la défense contre la règle YouTube « inauthentic content ».
3. **Conforme à YouTube.** `references/youtube-compliance.md` est passé case par case avant la publication.

## Héritage : tout le pipeline vient de ancient-humans-video
`AH=~/.claude/skills/ancient-humans-video`, `DT=~/.claude/skills/oxygen-odds-video` (toujours ces chemins absolus, le dossier de travail est ailleurs). Scripts, briefs d'agents, voix ElevenLabs, Flow, HyperFrames, son : **ceux de `$AH`, appelés par leur chemin, jamais copiés**. Ce skill ne contient que ce qui est propre à la chaîne :
- `references/identity.md` — la bible : joueur et narrateur, formats, structure d'une partie, écriture, visuels, son, description, Shorts.
- `references/agents.md` — ce qui change dans chaque brief d'agent, et le modèle de chaque agent.
- `references/youtube-compliance.md` — la liste de contrôle des règles YouTube, avec ses sources.
- `references/reference-depth-theory.md` — l'étude de marché (principes à garder, formes à ne jamais reprendre).
- `scripts/hud.py` (le HUD de jeu dans HyperFrames), `scripts/neon_cards.py` (cartes néon), `scripts/mix_oxygen.py` (le son de la chaîne), `scripts/thumb_oxygen.py` (la miniature), `scripts/originality.py` (le contrôle anti-clone), `scripts/meta_digest.py` (le résumé des métadonnées d'une chaîne). Chaque script a un `--selftest`.
- Démo complète de référence (8 novembre 2026, 64 s, tous les fichiers de travail) : `Desktop/Nouveau dossier (3)/oxygen-odds/demo-tiger/`.
- Style d'image `oxygen-neon` dans `$AH/scripts/styles.json`.

## Économie de tokens (règles de lecture)
1. Lire un fichier de `$AH` **par section** : `grep -n '^##' $AH/<fichier>` puis `sed -n '<a>,<b>p'`. Jamais `$AH/SKILL.md` en entier (5 500 mots) : les étapes ci-dessous le remplacent ; n'en lire que la section citée.
2. Sorties d'outils = résumés : `rea-video summary`, `analyze_video.py` (1 ligne), `script_metrics.py`, `meta_digest.py`, `originality.py`. Jamais `breakdown.json`, `*.json3`, `*.info.json`, `timing.json` en entier dans le contexte.
3. Images : une planche contact par lot (`$AH/scripts/sheets.py`), jamais image par image.
4. Agents : chacun écrit son livrable dans un fichier et ne rend que ≤ 10 lignes. `haiku` pour les contrôles et vérifications, `sonnet` pour l'écriture ; l'orchestrateur ne réécrit pas ce qu'un agent a produit.
5. Long calcul (rendu, décomposition, voix) en arrière-plan : attendre la notification, ne pas sonder.

## Workflow
1. **Brief** (`$AH/references/brief.md`, 2 tours max) : animal ou lieu, **format différent du précédent**, durée (défaut 12 min), voix ElevenLabs (clé `ELEVENLABS_API_KEY` du `.env` du dossier de travail ; lancer `tts.py` avec la variable d'environnement vidée pour que le `.env` gagne). **Story architect** : 3 parties possibles → `brief.json` avec `format`, `new_mechanic`, `validated_by_user: true`.
2. **Faits** : **Fact-checker**, 5 à 10 sources nommées, 20 à 50 chiffres, une source par bonne réponse de choix, debrief de sécurité de source officielle.
3. **Script et HUD** : **Script writer** → `script.md` + `hud.json` ; puis en parallèle **Fact-checker**, **Script critic** et **Originality checker** ; `python $AH/scripts/yt/script_metrics.py script.md --minutes 12` dans les fourchettes de `identity.md` §4.
4. **Shot list** : **Image director** copie `$AH/scripts/make_shots.py`, familles de `agents.md` (Visual director) ; `python $AH/scripts/prompts.py shots.json --style oxygen-neon --flow-per-min 6` ; **Visual director**.
5. **Voix** : `python $AH/scripts/tts.py shots.json --engine eleven --voice Brian --gap 0.3 --speed 0.9` (sans `--speed`, Brian sort à 190 mots/min, mesuré sur la démo du 8 novembre 2026 ; cible 160 à 172), test `--only 1,2,3` ; **Audio director** ; recaler les `t` de `hud.json` sur `timing.json` (`starts`).
6. **Images** :
   - **Flow (interface refaite en novembre 2026)** : chaque projet passe par un agent ; `qbatch.mjs` ne trouve plus ses boutons, et l'envoi automatisé déclenche « activité inhabituelle » (anti-robot : ne jamais le contourner). Procédure qui marche : écrire tous les prompts dans `flow_prompts_a_coller.txt` ; **l'utilisateur** les colle dans Flow (projet réglé en 16:9, x1) ; puis `FLOW_TAB=last node $AH/scripts/flow/harvest.mjs flow/raw` télécharge ses images, `python $AH/scripts/flow/harvest_sheet.py flow/raw` fait la planche, on associe chaque H### à son plan par l'image, et on copie en `flow/<video>/F###.png`.
   - Cartes-choix, cartes-niveaux, records et écran de fin : `python $DT/scripts/neon_cards.py shots.json flow/<video>` (jamais Flow).
   - Archives réelles par `$AH/scripts/openverse.py`, légendées et créditées.
   - **Image QC** par planche (sur la démo, l'image des pores montrait un poisson tacheté et non un requin-tigre : c'est le défaut type à attraper).
7. **Montage** : `python $AH/scripts/hf_build.py shots.json voice.wav timing.json hf --flow flow/<video> --no-captions --accent "#00e5ff"`, puis `python $DT/scripts/hud.py hf hud.json`, puis `npx hyperframes check hf --json` (ok) et le rendu de `$AH/SKILL.md` étape 7 du Workflow.
8. **Son** : `python $AH/scripts/openverse.py "scuba bubbles" --out audio/sfx --n 2` (fond CC0), puis `python $DT/scripts/mix_oxygen.py hf/renders/<rendu>.mp4 hud.json audio/sfx/<bulles>.mp3 out.mp4 --sonar <temps des révélations>` : voix compressée, fond baissé sous la voix, bips du HUD, sonar, « lock » des choix et alarme synthétisés, −14 LUFS (mesuré −14,1 LUFS, −1,4 dBTP sur la démo). Real SFX (`$AH/SKILL.md` §5) seulement pour des bruitages de bibliothèque en plus.
9. **Miniature** : image Flow au gabarit `thumbnail` du style `oxygen-neon`, puis `python $DT/scripts/thumb_oxygen.py scene.png thumbnail.jpg "3% SURVIVAL" --o2=0.07 --level="LEVEL 5 · ABYSS"`.
10. **Publication** : **packaging-strategist** (titre, texte de miniature), **seo-metadata-editor** (description `identity.md` §7), **Originality checker** sur le titre et la description, puis **Publication checker** avec `youtube-compliance.md`.
11. **Short et posts** : Short « One Choice » (`identity.md` §8) avec la commande de recadrage de `$AH/SKILL.md` étape 10 ; posts par le Community manager.

## Analyser une vidéo de référence (rea-video)
CLI installée en mode éditable depuis `~/.local/src/rea-video` ; préférences `stems off` et `lang en` déjà posées (le modèle de séparation voix/musique, 67 Mo sur GitHub, se bloque au téléchargement sur ce réseau ; la voix se mesure par `analyze_video.py`). Toujours préfixer `PYTHONUTF8=1` (sinon plantage cp1252). Télécharger en 480p (`$AH/SKILL.md` §8), puis :
```
PYTHONUTF8=1 rea-video decompose vids/<id>.mp4 -o rea/<id>    # en arrière-plan ; --no-packaging gagne ~40 s par minute
PYTHONUTF8=1 rea-video summary rea/<id>/breakdown.json        # seule sortie à lire
```
Rythme et voix : `python $AH/scripts/yt/analyze_video.py vids/<id>.mp4 analysis --subs vids/<id>.en-orig.json3`. Métadonnées : `yt-dlp --js-runtimes node --skip-download --write-info-json -o "meta/%(upload_date)s_%(id)s" <url chaîne>/videos` puis `python $DT/scripts/meta_digest.py meta`. Une analyse sert à trouver des **principes**, jamais une forme à reproduire.

## Contrôle avant livraison
- [ ] Format différent de l'épisode précédent, mécanique neuve, `originality.py` à 0 hit (contre la chaîne étudiée et contre nos scripts)
- [ ] `script_metrics.py` et `analyze_video.py out.mp4` dans les fourchettes de `identity.md` §4 ; chaque choix tranché par un fait `[vérifié]`
- [ ] HUD : `hyperframes check` ok, valeurs cohérentes avec le script, GAME OVER / YOU SURVIVED au bon moment
- [ ] Miniature `thumb_oxygen.py` sans `--force`, le score affiché correspond à la vidéo
- [ ] `youtube-compliance.md` : toutes les cases cochées (voix de synthèse déclarée, crédits, score de jeu annoncé)
