# Voie B : animation par code avec Maven Animate

Maven Animate (par Maven : Instagram @maven.iqq, YouTube maveniqq) dessine tout le film par code, à partir d'un fichier de scène JSON : animaux animés, jauges, sonar, compteurs, sous-titres mot à mot, MP4 de 720p à 4K en quelques secondes, sans Flow ni crédits. **Il n'est pas inclus dans ce skill** : sa licence interdit de le republier. Chacun le récupère par le lien de Maven et l'installe en skill séparé : `MV=~/.claude/skills/maven-animate`, avec son dossier `rights/` intact.

## Quand prendre cette voie plutôt que Flow
- Flow est bloqué (« activité inhabituelle ») ou les crédits sont épuisés.
- L'épisode est marin, ou la scène montre un humain : le casting de Maven couvre surtout la mer (cachalot, requin, orque, poisson, anguille, calmar, pieuvre, méduse, plongeur, humain). Un animal terrestre doit être construit comme gréement (`swimmer`) ou en tracés SVG (`shape`) : c'est faisable pour une silhouette simple, mais pour un lion ou un grizzli détaillé, garder Flow.
- Shorts, brouillons, plans de démonstration (un sonar, une plongée, une jauge) : on peut mélanger les deux voies, avec des plans Maven exportés en MP4 entre des images Flow.

## Règles Nature Odds (elles priment sur le style par défaut de Maven)
Le style par défaut de Maven (vecteur plat bleu nuit, plongeur en combinaison noire avec palmes jaunes) ressemble à Depth Theory : **ne jamais l'utiliser tel quel, ne jamais partir de `$MV/examples/`** (l'exemple anglais reprend la vidéo cachalot de Depth Theory).
- En tête du fichier de scène : `"theme": "night"`, et dans `colors` : `sonar` et `cool` à `#00e5ff`, `hot` à `#ff2e4d`, `mark` à `#ff2fd6`, `ink` à `#f0f8ff`.
- Monde : `"mode": "dark"`, `depth` entre 0,85 et 0,95, des particules (`motes`).
- Animaux : `"look": "neon"` (contour lumineux avec halo, ajout local décrit plus bas).
- Le joueur : `diver` sous l'eau, `person` sur terre, avec `"colors": {"suit": "#ff8a1f", "tank": "#3a2a1a", "flip": "#ff8a1f"}`.
- HUD de la chaîne (`identity.md` §5), traduit en éléments Maven : niveau = `tag` en haut à gauche ; jauge du milieu (O2, STAMINA…) = `bar` avec `"color": "cool"` ; SURVIVAL % = `count` avec `post`, centré sur `x` ; choix A/B/C = `facts` ; GAME OVER ou YOU SURVIVED = `seal` ; profondeur = `depth`.
- Format de scène complet : lire `$MV/references/scene-format.md` ; mouvement et rythme : `$MV/references/look.md`.

## Procédure
1. Voix d'abord (étape 5 du SKILL), puis les temps des mots : `timing.json` d'ElevenLabs, ou `python $MV/scripts/timestamps.py voice.wav words.json --lang en`.
2. Le **Motion designer** écrit `film.json` : un événement par temps fort de 1,5 à 3 s, aux règles ci-dessus, chiffres à l'écran identiques à ceux de la voix.
3. Planche de contrôle : `NODE_PATH=C:/Users/kamalAmmouri/Desktop/nastro/node_modules node $MV/scripts/render.mjs film.json sheet.png --sheet --res 720`, lue par l'**Image QC** (anatomie, rien sous les sous-titres, plongeur orange).
4. Rendu sans mastering : `node $MV/scripts/render.mjs film.json render.mp4 --res 1080 --voice voice.wav --raw`, puis le son de la chaîne : `python $DT/scripts/mix_odds.py render.mp4 hud.json <fond>.mp3 out.mp4 --sonar <temps>`.
5. `originality.py` sur le script, comme pour la voie Flow : l'outil ne change rien aux règles anti-clone ni à `youtube-compliance.md` (images non réalistes : pas de case « contenu synthétique » pour elles, mais la voix reste déclarée).

## Modifications locales de la copie de Maven (autorisées pour usage personnel)
Trois ajouts, marqués `local change (Nature Odds)` dans `$MV/engine/cast.js` et `$MV/engine/kit.js` (originaux gardés en `*.orig`) : le look `neon`, la couleur pleine `color` de `bar`, et les couleurs `colors` du `diver`. Si Maven publie une nouvelle version, les réappliquer, et ne jamais les publier.
Playwright et Chromium sont déjà installés sur cette machine : ne pas lancer `setup.ps1`, passer `NODE_PATH=C:/Users/kamalAmmouri/Desktop/nastro/node_modules`.
