CREATE TABLE `flash_tools` (
  `id` int(10) NOT NULL,
  `flash_id` varchar(5) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `ejecutable` varchar(20) NOT NULL,
  `ruta_folder` varchar(100) NOT NULL,
  `grabar_llave` varchar(50) NOT NULL,
  `borrar_llave` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `modelos` (
  `id` int(10) NOT NULL,
  `flash_id` varchar(5) NOT NULL,
  `modelo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `orden_produccion` (
  `id` int(10) NOT NULL,
  `ordenDeProduccion` varchar(20) NOT NULL,
  `modelo` varchar(20) NOT NULL,
  `cantidad` int(3) NOT NULL,
  `fecha_creacion` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `series` (
  `id` int(10) NOT NULL,
  `serie_computer` varchar(19) NOT NULL,
  `windowsPkID` varchar(13) NOT NULL,
  `windowsPkey` varchar(19) NOT NULL,
  `ordenDeProduccion` varchar(20) NOT NULL,
  `fecha_inyeccion` date NOT NULL,
  `fecha_creacion` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;