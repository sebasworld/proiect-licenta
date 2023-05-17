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
        


write_image(1, "A:/FACULTATE/LICENTA/static/upb-automatica.png")
write_image(2, "A:/FACULTATE/LICENTA/static/upb-automatica.png")
write_image(3, "A:/FACULTATE/LICENTA/static/upb-automatica.png")
write_image(4, "A:/FACULTATE/LICENTA/static/upb-automatica.png")
'''
write_image(2, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_fellowship.png")
write_image(3, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_two_towers.png")
write_image(4, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_return_oftheking.png")

write_image(5, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_godfather.png")
write_image(6, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/alien.png")
write_image(7, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/psycho.png")
write_image(8, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/mirror_game.png")
write_image(9, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/life_is_beautiful.png")
write_image(10, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/forrest_gump.png")
write_image(11, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/your_name.png")
write_image(12, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_lion_king.png")
write_image(13, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/spider_man.png")
write_image(14, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/star_wars_ep5.png")
write_image(15, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/star_wars_ep4.png")
write_image(16, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/schindlers_list.png")
write_image(17, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/rocketry.png")
write_image(18, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/braveheart.png")
write_image(19, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/central_intelligence.png")
write_image(20, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/stuber.png")'''