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

res=""
if len(sys.argv)<=3:
	split_file=split_last=os.path.splitext(sys.argv[1])
	res=split_file[0]+"_out_rf"+sys.argv[2]+split_file[1]
else:
	res=sys.argv[3]

result = None

try:
	# result = colorizer.plot_transformed_image(path=sys.argv[1], render_factor=render_factor, compare=True)
	result=colorizer.get_transformed_image(sys.argv[1], render_factor=render_factor, post_process=True, watermarked=False)
except:
	convertToJPG(input_path)
	result=colorizer.get_transformed_image(sys.argv[1], render_factor=render_factor, post_process=True, watermarked=False)
finally:
	if result is not None:
		result.save(res, quality=95)
		result.close()

print(sys.argv[1]+" -> "+res)
