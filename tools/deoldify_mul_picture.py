#usage <input> <render_factor> <output>
#run from the deoldify directory
import sys
import os

#allow modules to be imported
sys.path.append(".")

import shutil

from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *

#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.CPU)

print("Started "+sys.argv[1])

plt.style.use('dark_background')
#torch.backends.cudnn.benchmark=False
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

colorizer = get_image_colorizer(artistic=True)

#NOTE:  Max is 45 with 11GB video cards. 35 is a good default
render_factor=int(sys.argv[2])
#NOTE:  Make source_url None to just read from file at ./video/source/[file_name] directly without modification
result_path = None

in_directory=sys.argv[1]
out_directory=sys.argv[3]

if not os.path.exists(out_directory):
	os.makedirs(out_directory)

for filename in os.listdir(in_directory):
	curfile=os.path.join(in_directory, filename)
	outfile=os.path.join(out_directory, filename)
	# result_path = colorizer.plot_transformed_image(curfile, render_factor=render_factor, compare=True)
	try:
		result=colorizer.get_transformed_image(curfile, render_factor=render_factor, post_process=True, watermarked=False)
	except:
		convertToJPG(input_path)
		result=colorizer.get_transformed_image(curfile, render_factor=render_factor, post_process=True, watermarked=False)
	finally:
		if result is not None:
			result.save(outfile, quality=95)
			result.close()
	# plt.clf()
	# plt.close('all')
	
	print(curfile+" -> "+outfile)
	
	# shutil.move(result_path, outfile)
	# print("Done "+outfile)
