from reportlab.pdfgen import canvas 
c=canvas.Canvas("myresume.pdf",pagesize=(595,841))
#name 
c.setFont ("Helvetica",30)
c.drawString(20,650,"Ashis Kumar Ray ")
#contact inforamtion
c.setFont ("Helvetica",25)
c.drawString(5,580,"contact info.")
c.drawString(20,540,"Email:")
c.setFont ("Helvetica",15)
c.drawString(10,520,"ashisray.057@gmail.com")
# address
c.setFont ("Helvetica",25)
c.drawString(10,480,"Address")
c.setFont ("Helvetica",15)
c.drawString(10,450,"new delhi, (Inida)")
# education 
c.setFont ("Helvetica",25)
c.drawString(260,700,"Education")
c.setFont ("Helvetica",15)
c.drawString(260,680,"Persuing B.C.A (bachlors of computer application)")
#skills 
c.setFont ("Helvetica",25)
c.drawString(260,640,"Skills")
c.setFont ("Helvetica",20)
c.drawString(260,610,"Programming: ")
c.setFont ("Helvetica",15)
c.drawString(260,580,"data automaton with (python)")
c.drawString(260,560,"automation in ....")
c.drawString(260,540,"excel, pdf, emails, browser,api, file/folder,")
c.drawString(260,520, "csv, image, GUI, report, etc....")
c.drawString(260,500,"cybersecurity with (python)")
c.drawString(260,480,"(python),(c),(c++)")
#ssoft skills
c.setFont ("Helvetica",25)
c.drawString(260,440,"Soft Skills")
c.setFont ("Helvetica",15)
c.drawString(260,420,"Good co,,unication skills")
c.drawString(260,400,"leadership quality")
c.drawString(260,380,"Teamwork, problem solving")
c.drawString(260,360, "Time management,Adaptiblity")
c.drawString(260,340,"creative")
# adding image 
image_Path=r"C:\Users\ashis\OneDrive\Documents\my photo.jpg"
image_x=100
image_y=680
image_width=100
image_height=100
c.drawImage(image_Path,image_x,image_y,width=image_width,height=image_height)

# adding line 
line_x= image_x + image_width + 55
c.line(line_x,20,line_x,800)
c.save ()
print ("pdf generated successfully :")