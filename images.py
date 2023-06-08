import psycopg2

def write_image(facid,file_path):

    img =  open(file_path, "rb").read()

    conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
    crsr = conn.cursor()
    try :
        
            crsr.execute("UPDATE Facs SET facimg = %s WHERE facid = %s", (psycopg2.Binary(img), facid))
            conn.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        
            print(error)
    finally:
           conn.close()
        


write_image(1, "A:/FACULTATE/LICENTA/static/facultati/UPB/upb-automatica.png")
write_image(2, "A:/FACULTATE/LICENTA/static/facultati/UPB/upb-automatica.png")
write_image(3, "A:/FACULTATE/LICENTA/static/facultati/UPB/upb-automatica.png")
write_image(4, "A:/FACULTATE/LICENTA/static/facultati/UPB/upb-automatica.png")
write_image(5, "A:/FACULTATE/LICENTA/static/facultati/UPB/inginerie_electrica_upb.png")
write_image(6, "A:/FACULTATE/LICENTA/static/facultati/UPB/energetica_upb.png")
write_image(7, "A:/FACULTATE/LICENTA/static/facultati/UPB/etti.png")
write_image(8, "A:/FACULTATE/LICENTA/static/facultati/UPB/etti.png")
write_image(9, "A:/FACULTATE/LICENTA/static/facultati/UPB/inginerie_mecanica_si_mecatronica_upb.png")
write_image(10, "A:/FACULTATE/LICENTA/static/facultati/UPB/inginerie_industriala_si_robotica_upb.png")
write_image(11, "A:/FACULTATE/LICENTA/static/facultati/UPB/ingineria_sistemelor_biotehnice_upb.png")
write_image(12, "A:/FACULTATE/LICENTA/static/facultati/UPB/transporturi_upb.png")
write_image(13, "A:/FACULTATE/LICENTA/static/facultati/UPB/aerospatiala_upb.png")
write_image(14, "A:/FACULTATE/LICENTA/static/facultati/UPB/stiinta_si_ingineria_materialelor_upb.png")
write_image(15, "A:/FACULTATE/LICENTA/static/facultati/UPB/inginerie_chimica_si_biotehnologii_upb.png")
write_image(16, "A:/FACULTATE/LICENTA/static/facultati/UPB/inginerie_in_limbi_straine.png")
write_image(17, "A:/FACULTATE/LICENTA/static/facultati/UPB/stiinte_aplicate.png")
write_image(18, "A:/FACULTATE/LICENTA/static/facultati/UPB/inginerie_medicala_upb.png")
write_image(19, "A:/FACULTATE/LICENTA/static/facultati/UPB/facultatea_FAIMA.png")
write_image(20, "A:/FACULTATE/LICENTA/static/facultati/ASE/administrarea_afacerilor.png")
write_image(21, "A:/FACULTATE/LICENTA/static/facultati/ASE/administrarea_afacerilor.png")
write_image(22, "A:/FACULTATE/LICENTA/static/facultati/ASE/administratie_si_management_public.png")
write_image(23, "A:/FACULTATE/LICENTA/static/facultati/ASE/administratie_si_management_public.png")
write_image(24, "A:/FACULTATE/LICENTA/static/facultati/ASE/business_si_turism.png")
write_image(25, "A:/FACULTATE/LICENTA/static/facultati/ASE/CSIE.png")
write_image(26, "A:/FACULTATE/LICENTA/static/facultati/ASE/CSIE.png")
write_image(27, "A:/FACULTATE/LICENTA/static/facultati/ASE/CSIE.png")
write_image(28, "A:/FACULTATE/LICENTA/static/facultati/ASE/CSIE.png")
write_image(29, "A:/FACULTATE/LICENTA/static/facultati/ASE/CSIE.png")
write_image(30, "A:/FACULTATE/LICENTA/static/facultati/ASE/CSIE.png")
write_image(31, "A:/FACULTATE/LICENTA/static/facultati/ASE/CSIE.png")
write_image(32, "A:/FACULTATE/LICENTA/static/facultati/ASE/CSIE.png")
write_image(33, "A:/FACULTATE/LICENTA/static/facultati/ASE/contabilitate_informatica.png")
write_image(34, "A:/FACULTATE/LICENTA/static/facultati/ASE/contabilitate_informatica.png")
write_image(35, "A:/FACULTATE/LICENTA/static/facultati/ASE/drept_ASE.png")
write_image(36, "A:/FACULTATE/LICENTA/static/facultati/ASE/drept_ASE.png")
write_image(37, "A:/FACULTATE/LICENTA/static/facultati/ASE/economie_teoretica_si_aplicata.png")
write_image(38, "A:/FACULTATE/LICENTA/static/facultati/ASE/economie_teoretica_si_aplicata.png")
write_image(39, "A:/FACULTATE/LICENTA/static/facultati/ASE/economie_agroalimentara.png")
write_image(40, "A:/FACULTATE/LICENTA/static/facultati/ASE/economie_agroalimentara.png")
write_image(41, "A:/FACULTATE/LICENTA/static/facultati/ASE/finante_asigurari.png")
write_image(42, "A:/FACULTATE/LICENTA/static/facultati/ASE/finante_asigurari.png")
write_image(43, "A:/FACULTATE/LICENTA/static/facultati/ASE/finante_asigurari.png")
write_image(44, "A:/FACULTATE/LICENTA/static/facultati/ASE/finante_asigurari.png")
write_image(45, "A:/FACULTATE/LICENTA/static/facultati/ASE/management.png")
write_image(46, "A:/FACULTATE/LICENTA/static/facultati/ASE/management.png")
write_image(47, "A:/FACULTATE/LICENTA/static/facultati/ASE/management.png")
write_image(48, "A:/FACULTATE/LICENTA/static/facultati/ASE/management.png")
write_image(49, "A:/FACULTATE/LICENTA/static/facultati/ASE/marketing.png")
write_image(50, "A:/FACULTATE/LICENTA/static/facultati/ASE/marketing.png")
write_image(51, "A:/FACULTATE/LICENTA/static/facultati/ASE/marketing.png")
write_image(52, "A:/FACULTATE/LICENTA/static/facultati/ASE/marketing.png")
write_image(53, "A:/FACULTATE/LICENTA/static/facultati/ASE/relatii_economice.png")
write_image(54, "A:/FACULTATE/LICENTA/static/facultati/ASE/relatii_economice.png")
write_image(55, "A:/FACULTATE/LICENTA/static/facultati/ASE/relatii_economice.png")
write_image(56, "A:/FACULTATE/LICENTA/static/facultati/ASE/relatii_economice.png")
write_image(57, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(58, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(59, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(60, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(61, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(62, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(63, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(64, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(65, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(66, "A:/FACULTATE/LICENTA/static/facultati/UMFCD/medicina.png")
write_image(67, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/Administratie-si-Afaceri.png")
write_image(68, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/Administratie-si-Afaceri.png")
write_image(69, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/biologie_unibuc.png")
write_image(70, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/biologie_unibuc.png")
write_image(71, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/chimie.png")
write_image(72, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/chimie.png")
write_image(73, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/drept_unibuc.png")
write_image(74, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/filosofie.png")
write_image(75, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/filosofie.png")
write_image(76, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/fizica.png")
write_image(77, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/geografie.png")
write_image(78, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/geografie.png")
write_image(79, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/geologie_si_geofizica.png")
write_image(80, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/geologie_si_geofizica.png")
write_image(81, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/geologie_si_geofizica.png")
write_image(82, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/geologie_si_geofizica.png")
write_image(83, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/geologie_si_geofizica.png")
write_image(84, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/geologie_si_geofizica.png")
write_image(85, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/istorie.png")
write_image(86, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/jurnalism.png")
write_image(87, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/limbi_straine.png")
write_image(88, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/limbi_straine.png")
write_image(89, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/litere.png")
write_image(90, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/litere.png")
write_image(91, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/fmi.png")
write_image(92, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/fmi.png")
write_image(93, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/fmi.png")
write_image(94, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/fmi.png")
write_image(95, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/fmi.png")
write_image(96, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/fmi.png")
write_image(97, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/psihologie.png")
write_image(98, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/asistenta_sociala.png")
write_image(99, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/asistenta_sociala.png")
write_image(100, "A:/FACULTATE/LICENTA/static/facultati/UNIBUC/stiinte_politice.png")
write_image(101, "A:/FACULTATE/LICENTA/static/facultati/IASI/biologie.png")
write_image(102, "A:/FACULTATE/LICENTA/static/facultati/IASI/biologie.png")
write_image(103, "A:/FACULTATE/LICENTA/static/facultati/IASI/chimie.png")
write_image(104, "A:/FACULTATE/LICENTA/static/facultati/IASI/chimie.png")
write_image(105, "A:/FACULTATE/LICENTA/static/facultati/IASI/drept.png")
write_image(106, "A:/FACULTATE/LICENTA/static/facultati/IASI/drept.png")
write_image(107, "A:/FACULTATE/LICENTA/static/facultati/IASI/economie_si_administrarea_afacerilor.png")
write_image(108, "A:/FACULTATE/LICENTA/static/facultati/IASI/economie_si_administrarea_afacerilor.png")
write_image(109, "A:/FACULTATE/LICENTA/static/facultati/IASI/sport.png")
write_image(110, "A:/FACULTATE/LICENTA/static/facultati/IASI/sport.png")
write_image(111, "A:/FACULTATE/LICENTA/static/facultati/IASI/sport.png")
write_image(112, "A:/FACULTATE/LICENTA/static/facultati/IASI/sport.png")
write_image(113, "A:/FACULTATE/LICENTA/static/facultati/IASI/filosofie.png")
write_image(114, "A:/FACULTATE/LICENTA/static/facultati/IASI/filosofie.png")
write_image(115, "A:/FACULTATE/LICENTA/static/facultati/IASI/filosofie.png")
write_image(116, "A:/FACULTATE/LICENTA/static/facultati/IASI/filosofie.png")
write_image(117, "A:/FACULTATE/LICENTA/static/facultati/IASI/fizica.png")
write_image(118, "A:/FACULTATE/LICENTA/static/facultati/IASI/fizica.png")
write_image(119, "A:/FACULTATE/LICENTA/static/facultati/IASI/fizica.png")
write_image(120, "A:/FACULTATE/LICENTA/static/facultati/IASI/geografie.png")
write_image(121, "A:/FACULTATE/LICENTA/static/facultati/IASI/informatica.png")
write_image(122, "A:/FACULTATE/LICENTA/static/facultati/IASI/informatica.png")
write_image(123, "A:/FACULTATE/LICENTA/static/facultati/IASI/informatica.png")
write_image(124, "A:/FACULTATE/LICENTA/static/facultati/IASI/informatica.png")
write_image(125, "A:/FACULTATE/LICENTA/static/facultati/IASI/Istorie.png")
write_image(126, "A:/FACULTATE/LICENTA/static/facultati/IASI/Istorie.png")
write_image(127, "A:/FACULTATE/LICENTA/static/facultati/IASI/litere.png")
write_image(128, "A:/FACULTATE/LICENTA/static/facultati/IASI/litere.png")
write_image(129, "A:/FACULTATE/LICENTA/static/facultati/IASI/matematica.png")
write_image(130, "A:/FACULTATE/LICENTA/static/facultati/IASI/matematica.png")
write_image(131, "A:/FACULTATE/LICENTA/static/facultati/IASI/matematica.png")
write_image(132, "A:/FACULTATE/LICENTA/static/facultati/IASI/matematica.png")
write_image(133, "A:/FACULTATE/LICENTA/static/facultati/IASI/psihologie.png")
write_image(134, "A:/FACULTATE/LICENTA/static/facultati/IASI/psihologie.png")
write_image(135, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/info_matematica.png")
write_image(136, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/info_matematica.png")
write_image(137, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/fizica.png")
write_image(138, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/chimie.png")
write_image(139, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/biologie.png")
write_image(140, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/geografie.png")
write_image(141, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/stiinta_si_ingineria_mediului.png")
write_image(142, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/stiinta_si_ingineria_mediului.png")
write_image(143, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/drept.png")
write_image(144, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/drept.png")
write_image(145, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/litere.png")
write_image(146, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/litere.png")
write_image(147, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/istorie.png")
write_image(148, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/istorie.png")
write_image(149, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/sociologie.png")
write_image(150, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/sociologie.png")
write_image(151, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/psihologie.png")
write_image(152, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/psihologie.png")
write_image(153, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/stiinte_economice.png")
write_image(154, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/stiinte_economice.png")
write_image(155, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/studii_europene.png")
write_image(156, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/studii_europene.png")
write_image(157, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/business.png")
write_image(158, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/business.png")
write_image(159, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/stiinte_politice.png")
write_image(160, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/stiinte_politice.png")
write_image(161, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/sport.png")
write_image(162, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/teatru.png")
write_image(163, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/teatru.png")
write_image(164, "A:/FACULTATE/LICENTA/static/facultati/CLUJ_UBB/inginerie.png")

write_image(165, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/inginerie_electrica.png")
write_image(166, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/inginerie_electrica.png")
write_image(167, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/inginerie_mecanica.png")
write_image(168, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/inginerie_mecanica.png")
write_image(169, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/inginerie_tehnologica.png")
write_image(170, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/inginerie_tehnologica.png")
write_image(171, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/stiinta_si_ingineria_materialelor.png")
write_image(172, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/stiinta_si_ingineria_materialelor.png")
write_image(173, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/drept.png")
write_image(174, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/drept.png")
write_image(175, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/litere.png")
write_image(176, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/litere.png")
write_image(177, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/matematica_informatica.png")
write_image(178, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/matematica_informatica.png")
write_image(179, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/medicina.png")
write_image(180, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/medicina.png")
write_image(181, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/muzica.png")
write_image(182, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/muzica.png")
write_image(183, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/psihologie.png")
write_image(184, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/psihologie.png")
write_image(185, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/sociologie.png")
write_image(186, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/sociologie.png")
write_image(187, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/stiinte_economice.png")
write_image(188, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/stiinte_economice.png")
write_image(189, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/turism.png")
write_image(190, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/turism.png")
write_image(191, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/constructii.png")
write_image(192, "A:/FACULTATE/LICENTA/static/facultati/UNITBV_BRASOV/constructii.png")

write_image(193, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/chimie_bio_geo.png")
write_image(194, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/chimie_bio_geo.png")
write_image(195, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/chimie_bio_geo.png")
write_image(196, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/chimie_bio_geo.png")
write_image(197, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/drept.png")
write_image(198, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/drept.png")
write_image(199, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/feaa.png")
write_image(200, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/feaa.png")
write_image(201, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/fizica.png")
write_image(202, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/fizica.png")
write_image(203, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/litere.png")
write_image(204, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/litere.png")
write_image(205, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/fmi.png")
write_image(206, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/fmi.png")
write_image(207, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/teatru_muzica.png")
write_image(208, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/teatru_muzica.png")
write_image(209, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/sociologie_psiho.png")
write_image(210, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/sociologie_psiho.png")
write_image(211, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/stiinte_politice.png")
write_image(212, "A:/FACULTATE/LICENTA/static/facultati/UVT-TIMISOARA/stiinte_politice.png")


write_image(213, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/agronomie.png")
write_image(214, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/agronomie.png")
write_image(215, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/automatica.png")
write_image(216, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/automatica.png")
write_image(217, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/drept.png")
write_image(218, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/drept.png")
write_image(219, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/feaa.png")
write_image(220, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/feaa.png")
write_image(221, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/sport.png")
write_image(222, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/sport.png")
write_image(223, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/inginerie_electrica.png")
write_image(224, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/inginerie_electrica.png")
write_image(225, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/litere.png")
write_image(226, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/litere.png")
write_image(227, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/mecanica.png")
write_image(228, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/mecanica.png")
write_image(229, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/stiinte.png")
write_image(230, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/stiinte.png")
write_image(231, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/stiinte_sociale.png")
write_image(232, "A:/FACULTATE/LICENTA/static/facultati/CRAIOVA/stiinte_sociale.png")

