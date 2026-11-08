# Étude de marché : Depth Theory (mesurée le 8 novembre 2026, 7 vidéos, toutes celles de la chaîne)

**Ce fichier n'est pas un modèle à suivre.** Il dit pourquoi la niche marche ; la forme d'Oxygen Odds est dans `identity.md`. Les titres, la miniature, les tournures et l'outro décrits ici sont **à eux** : `originality.py` les bloque.

| Principe qui marche ici (on le garde) | Notre version Oxygen Odds |
|---|---|
| Le spectateur est mis en danger (« you ») | il **joue** : choix A/B/C, jauge d'O2, score |
| Un animal connu + un record + une vraie rencontre | idem, mais chaque fait tranche un choix du jeu |
| Échelles concrètes (bus, éléphants, ta main) | silhouette humaine étalon et « head to toe » |
| Débit soutenu, presque sans pause, plans de 3,5 à 4 s | idem (norme de la niche, pas une signature) |
| Pas de musique, effets sonores denses | bips d'ordinateur de plongée, sonar, détendeur |
| Sources et crédits dans la description | idem + mention IA et « score de jeu » |

À **ne jamais reprendre** : les gabarits de titres §2, la miniature §6 (gravure noire, plongeur à lampe, flèche rouge, « IT … YOU.. »), l'ouverture « Picture this », « What would you actually do? », « The real danger », l'outro, la palette bleu nuit vectorielle et les cartes à grille de §5.

