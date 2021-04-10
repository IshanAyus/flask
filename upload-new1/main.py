import os
import shutil

from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__)

#image_names = os.listdir('./images')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")
@app.route("/single")
def single():
	#target = shutil.rmtree('images')
	image_names = os.listdir('./images')
	if len(image_names)== 0:
		return render_template("single.html")
	elif len(image_names)!= 0:
		print( "single image accepted ")
		return render_template("sing_msg.html") 


@app.route("/upsingle", methods=["POST"])
def upsingle():
    image_names = os.listdir('./images')
    print(len(image_names))
    if len(image_names)!= 0:
    	return render_template("sing_msg.html")
    else:
    	target = os.path.join(APP_ROOT, 'images/')
    	print(target)
    	if not os.path.isdir(target):
            	os.mkdir(target)
    	else:
        	print("Couldn't create upload directory: {}".format(target))
    	for upload in request.files.getlist("file"):
        	filename = upload.filename
        	destination = "/".join([target, filename])
        	upload.save(destination)

    	return render_template("complete.html", image_name=filename)
    


@app.route('/upsingle/<filename>')
def send_imag(filename):
    return send_from_directory("images", filename)


    
@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    
    return render_template("complete.html", image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

@app.route("/delete")
def delete():
    target = shutil.rmtree('images')
    print('deleted yo')
    return render_template("delete.html")

            

if __name__ == "__main__":
    app.run(debug=True)

