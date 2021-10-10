#usage <input> <render_factor> <output>
import sys
import os
import shutil

from deoldify import device
from deoldify.device_id import DeviceId
#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.CPU)

from deoldify.visualize import *
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
	print(curfile)
	result_path = colorizer.plot_transformed_image(curfile, render_factor=render_factor, compare=True)
	# plt.clf()
	plt.close('all')
	
	outfile=os.path.join(out_directory, filename)
	shutil.move(result_path, outfile)
	print("Done "+outfile)