Source : @depththeoryofficial, 20,7 k abonnés, 7 vidéos du 26 oct. au 8 nov. 2026 (une tous les 2 à 3 jours). Données brutes dans `Desktop/Nouveau dossier (3)/depth-theory/` (`channel.json`, `analysis/`, `tx/` = transcriptions pour `originality.py --ref`, `rea/`). Ces données restent en local, jamais dans le dépôt (droits d'auteur).

| Date | Titre | Durée | Vues | Plan médian | Mots/min |
|---|---|---|---|---|---|
| 26/10 | Why You Never Want to Meet a Colossal Squid | 9:56 | 519 k | 6,5 s | 171 |
| 27/10 | **Why You'd Never Want To Meet A Sperm Whale** | 9:59 | **6,56 M** | 5,2 s | 168 |
| 29/10 | Would A Great White Survive Every Prehistoric Ocean? | 19:41 | 732 k | 5,2 s | 148 |
| 01/11 | Why You'd Never Want To Meet A Humpback Whale | 10:52 | 269 k | 3,9 s | 171 |
| 03/11 | Why You'd Never Want To Meet A Polar Bear | 15:33 | 264 k | 3,5 s | 170 |
| 05/11 | Why The Ocean's Deadliest Predator Never Hunts You | 11:52 | 51 k | 3,5 s | 172 |
| 08/11 | Why You'd Never Survive In Every Prehistoric Ocean | 16:56 | (2 jours) | 4,0 s | 160 |

## 1. Fourchettes chiffrées (contrôle de `script_metrics.py` et `analyze_video.py`)
- Durée 10 à 17 min ; défaut 12 min ≈ 2 000 mots.
- Voix : 160 à 172 mots/min ; voix masculine grave, f0 médian 103 à 111 Hz ; pauses quasi absentes (≤ 0,8 par min, aucune > 0,8 s). ElevenLabs « Brian » convient ; si trop aiguë, « Daniel ».
- Texte : 11,7 à 14,3 mots par phrase (cible 12) ; 6 à 13 % de phrases de ≤ 4 mots (« Not see it, feel it. ») ; « you » 0,5 à 3,3 pour 100 mots (cible 1,5 à 2) ; 2 à 6 nombres par minute (les plus récentes, 5 à 6) ; 4 à 7 questions par vidéo ; ouvertures « And / So / But » fréquentes.
- Montage : un plan toutes les 3,5 à 5 s (médiane), soit 12 à 18 coupes/min (rea-video) ; la chaîne accélère (6,5 s → 3,5 s en deux semaines) : viser 3,5 à 4 s. Caméra presque toujours en mouvement (85 %, rapprochement lent).
- Son (rea-video, 7/7) : voix de synthèse ; **pas de musique** sur 6 vidéos sur 7 (une seule a un lit discret à 140 BPM) ; **effets sonores denses** : 59 à 181 par vidéo, soit 6 à 11 par minute, en hausse sur les plus récentes. Cible : 8 par minute, un effet sur chaque apparition d'élément de carte (pop, tick, whoosh), chaque coupe vers une nouvelle scène, chaque révélation d'animal (grondement grave), jamais sous la voix au point de la couvrir.
- Pas de sous-titres incrustés.

## 2. Titres (gabarit)
Title Case, 40 à 55 caractères (mesuré : 43 à 52), « you » dans 6 titres sur 7, une promesse de danger pour le spectateur :
- **A** (4/7, dont le record 6,5 M) : `Why You'd Never Want To Meet A [Animal]`
- **B** (2/7) : `Would A [Predator] Survive Every Prehistoric Ocean?` / `Why You'd Never Survive In Every Prehistoric Ocean`
- **C** (1/7, le plus faible) : `Why The Ocean's Deadliest Predator Never Hunts You` (énigme sans nom d'animal : éviter, le nom de l'animal est le mot-clé recherché).
Animal choisi : grand, connu, avec une rencontre humaine réelle et un record (taille, son, force).

## 3. Description (gabarit observé sur 7/7)
1. Paragraphe d'accroche (2 à 4 phrases) : nom de l'animal en premier, 2 à 4 records chiffrés, une rencontre humaine, puis la question à « you » (« So what would you actually do if… ? »).
2. Optionnel : « In this video we… » + la liste des points traités, nommés avec leurs mots-clés (Essex, Moby-Dick, coda, Dunkleosteus…).
3. Chapitres `0:00 …` (6 à 13, aux temps réels).
4. Question aux commentaires : quelle créature ensuite.
5. `Sources:` études et articles avec URL ; `Footage and photos:` crédits (NOAA, USGS, NASA, Pexels avec noms, Wikimedia avec licence CC BY/BY-SA, « Animation and narration: original »).
La chaîne modèle n'a ni tags ni hashtags (0 sur 7) ni « subscribe » ; le seo-metadata-editor propose quand même des tags (≤ 500 caractères) en signalant l'écart, l'utilisateur décide.

## 4. Script (gabarit en temps)
1. **Scène d'ouverture « you »** (0:00–0:30) : « Picture this. You're floating… » (4/7) ou une scène réelle filmée/archivée (caméra d'un collier d'ours, photo de 1911). La sensation avant la vue, puis la révélation de l'animal.
2. **Démonter l'idée reçue + la promesse** (avant 1:30) : « When most people think of… But… So let's talk about why you'd never want to… »
3. **Taille** avec comparaisons concrètes (bus, éléphants, « as long as your hand »).
4. **3 à 5 paliers de danger**, un par chapitre : ce qu'il mange, son arme (son, morsure, odorat), son cerveau ou son comportement, l'histoire vraie (Essex 1820, plongeur avalé, kayakiste).
5. **« What would you actually do? »** : 3 ou 4 options éliminées une à une (carte « YOUR OPTIONS » barrée), puis la seule qui marche.
6. **Twist** : « The real danger » (c'est nous la menace : chasse, filets, chocs de navires) ou l'utilité de l'animal pour l'océan.
7. **Outro** (≤ 4 phrases) : merci, quelle créature ensuite en commentaires, lien vers une autre vidéo. Écrire sa propre formule, jamais celle de la chaîne mot pour mot.
Format B (« every prehistoric ocean ») : un chapitre par ère, titre `Ère (N million years ago): créature`, un verdict par ère (couronne / survit / crâne), score final.

## 5. Images (familles, pour 12 min ≈ 170 plans)
- **Scènes vectorielles plates** ~55 % : bleu nuit/sarcelle, rayons de lumière, animal anatomiquement juste en gris, plongeur minuscule (combinaison noire, bouteille blanche, palmes jaunes) ; la même scène du plongeur ouvre et ferme la vidéo.
- **Cartes infographiques** ~25 % (`html`, jamais Flow) : fond bleu nuit à grille fine ; titre en petites capitales blanches ou rouges soulignées (« WHAT DOES IT EAT? », « THE REAL DANGER ») ; barres d'échelle « ~16 M », jauge dB, compteur, sonar vert, carte avec chiffre encadré, liste d'options barrées, comparaison « YOU vs [animal] ».
- **Photos et vidéos réelles** ~12 % : fossiles et squelettes de musée, archives, NOAA/Pexels ; légende en petites capitales en haut (« A REAL DUNKLEOSTEUS · CLEVELAND MUSEUM ») et crédit minuscule en bas à gauche.
- **Accessoires d'humour** ~5 % : document papier (« OFFICIAL COMPLAINT », tampon « STOPPED »), vieille carte « Here be Monsters », petit bonhomme bâton « YOU » à tête ronde blanche.
- **Inserts science** ~3 % : coupe, microscope, onde sonore.
Palette : bleu nuit `#0b1d2e`, sarcelle `#1f5f6b`, gris animal `#8a8f94`, rouge danger `#e21e24`, vert sonar `#3ddc84`, sable pour les ères anciennes. Mouvement : zooms et panoramiques lents, aucune transition tape-à-l'œil.

## 5 bis. Décomposition rea-video (7/7, sans VLM, confiance ≈ 0,6)
Mélange stable : scènes animées 28 à 58 % (classées « rendu 3D » à cause des mouvements de caméra fluides ; à l'œil, du vecteur plat animé), cartes générées par code 22 à 67 %, images fixes en zoom/pan 8 à 28 %, plans douteux (« AI ») 3 à 15 % (surtout des vidéos d'archives NOAA/Pexels en 24 i/s), prise de vue réelle ≤ 2 %. Leçon technique (pas de style) : un rendu image + zoom/pan + cartes générées par code suffit dans cette niche ; notre pipeline HyperFrames le fait avec notre propre style (`identity.md` §5). Rapports : `depth-theory/rea/<id>/report.html`.

## 6. Miniature (7/7 identiques)
Fond noir pur ; animal en **gravure noir et blanc (scratchboard)**, énorme, à droite ; **plongeur minuscule avec lampe** dont le faisceau éclaire l'animal ; texte en haut à gauche, capitales blanches très grasses condensées, **le dernier mot en rouge**, terminé par « .. » : « IT SEES YOU.. », « IT HEARS YOU.. », « IT HUNTS YOU.. », « WON'T HUNT YOU... », « YOU'RE NEXT.. », « Still King? » ; **flèche rouge courbe** du texte vers le plongeur ; parfois des ondes sonores (cercles) autour de la tête de l'animal. Aucune couleur hors noir, blanc et rouge. **Leur signature : ne pas reprendre** (notre miniature : `identity.md` §5).
