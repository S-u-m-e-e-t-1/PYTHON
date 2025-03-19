-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 19, 2025 at 04:05 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `storemanagement`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`, `photo`, `phone`, `email`) VALUES
(1, 'admin1', 'admin1', 'admin1.png', '123-456-7890', 'alice.admin@example.com'),
(2, 'admin2', 'admin2', 'admin2.png', '234-567-8901', 'bob.admin@example.com');

-- --------------------------------------------------------

--
-- Table structure for table `attendances`
--

CREATE TABLE `attendances` (
  `id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendances`
--

INSERT INTO `attendances` (`id`, `staff_id`, `date`) VALUES
(0, 1, '2024-12-08');

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `bill_no` int(11) NOT NULL,
  `customer_name` varchar(255) NOT NULL,
  `contact` varchar(50) DEFAULT NULL,
  `date` date NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `mode_of_payment` varchar(50) NOT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `transaction_id` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bill_products`
--

CREATE TABLE `bill_products` (
  `bill_no` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dealers`
--

CREATE TABLE `dealers` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(255) NOT NULL,
  `outstanding` decimal(10,2) NOT NULL DEFAULT 0.00,
  `photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dealers`
--

INSERT INTO `dealers` (`id`, `name`, `address`, `phone`, `email`, `outstanding`, `photo`) VALUES
(1, 'Dealer One', '123 Main St', '123-456-7890', 'dealer1@example.com', 1000.00, 'dealer.jpg'),
(2, 'Dealer Two', '456 Elm St', '987-654-3210', 'dealer2@example.com', 500.00, 'dealer.jpg'),
(3, 'Dealer Three', '789 Oak St', '555-123-4567', 'dealer3@example.com', 750.00, 'dealer.jpg'),
(4, 'Dealer Four', '321 Pine St', '555-987-6543', 'dealer4@example.com', 300.00, 'dealer.jpg'),
(5, 'Dealer Five', '654 Maple St', '555-654-3210', 'dealer5@example.com', 1200.00, 'dealer.jpg'),
(6, 'Dealer Six', '987 Birch St', '555-321-0987', 'dealer6@example.com', 600.00, 'dealer.jpg'),
(7, 'Dealer Seven', '159 Cedar St', '555-789-0123', 'dealer7@example.com', 450.00, 'dealer.jpg'),
(8, 'Dealer Eight', '753 Spruce St', '555-456-7890', 'dealer8@example.com', 800.00, 'dealer.jpg'),
(9, 'Dealer Nine', '852 Willow St', '555-234-5678', 'dealer9@example.com', 950.00, 'dealer.jpg'),
(10, 'Dealer Ten', '951 Ash St', '555-678-1234', 'dealer10@example.com', 1100.00, 'dealer.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `dealer_id` int(11) NOT NULL,
  `photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `brand`, `price`, `quantity`, `dealer_id`, `photo`) VALUES
