---
name: depth-theory-video
description: Use when the user wants a YouTube video, script, title, description or thumbnail for their ocean-predator channel in the style of Depth Theory (@depththeoryofficial) — "Why You'd Never Want To Meet A [sperm whale / polar bear / colossal squid]", "Would A Great White Survive Every Prehistoric Ocean?", deep-sea monsters, whales, sharks, orcas, megalodon, prehistoric seas told to "you" the diver — or says "comme Depth Theory", "vidéo océan", "prédateur marin", "black engraving thumbnail with red arrow", even without naming a skill. Also use to re-measure that channel or break a reference video down with rea-video.
---

# Depth Theory Video

Explainer de 10 à 20 min en anglais (public US) : un animal marin (ou un océan préhistorique) raconté à « you », le plongeur minuscule face à l'animal géant. Normes mesurées le 8 novembre 2026 sur les 7 vidéos de la chaîne : `references/norms.md`. Réponses à l'utilisateur en français, livrables en anglais.

## Héritage : tout le pipeline vient de ancient-humans-video
`AH=~/.claude/skills/ancient-humans-video`, `DT=~/.claude/skills/depth-theory-video` (toujours ces chemins absolus, le dossier de travail est ailleurs). Scripts, agents, voix ElevenLabs, Flow, HyperFrames, son, publication : **ceux de `$AH`, appelés par leur chemin, jamais copiés**. Ce skill ne contient que ce qui change (normes, style, miniature, agents) :
- `references/norms.md` — chiffres de la chaîne, titres, description, chapitres, miniature, style visuel. Prime sur `$AH`.
- `references/agents.md` — ce qui change dans chaque brief d'agent de `$AH/references/agents.md`.
- `scripts/thumb_depth.py` — gabarit miniature (gravure noire, dernier mot rouge, flèche rouge).
- `scripts/meta_digest.py` — résumé compact des métadonnées de la chaîne.
- Style d'image `depth-flat` dans `$AH/scripts/styles.json` (`prompts.py --style depth-flat`).

## Économie de tokens (règles de lecture)
1. Lire un fichier de `$AH` **par section** : `grep -n '^##' $AH/<fichier>` puis `sed -n '<a>,<b>p'`. Jamais `$AH/SKILL.md` en entier (5 500 mots) : les étapes ci-dessous le remplacent ; n'en lire que la section citée.
2. Sorties d'outils = résumés : `rea-video summary`, `analyze_video.py` (1 ligne), `script_metrics.py`, `meta_digest.py`. Jamais `breakdown.json`, `*.json3`, `*.info.json`, `timing.json` en entier dans le contexte.
3. Images : une planche contact par lot (`$AH/scripts/sheets.py`, `analysis/*_sheet.jpg`), jamais image par image.
4. Agents : chaque agent écrit son livrable dans un fichier et ne rend que ≤ 10 lignes (verdict + chemin). Modèle `haiku` pour lint, QC et vérifications ; `sonnet` pour l'écriture ; l'orchestrateur ne réécrit pas ce qu'un agent a produit.
5. Mesures de la chaîne en cache dans `references/norms.md` : ne re-mesurer que les vidéos publiées depuis la date de mesure (`yt-dlp --dateafter`).
6. Long calcul (rendu, décomposition, TTS) en arrière-plan, attendre la notification, ne pas sonder.

