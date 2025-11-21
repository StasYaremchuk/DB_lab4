CREATE DATABASE IF NOT EXISTS `loreal_db4`;
USE `loreal_db4`;

DROP TABLE IF EXISTS `StoreContacts`;
DROP TABLE IF EXISTS `ProductPrices`;
DROP TABLE IF EXISTS `Stores`;
DROP TABLE IF EXISTS `ProductDescriptions`;
DROP TABLE IF EXISTS `BrandWebsites`;
DROP TABLE IF EXISTS `BrandProducts`;
DROP TABLE IF EXISTS `Products`;
DROP TABLE IF EXISTS `Categories`;
DROP TABLE IF EXISTS `Brands`;
DROP TABLE IF EXISTS `Addresses`;
DROP TABLE IF EXISTS `Countries`;


CREATE TABLE `Countries` (
  `country_id` INT NOT NULL AUTO_INCREMENT,
  `country_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`country_id`),
  UNIQUE INDEX `country_name` (`country_name` ASC)
);


CREATE TABLE `Addresses` (
  `address_id` INT NOT NULL AUTO_INCREMENT,
  `country_id` INT NOT NULL,
  `city` VARCHAR(100) NULL DEFAULT NULL,
  `street` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`address_id`),
  INDEX `country_id` (`country_id` ASC),
  INDEX `idx_city` (`city` ASC),
  FOREIGN KEY (`country_id`) REFERENCES `Countries`(`country_id`)
);


CREATE TABLE `Brands` (
  `brand_id` INT NOT NULL AUTO_INCREMENT,
  `brand_name` VARCHAR(100) NOT NULL,
  `description` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`brand_id`),
  UNIQUE INDEX `brand_name` (`brand_name` ASC),
  INDEX `idx_brand_name` (`brand_name` ASC)
);


CREATE TABLE `Categories` (
  `category_id` INT NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`category_id`),
  UNIQUE INDEX `category_name` (`category_name` ASC)
);

CREATE TABLE `Products` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(150) NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`product_id`),
  INDEX `idx_product_category` (`category_id` ASC),
  INDEX `idx_product_name` (`product_name` ASC),
  FOREIGN KEY (`category_id`) REFERENCES `Categories` (`category_id`)
);


CREATE TABLE `BrandProducts` (
  `brand_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  PRIMARY KEY (`brand_id`, `product_id`),
  FOREIGN KEY (`brand_id`) REFERENCES `Brands`(`brand_id`) ON DELETE CASCADE,
  FOREIGN KEY (`product_id`) REFERENCES `Products`(`product_id`) ON DELETE CASCADE
);


CREATE TABLE `BrandWebsites` (
  `website_id` INT NOT NULL AUTO_INCREMENT,
  `brand_id` INT NOT NULL,
  `url` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`website_id`),
  UNIQUE INDEX `idx_url` (`url` ASC),
  FOREIGN KEY (`brand_id`) REFERENCES `Brands`(`brand_id`)
);


CREATE TABLE `ProductDescriptions` (
  `description_id` INT NOT NULL AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `description` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`description_id`),
  FOREIGN KEY (`product_id`) REFERENCES `Products` (`product_id`)
);


CREATE TABLE `Stores` (
  `store_id` INT NOT NULL AUTO_INCREMENT,
  `store_name` VARCHAR(150) NOT NULL,
  `brand_id` INT NOT NULL,
  `address_id` INT NOT NULL,
  PRIMARY KEY (`store_id`),
  FOREIGN KEY (`brand_id`) REFERENCES `Brands` (`brand_id`),
  FOREIGN KEY (`address_id`) REFERENCES `Addresses` (`address_id`)
);


CREATE TABLE `ProductPrices` (
  `price_id` INT NOT NULL AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `store_id` INT NOT NULL,
  `price` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`price_id`),
  FOREIGN KEY (`product_id`) REFERENCES `Products` (`product_id`),
  FOREIGN KEY (`store_id`) REFERENCES `Stores` (`store_id`)
);


