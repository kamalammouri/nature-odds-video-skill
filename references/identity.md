# Nature Odds — bible de la chaîne (@NatureOdds)

Promesse : **chaque vidéo est une partie**. Tu entres dans le monde d'un animal (mer, terre ou ciel) avec une jauge pleine, la nature fixe tes chances. Le spectateur joue : il choisit à chaque niveau, il voit sa jauge baisser, il apprend la vraie biologie parce que chaque choix est tranché par un fait sourcé. Tout ce qui suit est propre à la chaîne ; la chaîne étudiée (`reference-depth-theory.md`) n'apporte que des principes, jamais une forme.

## 1. Le joueur et le narrateur
- **Le joueur = « you »**, au présent, deuxième personne : petit explorateur en tenue **orange** (combinaison étanche sous l'eau, veste sur terre, combinaison de vol en altitude), lampe frontale cyan, ordinateur de survie au poignet.
- **Le narrateur = ton ordinateur de survie (au poignet)** : calme, sec, précis, un brin pince-sans-rire. Il annonce les valeurs (« Stamina: eighty-two percent. Something large just changed direction. »), puis raconte. Pas de cri, pas d'emphase de bande-annonce.
- **Jauge selon le milieu** (`hud.json` `gauge`, `thumb_odds.py --gauge`) : sous l'eau **O2** ; sur terre **STAMINA** ; froid et banquise **WARMTH** ; nuit et grottes **BATTERY** (lampe) ; en altitude **AIR** ; en Body Swap, ce que l'animal risque de perdre (**ENERGY**).
- Phrase signature de la chaîne : **« Check your odds. »** (ouverture de chaque partie) et **« Drop your odds in the comments. »** (fin).

## 2. Quatre formats en rotation (jamais deux fois de suite le même)
| Format | Titre (gabarit à nous) | Niveaux | Mécanique |
|---|---|---|---|
| **A. 60 Seconds** | `Can You Survive 60 Seconds Next To A [Animal]?` | 5 niveaux de proximité (100 m → contact) | compte à rebours à l'écran |
| **B. Expedition** | `Can You Cross [Lieu] Alive?` / `Could You Survive A Dive To [N] Meters?` | 5 zones du lieu (savane, jungle, banquise, profondeurs…), une créature par zone | jauge de distance ou de profondeur |
| **C. Body Swap** | `You Wake Up As A [Animal]. Can You Survive?` | 5 épreuves de la vie de l'animal | tu joues l'animal : ses sens deviennent ton HUD |
| **D. Real Run** | `Could You Have Survived [Rencontre réelle]?` | la chronologie d'un incident documenté | rejouer les décisions, puis ce qui s'est vraiment passé |

**Chaque épisode a une mécanique neuve** ajoutée au HUD : jauge de bruit (sonar du cachalot), champ électrique (requin), température (ours polaire), courant, deuxième prédateur… Elle est notée dans `brief.json` (`new_mechanic`) et l'Originality checker refuse un épisode sans elle.

## 3. Structure d'une partie (≈ 12 min, 1 900 à 2 100 mots)
1. **GAME START** (0:00–0:25) : le HUD s'allume, « Check your odds. », le lieu, le but (« survive sixty seconds »), la première menace devinée avant d'être vue.
2. **Niveaux 1 à 5** (1,5 à 2,5 min chacun) : le décor → une capacité de l'animal (un record sourcé, converti en échelle humaine) → **CHOIX A / B / C** (carte à l'écran, 2 s de silence voulu pour que le spectateur choisisse) → la conséquence, tranchée par un fait → mise à jour du HUD (O2, SURVIVAL %).
3. **Retournement** vers 55 % : la règle change (fuite d'air, courant, second prédateur, nuit).
4. **Fin** : GAME OVER ou YOU SURVIVED, décidé par les faits, puis le score.
5. **Debrief** (≤ 60 s) : *what actually keeps people alive* — un vrai conseil de sécurité (source officielle : NOAA, gardes-côtes, Croix-Rouge) + un fait de conservation.
6. **Outro** (≤ 3 phrases) : « Drop your odds in the comments. » + la prochaine partie annoncée.
Les pourcentages de survie sont un **score de jeu** expliqué par les faits cités, jamais présentés comme une probabilité scientifique (dit une fois dans la vidéo et dans la description).

## 3 bis. Fichiers d'un épisode
- `brief.json` : `{"format": "A|B|C|D", "subject": "...", "title": "...", "thumb_text": "...", "goal": "...", "new_mechanic": "...", "gauge": "O2|ENERGY|AIR", "levels": [{"name": "...", "fact": "... [source]", "choice": {"A": "...", "B": "...", "C": "...", "correct": "B", "source": "..."}}], "twist": "...", "ending": "GAME OVER|YOU SURVIVED|WHAT REALLY HAPPENED", "validated_by_user": false}` ; `true` seulement après le choix de l'utilisateur.
- `script.md` : une phrase par ligne = un plan dit à voix haute ; en-têtes `## Chapter N — Level N: titre` (`make_shots.py` exige « Chapter »). Le choix est une phrase dite (« Choose. A, hold still. B, swim for the boat. C, face it. ») dont le plan est une carte `H({"type": "choice", ...})` ; la réponse vient à la ligne suivante, jamais dans la même phrase. Cartes néon par `$DT/scripts/neon_cards.py`.
- `hud.json` : schéma en tête de `$DT/scripts/hud.py`. **Body Swap** : `"gauge": "ENERGY"` (ou ce que l'animal risque de perdre), l'O2 n'a pas de sens quand tu es l'animal.
- **Scripts publiés** : chaque script final est copié en `published/<AAAA-MM-JJ>_<sujet>.txt` dans le dossier de la chaîne ; `originality.py script.md --ref published` vérifie qu'on ne se recopie pas.
- Texte de miniature par format : A « 0:12 LEFT », B « 1 IN 40 », C « STILL ALIVE? », D « GAME OVER? » ou le score réel.

## 4. Écriture
- 10 à 14 mots par phrase, 10 % de phrases très courtes ; « you » 3 à 5 pour 100 mots (plus que la chaîne étudiée : c'est un jeu) ; 4 à 6 nombres par minute, chacun ramené au corps (« longer than three of you lying head to toe »).
- Chaque choix a une bonne réponse défendable par une source ; pas de piège arbitraire.
- Humour sec du narrateur, une réplique par niveau au plus. Aucun gore : la mort est un écran GAME OVER, pas une description.
- Interdits (contrôlés par `$DT/scripts/originality.py`) : les tournures de la chaîne étudiée et toute phrase reprise de nos propres scripts précédents (> 10 mots d'affilée).

## 5. Identité visuelle
- Images Flow au style **`nature-neon`** (`$AH/scripts/styles.json`) : noir absolu, créatures en contours lumineux cyan / bleu électrique / magenta sur fond de nuit (eau, savane, jungle, glace selon l'épisode), particules, l'explorateur orange minuscule.
- **HUD permanent** en haut à gauche (`$DT/scripts/hud.py`) : niveau, barre d'O2 (rouge sous 30 %), SURVIVAL %, profondeur ; bandeaux GAME OVER / YOU SURVIVED / CHOICE LOCKED.
- **Cartes `html`** : carte-choix A/B/C dans des cadres néon ; carte-niveau « LEVEL 3 · TWILIGHT ZONE · 600 M » ; chiffre-record avec silhouette humaine à l'échelle.
- Couleurs : noir `#000000`, cyan `#00e5ff`, magenta `#ff2fd6`, rouge alerte `#ff2e4d`, orange explorateur `#ff8a1f`. Polices : JetBrains Mono (HUD), League Gothic (titres).
- Mouvement : lents zooms dans le noir, flashs de lumière sur les révélations, léger tremblement d'écran à chaque alerte.
- **Miniature** (`$DT/scripts/thumb_odds.py`) : la créature néon énorme à droite, l'explorateur orange en bas à gauche, en haut à gauche le score (« 3% SURVIVAL », « 0:12 LEFT », « 1 IN 40 », « GAME OVER? ») et la barre d'O2 presque vide.

## 6. Son
- Pas de musique dramatique : un **lit de détendeur** (respiration lente, bulles) très bas, et une pulsation synthé grave seulement dans le niveau 5.
- Signature sonore : bip de l'ordinateur à chaque mise à jour du HUD, ping de sonar à chaque révélation de créature, alarme douce sous 30 % d'O2, « lock » sur chaque choix. Cible ≈ 8 effets par minute, jamais par-dessus une phrase.

## 7. Description YouTube (gabarit à nous)
1. La partie en une phrase (« You have 60 seconds and full stamina next to a grizzly. Choose well. »), puis 2 records sourcés.
2. « Survival odds are a game score built from the facts cited in the video, not a scientific probability. »
3. Chapitres `0:00 Game start` / `1:40 Level 1 — …` / … / `11:10 Debrief: what actually keeps you alive`.
4. « Drop your odds in the comments: did you survive? »
5. `Sources:` (URL) ; `Visuals:` illustrations générées avec assistance IA (Google Flow) + photos/archives créditées avec licence ; `Voice:` voix de synthèse (ElevenLabs).
6. 3 hashtags (#NatureOdds #animals #survival) ; tags ≤ 500 caractères proposés par le seo-metadata-editor.

## 8. Shorts
« One Choice » : 30 à 45 s verticales, un seul niveau, la carte A/B/C, coupure avant la réponse (« answer in the comments, the full run is on the channel »).
