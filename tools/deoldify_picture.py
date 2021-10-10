#usage <input> <render_factor> <output>
import sys
import os
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

result_path = colorizer.plot_transformed_image(path=sys.argv[1], render_factor=render_factor, compare=True)

res=""
if len(sys.argv)<=3:
	split_file=split_last=os.path.splitext(sys.argv[1])
	res=split_file[0]+"_out_rf"+sys.argv[2]+split_file[1]
else:
	res=sys.argv[3]

print(str(result_path)+" -> "+res)

shutil.move(result_path, res)
