-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Client :  localhost
-- Généré le :  Mer 27 Mai 2020 à 20:21
-- Version du serveur :  5.7.29
-- Version de PHP :  5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `in19b1010`
--

-- --------------------------------------------------------

--
-- Structure de la table `web1_categorie`
--

CREATE TABLE `web1_categorie` (
  `id_categorie` int(11) NOT NULL,
  `categorie` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `web1_categorie`
--

INSERT INTO `web1_categorie` (`id_categorie`, `categorie`) VALUES
(1, 'Art'),
(2, 'BD'),
(5, 'Construction'),
(3, 'Films/Videos'),
(14, 'Informatique'),
(10, 'Jeux'),
(19, 'Luminaires'),
(4, 'Mode'),
(6, 'Musique'),
(12, 'Photographie'),
(15, 'Technologie'),
(16, 'Theatre');

-- --------------------------------------------------------

--
-- Structure de la table `web1_commentaire`
--

CREATE TABLE `web1_commentaire` (
  `id_comment` int(11) NOT NULL,
  `commentaire` text NOT NULL,
  `date_mise_en_ligne` date NOT NULL,
  `id_projet` int(11) NOT NULL,
  `id_membre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `web1_commentaire`
--

INSERT INTO `web1_commentaire` (`id_comment`, `commentaire`, `date_mise_en_ligne`, `id_projet`, `id_membre`) VALUES
(5, 'Superbe BD ! ', '2020-04-27', 7, 1),
(25, 'Hate de voir ca', '2020-04-11', 14, 21),
(27, 'Mais comment je vais passer avec mon bateau ??', '2020-04-11', 14, 23),
(30, 'Hâte de voir cela', '2020-04-28', 13, 23),
(34, 'Je compte installer ce système audio chez moi dès qu\'il sera disponible !', '2020-05-01', 17, 30),
(35, 'Ma femme souhaite la recevoir pour son anniversaire, je vais donc la lui offrir !', '2020-05-01', 9, 30),
(36, 'Hâte de lire cette BD qui parle du meilleur ami de Rintintin !', '2020-05-09', 8, 37),
(38, 'Super projet ! Je me réjouis d\'y jouer toutes les nuits !', '2020-05-09', 19, 34),
(39, 'Pas mal, je le vois bien dans le garage avec les autres enceintes', '2020-05-09', 17, 34),
(40, 'Mes copaiiiins !', '2020-05-09', 13, 34),
(41, 'Ça me sera bien utile dans la jungle pour faire fuir les tigres et autres animaux sauvages !', '2020-05-10', 17, 21),
(42, 'Pas mal pour se détendre entre 2 combats aux couteaux', '2020-05-10', 13, 21),
(43, 'A lire entre 2 BD des Schtroumpfs.', '2020-05-10', 8, 21),
(44, 'Lorsque mon trek sera terminé, je m\'installerai et ce jeu vidéo sera mon nouveau combat !', '2020-05-10', 19, 21),
(45, 'Pauvre gamin… Allez je t\'aide à avoir des amis !', '2020-05-10', 26, 23),
(46, 'J\'adore tes films moussaillon !', '2020-05-10', 28, 23),
(47, 'J\'adore vraiment tous tes films !', '2020-05-10', 27, 23),
(48, 'Franchement, pas mal le gilet, tu me le prêteras ?', '2020-05-10', 28, 37),
(49, 'Wow la relève de Mario ?', '2020-05-10', 19, 37),
(50, 'Le pauvre…… \r\nJe suis vraiment très triste pour toi', '2020-05-10', 26, 37),
(51, 'Laisse moi t\'aider mon petit', '2020-05-10', 26, 30),
(52, 'J\'en aurai besoin pour divertir mes enfants ;)', '2020-05-10', 29, 30),
(53, 'Pas mal ! Mes enfants adoreront !', '2020-05-10', 19, 30),
(54, 'Oufti oui vite un abri pour le pauvre homme', '2020-05-10', 30, 36);

-- --------------------------------------------------------

--
-- Structure de la table `web1_fichier`
--

CREATE TABLE `web1_fichier` (
  `id_fichier` int(11) NOT NULL,
  `url` varchar(50) NOT NULL,
  `id_news` int(11) DEFAULT NULL,
  `id_projet` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `web1_membre`
--

CREATE TABLE `web1_membre` (
  `id_membre` int(11) NOT NULL,
  `login` varchar(50) NOT NULL,
  `avatar` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `courriel` varchar(55) NOT NULL,
  `mot_passe` varchar(255) NOT NULL,
  `tel` varchar(14) DEFAULT NULL,
  `carte_VISA` varchar(19) NOT NULL,
  `adresse_rue` varchar(100) DEFAULT NULL,
  `adresse_numero` int(11) DEFAULT NULL,
  `adresse_code` int(11) DEFAULT NULL,
  `adresse_ville` varchar(50) DEFAULT NULL,
  `adresse_province` varchar(55) DEFAULT NULL,
  `adresse_pays` varchar(50) DEFAULT NULL,
  `est_desactive` tinyint(1) NOT NULL DEFAULT '0',
  `est_admin` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `web1_membre`
--

INSERT INTO `web1_membre` (`id_membre`, `login`, `avatar`, `prenom`, `nom`, `courriel`, `mot_passe`, `tel`, `carte_VISA`, `adresse_rue`, `adresse_numero`, `adresse_code`, `adresse_ville`, `adresse_province`, `adresse_pays`, `est_desactive`, `est_admin`) VALUES
(1, 'fabbodson', '5ea6b44cd4c7f.jpg', 'Fabrice', 'Bodson', 'fa.bodson@student.helmo.be', 'b117bc7ae6531d4519190f53e9c9d56e3149ffcf70d2cc631240aa7cfe48c629560831d882f31da4facd997f4dbad7cdff1e76ca23d959f273b90416bbf539e3', '041234567', '1234567812345670', 'rue de la plage', 20, 7854, 'Liège', 'Luxembourg', 'Belgique', 0, 1),
(21, 'Rambo', '5e92d12ee24fb.jpg', 'Sylvester', 'Stallone', 'ss@gmail.com', 'c6ee9e33cf5c6715a1d148fd73f7318884b41adcb916021e2bc0e800a5c5dd97f5142178f6ae88c8fdd98e1afb0ce4c8d2c54b5f37b30b7da1997bb33b0b8a31', '041234567', '1234567812345670', 'Rue du vin', 31, 5000, 'Los Angeles', 'Hainaut', 'Belgique', 0, 1),
(23, 'CaptainHaddock', '5eb6be6d41448.png', 'Capitaine', 'Haddock', 'Capi.hadok@gmail.com', 'eb60db82849a70f2549efcd8519868908916b49c31b211a95d449a484cbc81bd2352241e32c8cc38b08f09b9b1ebdb787699db5330f81a135b6f2eb8b347b342', '041234567', '1234567812345670', 'Moulinsart', 31, 8977, 'Virton', 'Luxembourg', 'Belgique', 0, 0),
(28, 'DonaldDuck', '5eaac6e7c81e9.png', 'Donald', 'Duck', 'Dd.duck@duckduck.go', '8c77dd9eac0d430d360c0ca72c96aaa508725f6a3e964413d0c9127f773b92cfb9aaf0e008503a3a9525c26fb95f89be0475ec9c7113febccc23666ec5f506e9', '012345667', '1234567812345670', 'Chez Mickey', 13, 1313, 'Souris city', 'Brabant Wallon', 'Disney', 0, 0),
(30, 'CR7', '5eabfbf4e3528.jpg', 'Cristiano', 'Ronaldo', 'C.ronaldo@gmail.com', '4647e43e7bf8f363b9efdabe7c0929b471489030904e3fa3ced7600b90dc8ae6a2e0d446728c84f27e5d44b6da6f2e5f9bcf49412ac6bbdd4241bfa9cd835b36', '012345667', '1234567812345670', 'Rue de Turin', 7, 7777, 'Turin', 'Liège', 'Italie', 0, 0),
(34, 'Pinocchio', '5eaf0ada932e1.jpg', 'Pinocchio', 'EnBois', 'P.bois@gmail.com', '3fe8ba87f06ea33ad4edea47e84252f73a889dec1a44be7f9b43aee639f86785c696faefd4be595c7cb2de5e44b62336ad220ff1b87280cf61b003b9f3a13895', '0123456', '1234567812345670', 'Rue dans le bois', 13, 1313, 'Rome', 'Flandre Orientale', 'Italie', 0, 0),
(35, 'Avatar', '5eb14a2cdb3d8.png', 'Avatar', 'Maitre de l\'air', 'Av.tar@gmail.com', '5675e9f1921f4b2e3e242b71693cfd9d6332c81e0edc74f04b056da85cad77d5d921a29d712c4184379715e46ffe1afbcf61919337fb2540707361da0f8632aa', '012345667', '1234567812345670', 'Rue de l\'air', 9, 9999, 'Liege', 'Liège', 'Belgique', 0, 0),
(36, 'Feudedieu', '5eb16a91205fa.jpg', 'Camouu', 'Dupont', 'Petitponey@gmail.com', '810c0725cea8d08633795374c77db6cada8e8836c36ff9648b4a11591492e84c5f087eb316cdf86457351a0fd4a3be3d722a7e8d986132defe183010f144fe61', '0432764319', '1234567812345670', 'Rue de l\'écurie', 28, 2828, 'Prairie', 'Luxembourg', 'Pays merveilleux', 0, 0),
(37, 'John Doe', '5eb6bf34b3a23.jpg', 'John', 'Doe', 'J.d@gmail.com', 'ed61623e7c566e3504a5ca78daebbe798e894cbd8b0ec7304dc751af6d67b63bdb593bdf447adc59b2710b84d99cc3e0a875503a78708506799209288e2ae6d8', '012345667', '1234567812345670', 'Rue de l\'eau', 42, 4242, 'Aquapolis', 'Flandre Occidentale', 'Belgique', 0, 0),
(38, 'Jean', '5ec24a6c17618.jpg', 'Jean', 'Jean', 'Jean@gmail.com', '7f3adfdfdcd5c9f3bcb7e66302197583cdd04e7f6009918f9dd51a95fb666fdef060d549cc075bffcb5108198289dfbd9d37a42acbb9359a3a96d5b488ec9c9c', '0687895626', '1234567812345670', 'Rue du pré jean', 45, 7856, 'Jeanville', 'Namur', 'Jeanland', 0, 0),
(39, 'Aezing', '5ecd048901cb1.png', 'Antoine', 'Valente', 'Antoine_valente@hotmail.com', '51c486fafd57f659fb92dfcb83d039351bcc16fdada7bad7a5c7d88e707b4250de723974ce0ba6448fc8de9d75c0e2bdd9c6a42c06d32944e108fdffd81b66d5', '+32495940924', '1234567812345670', 'Rue de Jehanster', 3, 4800, 'Verviers', 'Anvers', 'Belgique', 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `web1_news`
--

CREATE TABLE `web1_news` (
  `id_news` int(11) NOT NULL,
  `intitule` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `date_publication` date NOT NULL,
  `id_projet` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `web1_news`
--

INSERT INTO `web1_news` (`id_news`, `intitule`, `description`, `date_publication`, `id_projet`) VALUES
(1, 'Rantanplan', 'Voici Rantanplan, le nouveau personnage de mon roman ! Qui est-il ? C\'est tout simplement le meilleur ami de Rintintin !', '2020-04-28', 8),
(4, 'Planche finale', 'Voici la planche finale de ma BD', '2020-04-12', 8),
(9, 'Premiere grue achetee', 'A chaque étape sa news, aujourd\'hui nous avons achté une premiere grue !', '2020-04-12', 14),
(15, 'Couverture choisie', 'Après de nombreux brouillons, voici enfin arrivée la planche qui servira de couverture pour ma bande dessinée', '2020-05-09', 7);

-- --------------------------------------------------------

--
-- Structure de la table `web1_participation`
--

CREATE TABLE `web1_participation` (
  `id_participation` int(11) NOT NULL,
  `date_participation` date NOT NULL,
  `montant` double NOT NULL,
  `id_membre` int(11) NOT NULL,
  `id_projet` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `web1_participation`
--

INSERT INTO `web1_participation` (`id_participation`, `date_participation`, `montant`, `id_membre`, `id_projet`) VALUES
(23, '2020-04-12', 5, 21, 8),
(30, '2020-04-12', 20, 1, 13),
(31, '2020-04-12', 1, 21, 13),
(36, '2020-04-12', 100, 1, 7),
(39, '2020-04-27', 12, 1, 19),
(40, '2020-04-27', 55, 1, 14),
(41, '2020-04-27', 15, 21, 19),
(42, '2020-04-27', 13, 21, 17),
(43, '2020-04-27', 50, 21, 14),
(44, '2020-04-27', 5, 23, 17),
(45, '2020-04-27', 35, 23, 14),
(70, '2020-05-01', 5, 30, 13),
(71, '2020-05-01', 50, 30, 17),
(72, '2020-05-01', 10000, 30, 9),
(73, '2020-05-05', 500, 36, 14),
(74, '2020-05-09', 25, 37, 8),
(76, '2020-05-09', 15, 34, 19),
(77, '2020-05-09', 25, 34, 17),
(78, '2020-05-09', 13, 34, 13),
(79, '2020-05-10', 50, 23, 26),
(80, '2020-05-10', 30, 23, 28),
(81, '2020-05-10', 10, 23, 27),
(82, '2020-05-10', 45, 37, 28),
(83, '2020-05-10', 100, 37, 19),
(84, '2020-05-10', 100, 37, 26),
(85, '2020-05-10', 125, 30, 26),
(86, '2020-05-10', 173, 30, 29),
(87, '2020-05-10', 1500, 30, 19),
(88, '2020-05-10', 200, 36, 30),
(89, '2020-05-18', 45, 38, 28);

-- --------------------------------------------------------

--
-- Structure de la table `web1_projet`
--

CREATE TABLE `web1_projet` (
  `id_projet` int(11) NOT NULL,
  `intitule` varchar(50) NOT NULL,
  `date_echeance` date NOT NULL,
  `date_creation` date NOT NULL,
  `description` text NOT NULL,
  `montant` double NOT NULL,
  `montant_actuel` int(11) NOT NULL DEFAULT '0',
  `montant_minimum` int(11) NOT NULL,
  `illustration_apercu` varchar(100) NOT NULL,
  `carte_VISA` varchar(19) NOT NULL,
  `nom_VISA` varchar(50) NOT NULL,
  `est_prolonge` tinyint(1) NOT NULL DEFAULT '0',
  `est_valide` tinyint(1) NOT NULL DEFAULT '0',
  `taux_participation` double NOT NULL,
  `id_membre` int(11) NOT NULL,
  `id_type_part` int(11) NOT NULL,
  `id_categorie` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `web1_projet`
--

INSERT INTO `web1_projet` (`id_projet`, `intitule`, `date_echeance`, `date_creation`, `description`, `montant`, `montant_actuel`, `montant_minimum`, `illustration_apercu`, `carte_VISA`, `nom_VISA`, `est_prolonge`, `est_valide`, `taux_participation`, `id_membre`, `id_type_part`, `id_categorie`) VALUES
(7, 'RINTINTIN', '2020-04-20', '2020-04-08', 'Rintintin le meilleur ami de Max ! Toujours prêt pour de nouvelles aventures !Rejoignez la !', 100, 100, 1, '5e92c04302093.jpg', '1234-5678-1234-5670', 'bodson', 0, 1, 1, 1, 1, 1),
(8, 'RINPLINPLIN', '2020-07-30', '2020-04-09', 'La bande dessinée sur les aventures du copain de Rintintin!', 100, 30, 1, '5eb7c783e1f18.jpg', '1214-5978-1132-568', 'dupont', 0, 0, 0.3, 1, 3, 2),
(9, 'ROBE SWAG', '2020-08-17', '2020-04-10', 'Robe de nouvelle tendance !', 10000, 10000, 1, '5eb7d8543c3e4.jpg', '1234-5678-1234-5670', 'dupont', 0, 0, 1, 1, 4, 4),
(13, 'SCHTROUMPFS', '2020-05-22', '2020-04-10', 'Le nouveau schtroumpfs volant est de sortie !', 42, 39, 1, '5e906f17c7752.jpg', '1234-5678-1234-5670', 'peyo', 0, 0, 0.93, 1, 4, 2),
(14, 'PONT D\'AVIGNON', '2020-07-21', '2020-04-10', 'Sur le pont d\'avignon, on y danse on y danse, sur le pont d\'avignon....', 7839, 640, 1, '5eb7d7b078074.jpg', '1234-5678-1234-5670', 'pontois', 0, 0, 0.08, 1, 1, 5),
(17, 'POWERON', '2020-06-25', '2020-04-10', 'Augmentez le volume !!', 100, 93, 1, '5e908442751ab.jpg', '1234-5678-1234-5670', 'drdre', 0, 0, 0.93, 1, 1, 6),
(19, 'MARIA', '2020-10-22', '2020-04-12', 'Maria DB le nouveau jeu totalement givré !', 1918, 1642, 1, '5e92edc78f2dc.jpg', '1234-5678-1234-5670', 'nintendo', 0, 0, 0.86, 21, 4, 10),
(26, 'MARIONNETTES', '2020-08-20', '2020-05-09', 'Pour me faire des amies, je compte créer d\'autres marionettes afin de jouer avec eux !', 300, 275, 2, '5eb6d1140ef49.jpg', '1234-5678-1234-5670', 'jeppeto', 0, 0, 0.92, 34, 1, 1),
(27, 'BANDANA', '2020-07-10', '2020-05-10', 'Il me faut un nouveau bandana d\'urgence, l\'autre je l\'ai perdu dans Rambo 3…', 10, 10, 1, '5eb7ceecd2219.jpg', '1234-5678-1234-5670', 'rambo', 0, 0, 1, 21, 1, 1),
(28, 'GILET DE CAMOUFLAGE', '2020-07-10', '2020-05-10', 'J\'ai bousillé ma veste militaire de camouflage lors de ma dernière expérience de survie dans les bois.', 250, 120, 2, '5eb7d04a22432.jpg', '1234-5678-1234-5670', 'rambo', 0, 0, 0.48, 21, 1, 4),
(29, 'PINOCCHIO ET SES AMIS', '2020-09-30', '2020-05-10', 'Mon histoire est plutôt folle, Gepetto m\'a donc conseillé de relater mes aventures sous forme de bande dessinée', 200, 173, 1, '5eb7d4bab2183.jpg', '1234-5678-1234-5670', 'gepetto', 0, 0, 0.87, 34, 1, 2),
(30, 'ABRI DE GEPETTO', '2020-09-24', '2020-05-10', 'Gepetto a besoin d\'un nouvel abri pour ses marionnettes, aidez le svp', 1000, 200, 5, '5eb7d58a340ec.jpg', '1234-5678-1234-5670', 'gepetto', 0, 0, 0.2, 34, 1, 5);

-- --------------------------------------------------------

--
-- Structure de la table `web1_seuil_recompense`
--

CREATE TABLE `web1_seuil_recompense` (
  `id_seuil` int(11) NOT NULL,
  `montant` float NOT NULL,
  `contrepartie` text,
  `id_projet` int(11) NOT NULL,
  `id_type_part` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `web1_type_participation`
--

CREATE TABLE `web1_type_participation` (
  `id_type_part` int(11) NOT NULL,
  `libelle` varchar(50) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `web1_type_participation`
--

INSERT INTO `web1_type_participation` (`id_type_part`, `libelle`, `description`) VALUES
(1, 'don', 'Aucune contrepartie n’est promise au donateur'),
(2, 'recompense', 'En fonction du montant offert, des paliers de cadeaux peuvent être proposés à la concrétisation du projet'),
(3, 'pret', 'Après un délai annoncé écoulé depuis la concrétisation du projet, le donateur est remboursé avec intérêt'),
(4, 'capital', 'Le donateur reçoit un certain nombre de parts de la société');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `web1_categorie`
--
ALTER TABLE `web1_categorie`
  ADD PRIMARY KEY (`id_categorie`),
  ADD UNIQUE KEY `web1_categorie_categorie_uindex` (`categorie`);

--
-- Index pour la table `web1_commentaire`
--
ALTER TABLE `web1_commentaire`
  ADD PRIMARY KEY (`id_comment`),
  ADD KEY `web1_commentaire_ibfk2` (`id_membre`),
  ADD KEY `web1_commentaire_ibfk_1` (`id_projet`);

--
-- Index pour la table `web1_fichier`
--
ALTER TABLE `web1_fichier`
  ADD PRIMARY KEY (`id_fichier`),
  ADD KEY `web1_fichier_ibfk_1` (`id_news`),
  ADD KEY `web1_fichier_ibfk_2` (`id_projet`);

--
-- Index pour la table `web1_membre`
--
ALTER TABLE `web1_membre`
  ADD PRIMARY KEY (`id_membre`),
  ADD UNIQUE KEY `login` (`login`);

--
-- Index pour la table `web1_news`
--
ALTER TABLE `web1_news`
  ADD PRIMARY KEY (`id_news`),
  ADD KEY `web1_news_ibfk_1` (`id_projet`);

--
-- Index pour la table `web1_participation`
--
ALTER TABLE `web1_participation`
  ADD PRIMARY KEY (`id_participation`),
  ADD KEY `web1_participation_ibfk_1` (`id_membre`),
  ADD KEY `web1_participation_ibfk_2` (`id_projet`);

--
-- Index pour la table `web1_projet`
--
ALTER TABLE `web1_projet`
  ADD PRIMARY KEY (`id_projet`),
  ADD KEY `web1_projet_ibfk_2` (`id_type_part`),
  ADD KEY `web1_projet_ibfk_1` (`id_membre`),
  ADD KEY `web1_projet_ibfk_3` (`id_categorie`);

--
-- Index pour la table `web1_seuil_recompense`
--
ALTER TABLE `web1_seuil_recompense`
  ADD PRIMARY KEY (`id_seuil`),
  ADD UNIQUE KEY `web1_seuil_recompense_montant_uindex` (`montant`),
  ADD KEY `web1_seuil_recompense_ibfk_2` (`id_type_part`),
  ADD KEY `web1_seuil_recompense_ibfk_1` (`id_projet`);

--
-- Index pour la table `web1_type_participation`
--
ALTER TABLE `web1_type_participation`
  ADD PRIMARY KEY (`id_type_part`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `web1_categorie`
--
ALTER TABLE `web1_categorie`
  MODIFY `id_categorie` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT pour la table `web1_commentaire`
--
ALTER TABLE `web1_commentaire`
  MODIFY `id_comment` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;
--
-- AUTO_INCREMENT pour la table `web1_fichier`
--
ALTER TABLE `web1_fichier`
  MODIFY `id_fichier` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `web1_membre`
--
ALTER TABLE `web1_membre`
  MODIFY `id_membre` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
--
-- AUTO_INCREMENT pour la table `web1_news`
--
ALTER TABLE `web1_news`
  MODIFY `id_news` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT pour la table `web1_participation`
--
ALTER TABLE `web1_participation`
  MODIFY `id_participation` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=90;
--
-- AUTO_INCREMENT pour la table `web1_projet`
--
ALTER TABLE `web1_projet`
  MODIFY `id_projet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT pour la table `web1_seuil_recompense`
--
ALTER TABLE `web1_seuil_recompense`
  MODIFY `id_seuil` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `web1_type_participation`
--
ALTER TABLE `web1_type_participation`
  MODIFY `id_type_part` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `web1_commentaire`
--
ALTER TABLE `web1_commentaire`
  ADD CONSTRAINT `web1_commentaire_ibfk2` FOREIGN KEY (`id_membre`) REFERENCES `web1_membre` (`id_membre`),
  ADD CONSTRAINT `web1_commentaire_ibfk_1` FOREIGN KEY (`id_projet`) REFERENCES `web1_projet` (`id_projet`) ON DELETE CASCADE;

--
-- Contraintes pour la table `web1_fichier`
--
ALTER TABLE `web1_fichier`
  ADD CONSTRAINT `web1_fichier_ibfk_1` FOREIGN KEY (`id_news`) REFERENCES `web1_news` (`id_news`),
  ADD CONSTRAINT `web1_fichier_ibfk_2` FOREIGN KEY (`id_projet`) REFERENCES `web1_projet` (`id_projet`);

--
-- Contraintes pour la table `web1_news`
--
ALTER TABLE `web1_news`
  ADD CONSTRAINT `web1_news_ibfk_1` FOREIGN KEY (`id_projet`) REFERENCES `web1_projet` (`id_projet`) ON DELETE CASCADE;

--
-- Contraintes pour la table `web1_participation`
--
ALTER TABLE `web1_participation`
  ADD CONSTRAINT `web1_participation_ibfk_1` FOREIGN KEY (`id_membre`) REFERENCES `web1_membre` (`id_membre`),
  ADD CONSTRAINT `web1_participation_ibfk_2` FOREIGN KEY (`id_projet`) REFERENCES `web1_projet` (`id_projet`) ON DELETE CASCADE;

--
-- Contraintes pour la table `web1_projet`
--
ALTER TABLE `web1_projet`
  ADD CONSTRAINT `web1_projet_ibfk_1` FOREIGN KEY (`id_membre`) REFERENCES `web1_membre` (`id_membre`),
  ADD CONSTRAINT `web1_projet_ibfk_2` FOREIGN KEY (`id_type_part`) REFERENCES `web1_type_participation` (`id_type_part`),
  ADD CONSTRAINT `web1_projet_ibfk_3` FOREIGN KEY (`id_categorie`) REFERENCES `web1_categorie` (`id_categorie`);

--
-- Contraintes pour la table `web1_seuil_recompense`
--
ALTER TABLE `web1_seuil_recompense`
  ADD CONSTRAINT `web1_seuil_recompense_ibfk_1` FOREIGN KEY (`id_projet`) REFERENCES `web1_projet` (`id_projet`),
  ADD CONSTRAINT `web1_seuil_recompense_ibfk_2` FOREIGN KEY (`id_type_part`) REFERENCES `web1_type_participation` (`id_type_part`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