CREATE TABLE `StoreContacts` (
  `contact_id` INT NOT NULL AUTO_INCREMENT,
  `store_id` INT NOT NULL,
  `phone` VARCHAR(20) NULL,
  `email` VARCHAR(100) NULL,
  PRIMARY KEY (`contact_id`),
  FOREIGN KEY (`store_id`) REFERENCES `Stores` (`store_id`)
);


INSERT INTO `Countries` VALUES
(1,'Україна'),(2,'Польща'),(3,'Франція'),(4,'Німеччина'),(5,'Італія'),
(6,'Іспанія'),(7,'Великобританія'),(8,'США'),(9,'Канада'),(10,'Японія'),
(11,'Південна Корея'),(12,'Китай'),(13,'Австралія'),(14,'Бразилія'),(15,'Мексика');


INSERT INTO `Addresses` VALUES
(1,1,'Київ','вул. Хрещатик, 22'),
(2,1,'Львів','просп. Свободи, 10'),
(3,2,'Варшава','Marszalkowska, 50'),
(4,3,'Париж','Rue de Rivoli, 15'),
(5,4,'Берлін','Unter den Linden, 5'),
(6,5,'Рим','Via del Corso, 100'),
(7,6,'Мадрид','Gran Via, 25'),
(8,7,'Лондон','Oxford Street, 150'),
(9,8,'Нью-Йорк','5th Avenue, 200'),
(10,9,'Торонто','Yonge Street, 300'),
(11,10,'Токіо','Ginza, 5-5-5'),
(12,11,'Сеул','Myeongdong, 123'),
(13,12,'Пекін','Wangfujing 88'),
(14,13,'Сідней','George Street, 400'),
(15,14,'Ріо','Atlantica, 500');


INSERT INTO `Brands` VALUES
(1,'L''Oréal Paris','Основний бренд косметики'),
(2,'Garnier','Натуральні компоненти'),
(3,'Maybelline','Професійний макіяж'),
(4,'Kiehl''s','Преміум догляд'),
(5,'Lancôme','Французька розкіш'),
(6,'Vichy','Дерматологічна косметика'),
(7,'La Roche-Posay','Догляд для чутливої шкіри'),
(8,'Biotherm','Термальна вода'),
(9,'Yves Saint Laurent','Преміальна косметика'),
(10,'Giorgio Armani','Розкіш з Італії'),
(11,'Ralph Lauren','Американський стиль'),
(12,'Cacharel','Французький бренд'),
(13,'Helena Rubinstein','Антивікові інновації'),
(14,'Shu Uemura','Японські технології'),
(15,'Matrix','Догляд за волоссям');


INSERT INTO `Categories` VALUES
(1,'Шампунь'),(2,'Крем'),(3,'Тональний крем'),(4,'Помада'),(5,'Сироватка'),
(6,'Маска'),(7,'Гель'),(8,'Лосьйон'),(9,'Дезодорант'),(10,'Парфуми'),
(11,'Туш'),(12,'Тіні'),(13,'Пудра'),(14,'Консилер'),(15,'Бальзам');


INSERT INTO `Products` VALUES
(1,'Revitalift Cream',2),
(2,'Color Protect Shampoo',1),
(3,'Nutritional Mask',6),
(4,'Fit Me Foundation',3),
(5,'Lip Gloss',4),
(6,'Hydrating Serum',5),
(7,'Gentle Face Wash',7),
(8,'Repair Conditioner',1),
(9,'Lavender Hand Cream',2),
(10,'Micellar Water',8),
(11,'Ultra Light Sunscreen',2),
(12,'Anti-Dandruff Shampoo',1),
(13,'Volume Mascara',11),
(14,'Matte Lipstick',4),
(15,'Firming Cream',2);


