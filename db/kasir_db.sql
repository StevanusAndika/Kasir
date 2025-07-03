-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 03, 2025 at 05:36 PM
-- Server version: 8.0.30
-- PHP Version: 8.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kasir_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `id` int NOT NULL,
  `kode` varchar(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `satuan` varchar(20) DEFAULT NULL,
  `harga` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`id`, `kode`, `nama`, `satuan`, `harga`) VALUES
(1, '9556126640121', 'Rexona Ap Deo Aero', 'pcs', 12000),
(2, '9300830001743', 'Rexona Men Aero', 'pcs', 13500),
(3, '8999999000123', 'Indomie Goreng', 'bungkus', 3000),
(4, '8998899111223', 'Teh Botol Sosro', 'botol', 5000),
(5, '8886008101010', 'Aqua Botol 600ml', 'botol', 4500),
(6, '8996001301000', 'Kopi ABC Sachet', 'sachet', 2000),
(7, '8998888111122', 'Sabun Lifebuoy Merah', 'batang', 3500);

-- --------------------------------------------------------

--
-- Table structure for table `penjualan`
--

CREATE TABLE `penjualan` (
  `id` int NOT NULL,
  `tanggal` datetime DEFAULT NULL,
  `pelanggan` varchar(100) DEFAULT NULL,
  `sales` varchar(100) DEFAULT NULL,
  `jenis_pembayaran` varchar(10) DEFAULT NULL,
  `total` int DEFAULT NULL,
  `bayar` int DEFAULT NULL,
  `kembali` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `penjualan`
--

INSERT INTO `penjualan` (`id`, `tanggal`, `pelanggan`, `sales`, `jenis_pembayaran`, `total`, `bayar`, `kembali`) VALUES
(1, '2025-06-25 15:48:20', '', '', 'KREDIT', 24000, 3200000, 3176000),
(2, '2025-06-25 16:18:57', '', 'maulana', 'TUNAI', 30500, 50000, 19500),
(3, '2025-06-25 16:38:24', '', 'maulana', 'TUNAI', 27000, 50000, 23000),
(4, '2025-06-25 19:47:40', '', 'dwi', 'TUNAI', 16500, 20000, 3500);

-- --------------------------------------------------------

--
-- Table structure for table `penjualan_detail`
--

CREATE TABLE `penjualan_detail` (
  `id` int NOT NULL,
  `penjualan_id` int DEFAULT NULL,
  `kode_barang` varchar(20) DEFAULT NULL,
  `nama_barang` varchar(100) DEFAULT NULL,
  `jumlah` int DEFAULT NULL,
  `satuan` varchar(20) DEFAULT NULL,
  `harga` int DEFAULT NULL,
  `total` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `penjualan_detail`
--

INSERT INTO `penjualan_detail` (`id`, `penjualan_id`, `kode_barang`, `nama_barang`, `jumlah`, `satuan`, `harga`, `total`) VALUES
(1, 1, '9556126640121', 'Rexona Ap Deo Aero', 1, 'pcs', 12000, 12000),
(2, 1, '9556126640121', 'Rexona Ap Deo Aero', 1, 'pcs', 12000, 12000),
(3, 2, '9300830001743', 'Rexona Men Aero', 1, 'pcs', 13500, 13500),
(4, 2, '8998899111223', 'Teh Botol Sosro', 1, 'botol', 5000, 5000),
(5, 2, '9556126640121', 'Rexona Ap Deo Aero', 1, 'pcs', 12000, 12000),
(6, 3, '9300830001743', 'Rexona Men Aero', 1, 'pcs', 13500, 13500),
(7, 3, '9300830001743', 'Rexona Men Aero', 1, 'pcs', 13500, 13500),
(8, 4, '9300830001743', 'Rexona Men Aero', 1, 'pcs', 13500, 13500),
(9, 4, '8999999000123', 'Indomie Goreng', 1, 'bungkus', 3000, 3000);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'maulana', 'P@ssw0rd12'),
(2, 'Dwi', 'P@ssw0rd12'),
(8, 'yanty', '12345678'),
(9, 'Ika Novita Manurung', '4ce91c158da7ae5d1890743d4c209d37a3e358166cab79d8b3525d5efdf0237a');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode` (`kode`);

--
-- Indexes for table `penjualan`
--
ALTER TABLE `penjualan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `penjualan_detail`
--
ALTER TABLE `penjualan_detail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `barang`
--
ALTER TABLE `barang`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `penjualan`
--
ALTER TABLE `penjualan`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `penjualan_detail`
--
ALTER TABLE `penjualan_detail`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