(1, 'Product A1', 'Brand X', 19.99, 100, 1, 'product.jpg'),
(2, 'Product A2', 'Brand X', 29.99, 50, 1, 'product.jpg'),
(3, 'Product A3', 'Brand X', 39.99, 75, 1, 'product.jpg'),
(4, 'Product A4', 'Brand X', 49.99, 20, 1, 'product.jpg'),
(5, 'Product A5', 'Brand X', 59.99, 30, 1, 'product.jpg'),
(6, 'Product B1', 'Brand Y', 19.99, 100, 2, 'product.jpg'),
(7, 'Product B2', 'Brand Y', 29.99, 50, 2, 'product.jpg'),
(8, 'Product B3', 'Brand Y', 39.99, 75, 2, 'product.jpg'),
(9, 'Product B4', 'Brand Y', 49.99, 20, 2, 'product.jpg'),
(11, 'Product C1', 'Brand Z', 20.00, 100, 4, 'product.jpg'),
(12, 'Product C2', 'Brand Z', 29.99, 50, 3, 'product.jpg'),
(13, 'Product C3', 'Brand Z', 39.99, 75, 3, 'product.jpg'),
(14, 'Product C4', 'Brand Z', 49.99, 20, 3, 'product.jpg'),
(15, 'Product C5', 'Brand Z', 59.99, 30, 3, 'product.jpg'),
(16, 'Product D1', 'Brand W', 19.99, 100, 4, 'product.jpg'),
(17, 'Product D2', 'Brand W', 29.99, 50, 4, 'product.jpg'),
(18, 'Product D3', 'Brand W', 39.99, 75, 4, 'product.jpg'),
(19, 'Product D4', 'Brand W', 49.99, 20, 4, 'product.jpg'),
(20, 'Product D5', 'Brand W', 59.99, 30, 4, 'product.jpg'),
(21, 'Product E1', 'Brand V', 19.99, 100, 5, 'product.jpg'),
(22, 'Product E2', 'Brand V', 29.99, 50, 5, 'product.jpg'),
(23, 'Product E3', 'Brand V', 39.99, 75, 5, 'product.jpg'),
(24, 'Product E4', 'Brand V', 49.99, 20, 5, 'product.jpg'),
(25, 'Product E5', 'Brand V', 59.99, 30, 5, 'product.jpg'),
(26, 'Product F1', 'Brand U', 19.99, 100, 6, 'product.jpg'),
(27, 'Product F2', 'Brand U', 29.99, 50, 6, 'product.jpg'),
(28, 'Product F3', 'Brand U', 39.99, 75, 6, 'product.jpg'),
(29, 'Product F4', 'Brand U', 49.99, 20, 6, 'product.jpg'),
(30, 'Product F5', 'Brand U', 59.99, 30, 6, 'product.jpg'),
(31, 'Product G1', 'Brand T', 19.99, 100, 7, 'product.jpg'),
(32, 'Product G2', 'Brand T', 29.99, 50, 7, 'product.jpg'),
(33, 'Product G3', 'Brand T', 39.99, 75, 7, 'product.jpg'),
(34, 'Product G4', 'Brand T', 49.99, 20, 7, 'product.jpg'),
(35, 'Product G5', 'Brand T', 59.99, 30, 7, 'product.jpg'),
(36, 'Product H1', 'Brand S', 19.99, 100, 8, 'product.jpg'),
(37, 'Product H2', 'Brand S', 29.99, 50, 8, 'product.jpg'),
(38, 'Product H3', 'Brand S', 39.99, 75, 8, 'product.jpg'),
(39, 'Product H4', 'Brand S', 49.99, 20, 8, 'product.jpg'),
(40, 'Product H5', 'Brand S', 59.99, 30, 8, 'product.jpg'),
(41, 'Product I1', 'Brand R', 19.99, 100, 9, 'product.jpg'),
(42, 'Product I2', 'Brand R', 29.99, 50, 9, 'product.jpg'),
(43, 'Product I3', 'Brand R', 39.99, 75, 9, 'product.jpg'),
(44, 'Product I4', 'Brand R', 49.99, 20, 9, 'product.jpg'),
(45, 'Product I5', 'Brand R', 59.99, 30, 9, 'product.jpg'),
(46, 'Product J1', 'Brand Q', 19.99, 100, 10, 'product.jpg'),
(47, 'Product J2', 'Brand Q', 29.99, 50, 10, 'product.jpg'),
(48, 'Product J3', 'Brand Q', 39.99, 75, 10, 'product.jpg'),
(49, 'Product J4', 'Brand Q', 49.99, 20, 10, 'product.jpg'),
(50, 'Product J5', 'Brand Q', 59.99, 30, 10, 'product.jpg'),
(51, 'abc', 'brand c', 23.00, 123, 10, 'JAGA.jpg'),
(52, 'whd', 'jdh', 123.00, 45, 4, 'download.png'),
(53, 'sumeet', 'gicm', 123.00, 345, 5, 'logo.png');

-- --------------------------------------------------------

--
-- Table structure for table `salary`
--

CREATE TABLE `salary` (
  `transaction_id` int(11) NOT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `amount` decimal(10,2) NOT NULL,
  `date` date NOT NULL,
  `mode` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`bill_no`),
  ADD KEY `staff_id` (`staff_id`);

--
-- Indexes for table `bill_products`
--
ALTER TABLE `bill_products`
  ADD PRIMARY KEY (`bill_no`,`product_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `dealers`
--
ALTER TABLE `dealers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_dealer` (`dealer_id`);

--
-- Indexes for table `salary`
--
ALTER TABLE `salary`
  ADD PRIMARY KEY (`transaction_id`),
  ADD KEY `staff_id` (`staff_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `bill_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1067;

--
-- AUTO_INCREMENT for table `dealers`
--
ALTER TABLE `dealers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `salary`
--
ALTER TABLE `salary`
  MODIFY `transaction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65869;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`id`);

--
-- Constraints for table `bill_products`
--
ALTER TABLE `bill_products`
  ADD CONSTRAINT `bill_products_ibfk_1` FOREIGN KEY (`bill_no`) REFERENCES `bill` (`bill_no`),
  ADD CONSTRAINT `bill_products_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `fk_dealer` FOREIGN KEY (`dealer_id`) REFERENCES `dealers` (`id`);

--
-- Constraints for table `salary`
--
ALTER TABLE `salary`
  ADD CONSTRAINT `salary_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