INSERT INTO `BrandProducts` VALUES
(1,1),(1,2),(1,7),
(2,3),(2,6),
(3,4),(3,5),
(4,8),(4,10),
(5,9),
(6,11),
(7,12),
(8,13),
(9,14),
(10,15);


INSERT INTO `BrandWebsites` VALUES
(1,1,'https://www.lorealparis.com'),
(2,2,'https://www.garnier.com'),
(3,3,'https://www.maybelline.com'),
(4,4,'https://www.kiehls.com'),
(5,5,'https://www.lancome.com'),
(6,6,'https://www.vichy.com'),
(7,7,'https://www.laroche-posay.com'),
(8,8,'https://www.biotherm.com'),
(9,9,'https://www.ysl.com'),
(10,10,'https://www.giorgioarmanibeauty.com'),
(11,11,'https://www.ralphlauren.com'),
(12,12,'https://www.cacharel.com'),
(13,13,'https://www.helenarubinstein.com'),
(14,14,'https://www.shuuemura.com'),
(15,15,'https://www.matrix.com');


INSERT INTO `ProductDescriptions` VALUES
(1,1,'Антивіковий крем'),
(2,2,'Захист кольору'),
(3,3,'Маска з аргановою олією'),
(4,4,'Природне покриття'),
(5,5,'Блиск з вітаміном Е'),
(6,6,'Інтенсивне зволоження'),
(7,7,'Гель для чутливої шкіри'),
(8,8,'Кондиціонер для волосся'),
(9,9,'Крем для рук'),
(10,10,'Міцелярна вода'),
(11,11,'Крем з SPF 50'),
(12,12,'Проти лупи'),
(13,13,'Туш для обʼєму'),
(14,14,'Матова помада'),
(15,15,'Крем з ретинолом');


INSERT INTO `Stores` VALUES
(1,'L''Oréal Kyiv Store',1,1),
(2,'L''Oréal Lviv Store',1,2),
(3,'Garnier Warsaw',2,3),
(4,'Lancome Paris',5,4),
(5,'L''Oréal Berlin Store',1,5),
(6,'Kiehl''s Rome',4,6),
(7,'Maybelline Madrid',3,7),
(8,'Vichy London',6,8),
(9,'Biotherm New York',8,9),
(10,'La Roche-Posay Toronto',7,10),
(11,'Shu Uemura Tokyo',14,11),
(12,'YSL Seoul',9,12),
(13,'Armani Beijing',10,13),
(14,'Matrix Sydney',15,14),
(15,'L''Oréal Rio',1,15);


INSERT INTO `ProductPrices` VALUES
(1,1,1,450.00),(2,2,2,320.00),(3,3,3,150.00),(4,4,4,500.00),(5,5,5,250.00),
(6,6,6,380.00),(7,7,7,180.00),(8,8,8,420.00),(9,9,9,290.00),(10,10,10,210.00),
(11,11,11,350.00),(12,12,12,270.00),(13,13,13,190.00),(14,14,14,330.00),(15,15,15,480.00);

INSERT INTO `StoreContacts` VALUES
(1,1,'+380441234567','kyiv@loreal.com'),
(2,2,'+380322345678','lviv@loreal.com'),
(3,3,'+48221234567','warsaw@garnier.com'),
(4,4,'+33123456789','paris@lancome.com'),
(5,5,'+49301234567','berlin@loreal.com'),
(6,6,'+390612345678','rome@kiehls.com'),
(7,7,'+34123456789','madrid@maybelline.com'),
(8,8,'+442012345678','london@vichy.com'),
(9,9,'+12125551234','newyork@biotherm.com'),
(10,10,'+14165551234','toronto@larocheposay.com'),
(11,11,'+81312345678','tokyo@shuuemura.com'),
(12,12,'+82212345678','seoul@ysl.com'),
(13,13,'+861012345678','beijing@armani.com'),
(14,14,'+61298765432','sydney@matrix.com'),
(15,15,'+552112345678','rio@loreal.com');