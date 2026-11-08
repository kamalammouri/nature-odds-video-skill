# Conformité YouTube (vérifiée le 8 novembre 2026)

Le **Publication checker** passe cette liste avant chaque mise en ligne ; une seule case non cochée bloque la publication. Sources en bas : les règles officielles priment sur ce résumé ; les relire si une règle a changé.

## 1. Contenu inauthentique (ex-« repetitious content », renommé le 15 juillet 2025)
YouTube démonétise le contenu produit en masse ou répétitif, **quelle que soit la façon dont il est fait (IA comprise)** ; ses exemples : récits narrés et diaporamas qui ne diffèrent que superficiellement. L'IA reste permise si elle sert un contenu original. Les sources secondaires indiquent un examen au niveau de la chaîne entière.
- [ ] Format différent de l'épisode précédent (rotation A/B/C/D de `identity.md` §2) et une **mécanique neuve** (`brief.json.new_mechanic`).
- [ ] Script écrit à partir d'une recherche propre (≥ 5 sources nommées), pas d'un gabarit rempli.
- [ ] `originality.py script.md --ref published` (`identity.md` §3 bis) : 0 hit (pas de phrases recyclées d'un épisode à l'autre).
- [ ] Apport humain visible : choix éditoriaux, debrief de sécurité, humour du narrateur, mise en scène du jeu.

## 2. Contenu réutilisé et droits d'auteur
- [ ] Aucune séquence d'une autre chaîne. Photos et vidéos réelles seulement en CC0, domaine public (NOAA, USGS, NASA), licence Pexels, ou CC BY / CC BY-SA **crédités** (auteur, licence, lien) ; jamais NC ni ND.
- [ ] Sons CC0 ou Bibliothèque audio YouTube ; `credits.csv` joint à la fiche.
- [ ] `originality.py script.md --ref <transcriptions de la chaîne étudiée> --title "<titre>" --ref-titles channel.json` : 0 hit (ni phrase, ni tournure signature, ni titre trop proche).

## 3. Usurpation d'identité et imitation
- [ ] Nom, logo, bannière, miniature, police et palette propres à Nature Odds (`identity.md` §5). Jamais le nom, le style de miniature (gravure noire, flèche rouge, « IT … YOU.. ») ni les gabarits de titres d'une autre chaîne.
- [ ] Les questions génériques (« Can you survive… ») sont un usage commun ; la signature de la chaîne est le HUD de jeu et la mécanique, pas la question.

## 4. Contenu altéré ou synthétique (case « Altered or synthetic content » dans Studio)
Obligatoire pour un contenu **réaliste** qu'un spectateur pourrait prendre pour réel ; pas pour l'animation ou l'irréaliste évident. Les sources divergent sur les voix de synthèse réalistes.
- [ ] Images néon stylisées : non réalistes, case non requise pour elles.
- [ ] **Voix ElevenLabs réaliste : cocher « Oui »** par prudence, et le dire dans la description (`identity.md` §7).
- [ ] Jamais une image IA présentée comme une photo réelle d'animal ou de rencontre ; les archives réelles portent leur légende « REAL FOOTAGE · source ».

## 5. Exactitude, sécurité, métadonnées
- [ ] Chaque record, chaque rencontre `[vérifié]` par le Fact-checker ; les pourcentages de survie annoncés comme score de jeu, pas comme statistique.
- [ ] Debrief de sécurité tiré d'une source officielle ; rien n'incite à approcher, nourrir ou toucher un animal sauvage.
- [ ] Miniature et titre fidèles au contenu : la créature et le score de la miniature apparaissent dans la vidéo (pas d'appât trompeur).
- [ ] Pas de gore : la mort reste un écran GAME OVER.
- [ ] Public : « Non, ce contenu n'est pas conçu pour les enfants » (ton de jeu, mais sujets de danger réel) ; catégorie Éducation.

## Sources
- Politique officielle sur le contenu réutilisé : https://support.google.com/youtube/answer/87047
- Mise à jour « inauthentic content » de juillet 2025 : https://www.windowscentral.com/software-apps/youtube-ramps-up-campaign-against-ai-slop-with-stricter-monetization-caveats-on-inauthentic-and-repetitive-videos , https://alternativeto.net/news/2025/7/youtube-updates-its-policy-to-demonetize-inauthentic-mass-produced-ai-generated-content
- Contenu altéré ou synthétique : https://www.socialsamosa.com/news-2/youtube-mandates-disclosure-ai-videos-4369213 , https://air.io/en/youtube-glossary/what-is-youtubes-ai-content-disclosure-policy