## Workflow
1. **Brief** (`$AH/references/brief.md`, 2 tours max) : animal ou concept, angle, durée (défaut 12 min), voix ElevenLabs (clé `ELEVENLABS_API_KEY` du `.env` du dossier de travail ; lancer `tts.py` avec la variable d'environnement vidée pour que le `.env` gagne). **Story architect** : 3 angles au gabarit de titre de `norms.md` §2 → `brief.json` `validated_by_user: true`.
2. **Faits** : **Fact-checker**, 5 à 10 sources nommées (études, NOAA, musées, presse sur les rencontres réelles), 20 à 50 chiffres. Chaque rencontre humaine racontée est datée et sourcée.
3. **Script** : **Script writer** au gabarit de `norms.md` §4 ; puis **Fact-checker** + **Script critic** en parallèle ; `python $AH/scripts/yt/script_metrics.py script.md --minutes 12` dans les fourchettes de `norms.md` §1.
4. **Shot list** : **Image director** copie `$AH/scripts/make_shots.py`, familles et rythme de `norms.md` §5 ; `python $AH/scripts/prompts.py shots.json --style depth-flat --flow-per-min 6` ; **Visual director**.
5. **Voix** : `python $AH/scripts/tts.py shots.json --engine eleven --voice Brian --gap 0.3`, test `--only 1,2,3` ; **Audio director** vérifie débit, pauses et f0 contre `norms.md` §1.
6. **Images** : Flow par Playwright (`$AH/references/flow-automation.md`, section par section) ; cartes infographiques et chiffres en `html` (jamais Flow) ; photos réelles (fossiles, musées, NOAA/USGS domaine public, CC0/CC BY) par `$AH/scripts/openverse.py`, crédit en bas à gauche et dans la description ; **Image QC** par planche.
7. **Montage** : HyperFrames par défaut (`$AH/scripts/hf_build.py`, `--accent "#e21e24"`), commandes de rendu dans `$AH/SKILL.md` étape 7 du Workflow.
8. **Son** : commandes de `$AH/SKILL.md` §5, **avec les cibles de `norms.md` §1 qui priment** : pas de lit musical (ou un drone très bas si l'utilisateur le veut), effets Real SFX denses (~8/min : `sfx_cues.py` puis ajouter un pop/whoosh par élément de carte et par coupe de scène), −14 LUFS.
9. **Miniature** : image Flow au gabarit `thumbnail` du style `depth-flat`, puis `python $DT/scripts/thumb_depth.py scene.png thumbnail.jpg "IT HEARS YOU.." --arrow=0.33,0.22,0.16,0.75` (flèche du texte vers le plongeur).
10. **Publication** : **packaging-strategist** (titre) et **seo-metadata-editor** (description, chapitres, sources) au gabarit de `norms.md` §3 ; **Publication checker**.
11. **Short et posts** : `$AH/SKILL.md` étapes 10 et 11 du Workflow, inchangées.

## Analyser une vidéo de référence (rea-video)
CLI installée en mode éditable depuis `~/.local/src/rea-video` ; préférences `stems off` et `lang en` déjà posées (le modèle de séparation voix/musique, 67 Mo sur GitHub, se bloque au téléchargement sur ce réseau ; la voix se mesure par `analyze_video.py`). Toujours préfixer `PYTHONUTF8=1` (sinon plantage cp1252). Télécharger en 480p (`$AH/SKILL.md` §8), puis :
```
PYTHONUTF8=1 rea-video decompose vids/<id>.mp4 -o rea/<id>    # en arrière-plan ; --no-packaging gagne ~40 s par minute
PYTHONUTF8=1 rea-video summary rea/<id>/breakdown.json        # seule sortie à lire
```
Au besoin ensuite : `storyboard.jpg`, et la section voulue de `report.md` (`grep -n '^##'`). Rythme et voix : `python $AH/scripts/yt/analyze_video.py vids/<id>.mp4 analysis --subs vids/<id>.en-orig.json3`. Métadonnées : `yt-dlp --js-runtimes node --skip-download --write-info-json -o "meta/%(upload_date)s_%(id)s" <url chaîne>/videos` puis `python $DT/scripts/meta_digest.py meta`.

## Contrôle avant livraison
- [ ] Titre au gabarit `norms.md` §2 ; miniature par `thumb_depth.py` sans `--force`
- [ ] `script_metrics.py` et `analyze_video.py out.mp4` dans les fourchettes de `norms.md` §1
- [ ] Toute rencontre, chiffre ou record `[vérifié]` par le Fact-checker ; aucune mise en scène présentée comme un fait
- [ ] Description : accroche chiffrée, chapitres aux temps réels de la voix, question aux commentaires, sources et crédits d'images complets
- [ ] Planche contact passée par Image QC ; chaque photo réelle créditée
