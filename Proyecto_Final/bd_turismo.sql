-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-08-2024 a las 04:54:27
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_turismo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `guia`
--

CREATE TABLE `guia` (
  `nombre` varchar(30) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `genero` varchar(50) DEFAULT NULL,
  `experiencia` varchar(10) DEFAULT NULL,
  `idioma` varchar(50) DEFAULT NULL,
  `tarifa` decimal(10,2) DEFAULT NULL,
  `id_guia` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `guia`
--

INSERT INTO `guia` (`nombre`, `apellidos`, `edad`, `genero`, `experiencia`, `idioma`, `tarifa`, `id_guia`) VALUES
('Joaquin', 'Zamora', 30, 'Masculino', '10', 'Ingles', 1000.00, 'G001'),
('Martin', 'Zamada Herrera', 25, 'Masculino', '10', 'Espanol', 550.00, 'G002');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paseoturistas`
--

CREATE TABLE `paseoturistas` (
  `id_ruta` varchar(10) NOT NULL,
  `duracion` int(11) DEFAULT NULL,
  `guia` varchar(255) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `destino` varchar(255) DEFAULT NULL,
  `costo` decimal(10,2) DEFAULT NULL,
  `hora_partida` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservapaseo`
--

CREATE TABLE `reservapaseo` (
  `folio` int(11) NOT NULL,
  `id_ruta` varchar(10) DEFAULT NULL,
  `id_guia` varchar(10) DEFAULT NULL,
  `id_turista` varchar(10) DEFAULT NULL,
  `id_viaje` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaviaje`
--

CREATE TABLE `reservaviaje` (
  `folio` int(11) NOT NULL,
  `id_viaje` varchar(10) DEFAULT NULL,
  `id_turista` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reservaviaje`
--

INSERT INTO `reservaviaje` (`folio`, `id_viaje`, `id_turista`) VALUES
(1, 'V001', 'T002');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turista`
--

CREATE TABLE `turista` (
  `nombre` varchar(30) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `genero` varchar(50) DEFAULT NULL,
  `estancia` varchar(10) DEFAULT NULL,
  `id_turista` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `turista`
--

INSERT INTO `turista` (`nombre`, `apellidos`, `edad`, `genero`, `estancia`, `id_turista`) VALUES
('Jose', 'Martinez', 32, 'Femenino', '10 dias', 'T002'),
('Joaquin', 'Minchaca', 31, 'No Binario', '15 dias', 'T003');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nomusuario` varchar(100) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `contrasena` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nomusuario`, `correo`, `contrasena`) VALUES
(3, 'fer', 'fernando@gmail.com', 'fernan'),
(4, 'fersho', 'fercho@gmail.com', 'fernando'),
(5, 'ferni', 'fer@gmail.com', 'fer');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `viaje`
--

CREATE TABLE `viaje` (
  `id_viaje` varchar(10) NOT NULL,
  `destino` varchar(255) DEFAULT NULL,
  `salida` date DEFAULT NULL,
  `costo` decimal(10,2) DEFAULT NULL,
  `hora_partida` time DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `num_turistas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `viaje`
--

INSERT INTO `viaje` (`id_viaje`, `destino`, `salida`, `costo`, `hora_partida`, `estado`, `num_turistas`) VALUES
('V001', 'Los Angeles CA', '2024-09-24', 3000.00, '21:59:00', 'Pendiente', 10);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `guia`
--
ALTER TABLE `guia`
  ADD PRIMARY KEY (`id_guia`);

--
-- Indices de la tabla `paseoturistas`
--
ALTER TABLE `paseoturistas`
  ADD PRIMARY KEY (`id_ruta`);

--
-- Indices de la tabla `reservapaseo`
--
ALTER TABLE `reservapaseo`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `id_turista` (`id_turista`),
  ADD KEY `id_guia` (`id_guia`),
  ADD KEY `id_viaje` (`id_viaje`),
  ADD KEY `id_ruta` (`id_ruta`);

--
-- Indices de la tabla `reservaviaje`
--
ALTER TABLE `reservaviaje`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `id_viaje` (`id_viaje`),
  ADD KEY `id_turista` (`id_turista`);

--
-- Indices de la tabla `turista`
--
ALTER TABLE `turista`
  ADD PRIMARY KEY (`id_turista`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`);

--
-- Indices de la tabla `viaje`
--
ALTER TABLE `viaje`
  ADD PRIMARY KEY (`id_viaje`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `reservapaseo`
--
ALTER TABLE `reservapaseo`
  MODIFY `folio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reservaviaje`
--
ALTER TABLE `reservaviaje`
  MODIFY `folio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `reservapaseo`
--
ALTER TABLE `reservapaseo`
  ADD CONSTRAINT `reservapaseo_ibfk_3` FOREIGN KEY (`id_turista`) REFERENCES `turista` (`id_turista`),
  ADD CONSTRAINT `reservapaseo_ibfk_6` FOREIGN KEY (`id_guia`) REFERENCES `guia` (`id_guia`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reservapaseo_ibfk_7` FOREIGN KEY (`id_viaje`) REFERENCES `viaje` (`id_viaje`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reservapaseo_ibfk_8` FOREIGN KEY (`id_ruta`) REFERENCES `paseoturistas` (`id_ruta`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `reservaviaje`
--
ALTER TABLE `reservaviaje`
  ADD CONSTRAINT `reservaviaje_ibfk_1` FOREIGN KEY (`id_viaje`) REFERENCES `viaje` (`id_viaje`),
  ADD CONSTRAINT `reservaviaje_ibfk_2` FOREIGN KEY (`id_turista`) REFERENCES `turista` (`id_turista`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
