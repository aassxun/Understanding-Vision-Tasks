Our paper ''The Key of Understanding Vision Tasks: Explanatory Instructions'' is available at xxx.

Dataset and code will be available in two months.

### Samples for Zero-shot Capabilities on Vision Tasks (Relatively Simple Samples)

#### Instruction-level Zero-shot Samples (Depth Estimation)

| **Input Image** | **Unseen Explanatory Instruction** | **Output Image** | **Ground Truth** |
|:---------------------:|:----------------------------:|:---------------------:|:----------------------:|
| <img src="assets/rgb_00015.jpg" alt="Input Image 1-1" width="133" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Acknowledge the spatial structure and identify variations in light intensity, translating these into a gradient scale representing distances. Accentuate regions where light diminishes gradually, enhancing the perception of depth by dimming peripheral areas. Adjust the distribution of luminance to highlight the central vanishing point, converting detailed textures into smooth transitions of grayscale.` | <img src="assets/depth_output_15.jpg" alt="Output Image" width="133" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/depth_gt_15.png" alt="Ground Truth" width="133" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/rgb_00018.jpg" alt="Input Image 1-2" width="133" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Start by analyzing the spatial layout to identify key structural elements. Gradually obscure less relevant details in the periphery to focus primarily on central depth. Increase contrast between light and dark areas to enhance perception of distance. Transition the textures into smooth gradients to reflect variations in depth, with a focus on enhanced luminosity for regions that are further away.` | <img src="assets/depth_output_18.jpg" alt="Output Image" width="133" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/depth_gt_18.png" alt="Ground Truth" width="133" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/rgb_00021.jpg" alt="Input Image 1-3" width="133" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Convert each region’s color intensity to a grayscale value corresponding to its relative distance from the viewer, with nearer objects appearing lighter and those farther away darker. Gradually smooth transitions between these regions to reflect continuous depth variation. Remove textural details that do not affect perceived depth to create uniformity based on object proximity. Adjust overall brightness to highlight the spatial configuration without explicit texture representation.` | <img src="assets/depth_output_21.jpg" alt="Output Image" width="133" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/depth_gt_21.png" alt="Ground Truth" width="133" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |

---

#### Instruction-level Zero-shot Samples (Surface Normal Estimation).

| **Input Image** | **Unseen Explanatory Instruction** | **Output Image** | **Ground Truth** |
|:---------------------:|:----------------------------:|:---------------------:|:----------------------:|
| <img src="assets/rgb_00015.jpg" alt="Input Image 1-1" width="133" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Translate the visible structures into a range of bright colors reflecting orientation angles, enhancing variations across surfaces.` | <img src="assets/surface_output_15.jpg" alt="Output Image" width="133" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/surface_gt_15.jpg" alt="Ground Truth" width="133" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/rgb_00018.jpg" alt="Input Image 1-2" width="133" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Convert visual elements into a spectrum of colors that represent the directionality of surfaces, capturing the angles and orientations vividly.` | <img src="assets/surface_output_18.jpg" alt="Output Image" width="133" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/surface_gt_18.jpg" alt="Ground Truth" width="133" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/rgb_00021.jpg" alt="Input Image 1-3" width="133" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Translate the scene into a colorful array to indicate surface orientations and angles.` | <img src="assets/surface_output_21.jpg" alt="Output Image" width="133" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/surface_gt_21.jpg" alt="Ground Truth" width="133" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |

---

#### Instruction-level Zero-shot Samples (HED Boundary Detection).
| **Input Image** | **Unseen Explanatory Instruction** | **Output Image** | **Ground Truth** |
|:---------------------:|:----------------------------:|:---------------------:|:----------------------:|
| <img src="assets/hed_input_6.png" alt="Input Image 1-1" width="100" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Capture the outline and prominent edges of the cylindrical object and its surroundings, simplify everything by removing textures and detailed surfaces, and emphasize only the contours and distinct features while rendering a higher contrast between light and dark regions with sharp shifts in tones.` | <img src="assets/hed_output_6.png" alt="Output Image" width="100" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/hed_gt_6.png" alt="Ground Truth" width="100" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/hed_input_10.jpg" alt="Input Image 1-2" width="100" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `The vibrant scene with multiple colors and details could be simplified into a monochrome representation. First, focus on defining the high-contrast areas between light and dark in a much starker, black-and-white way. Then, it's important to emphasize contours and significant edges, such as the lines around the face, the dress’ folds, and the furniture's details, while downplaying softer gradients. Removing extraneous colors and textures leaves behind only the essential structural features that provide a more abstract, but recognizable silhouette and objects.` | <img src="assets/hed_output_10.png" alt="Output Image" width="100" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/hed_gt_10.png" alt="Ground Truth" width="100" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/hed_input_14.jpg" alt="Input Image 1-3" width="100" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Begin by eliminating most of the intricate details and colors, transforming the vibrant elements into simplified outlines. Keep only the borders and defined structures, ensuring that the environment and figure take on an abstract form. Remove all texture, reducing the entire composition to minimal contrasting edges that define the shapes more than the details.` | <img src="assets/hed_output_14.png" alt="Output Image" width="100" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/hed_gt_14.png" alt="Ground Truth" width="100" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |

---

#### Instruction-level Zero-shot Samples (Dehazing).
| **Input Image** | **Unseen Explanatory Instruction** | **Output Image** | **Ground Truth** |
|:---------------------:|:----------------------------:|:---------------------:|:----------------------:|
| <img src="assets/0016_0.8_0.08.jpg" alt="Input Image 1-1" width="100" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Gradually reduce atmospheric interference, allowing clearer visibility of buildings and sharpening the outlines. Enhance clarity and brightness to bring out the details within the cityscape, providing a crisper view.` | <img src="assets/0016_output.jpg" alt="Output Image" width="100" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/0016_gt.jpg" alt="Ground Truth" width="100" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/0017_0.9_0.08.jpg" alt="Input Image 1-2" width="100" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Increasing the clarity by reducing haze, enhancing contrast, and deepening colors to give a sharper and more vibrant appearance to the scene.` | <img src="assets/0017_output.jpg" alt="Output Image" width="100" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/0017_gt.jpg" alt="Ground Truth" width="100" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/0018_0.9_0.2.jpg" alt="Input Image 1-3" width="100" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `To achieve clarity and vibrancy, adjust the brightness and reduce the foggy effect. Enhance the sharpness of the trees and structures, allowing their details to stand out against the clear blue sky.` | <img src="assets/0018_output.jpg" alt="Output Image" width="100" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/0018_gt.jpg" alt="Ground Truth" width="100" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |

---

#### Instruction-level Zero-shot Samples (Deraining).
| **Input Image** | **Unseen Explanatory Instruction** | **Output Image** | **Ground Truth** |
|:---------------------:|:----------------------------:|:---------------------:|:----------------------:|
| <img src="assets/norain-5x2.jpg" alt="Input Image 1-1" width="100" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Imagine a scenario where rainfall suddenly stops and the water settles, clearing up the scene to enhance visibility and eliminate rain streaks.` | <img src="assets/deraining_output_5.jpg" alt="Output Image" width="100" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/deraining_gt_5.jpg" alt="Ground Truth" width="100" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/norain-6x2.jpg" alt="Input Image 1-2" width="100" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Remove the raindrops and streaks, focusing on enhancing clarity and brightness to achieve a crisp and rain-free appearance in the environment.` | <img src="assets/deraining_output_6.jpg" alt="Output Image" width="100" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/deraining_gt_6.jpg" alt="Ground Truth" width="100" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/norain-9x2.jpg" alt="Input Image 1-3" width="100" height="100"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Imagine the rainfall gradually lessening until the sky clears completely, leaving only the vibrant greenery and the birds in focus.` | <img src="assets/deraining_output_9.jpg" alt="Output Image" width="100" height="100"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/deraining_gt_9.jpg" alt="Ground Truth" width="100" height="100"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |

---

#### Instruction-level Zero-shot Samples (Segmentation).
| **Input Image** | **Unseen Explanatory Instruction** | **Output Image** | **Ground Truth** |
|:---------------------:|:----------------------------:|:---------------------:|:----------------------:|
| <img src="assets/seg_input_1.jpg" alt="Input Image 1-1" height="60"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Apply a pink color overlay to bicycles, completely matching their shapes.` | <img src="assets/seg_output_1.jpg" alt="Output Image" height="60"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/seg_gt_1.jpg" alt="Ground Truth" height="60"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/seg_input_2.jpg" alt="Input Image 1-2" height="70"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Apply a solid grey color tint to fully cover one banana instance.Paint over each stove with a powderblue color.` | <img src="assets/seg_output_2.jpg" alt="Output Image" height="70"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/seg_gt_2.jpg" alt="Ground Truth" height="70"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |
| <img src="assets/seg_input_3.jpg" alt="Input Image 1-3" height="120"/> <span style="display:inline;"> <sub>**Input Image**</sub></span> | `Spectral\_r is the reversed version of Spectral, transitioning through red, yellow, green, and blue. Based on the previously defined colors, help me complete the segmentation task below. Color all instances of bucket, toilet using Spectral\_r colors, following their contours precisely.` | <img src="assets/seg_output_3.jpg" alt="Output Image" height="120"/> <span style="display:inline;"> <sub>**Output Image**</sub></span> | <img src="assets/seg_gt_3.jpg" alt="Ground Truth" height="120"/> <span style="display:inline;"> <sub>**Ground Truth**</sub></span> |

---

### Samples for Zero-shot Capabilities on Vision Tasks (Relatively Hard Samples)
#### Task-level & Instruction-level Zero-shot Samples (Canny-to-Image)
<div align="center">
  <img src="assets/canny_edge_source_1.png" width="18%" style="display: inline-block; margin-right: 2%;">
  <img src="assets/zero_shot_canny_edge_source_1_out_1.jpg" width="18%" style="display: inline-block; margin-right: 2%;">
  <img src="assets/zero_shot_canny_edge_source_1_out_2.jpg" width="18%" style="display: inline-block; margin-right: 2%;">
  <img src="assets/zero_shot_canny_edge_source_1_out_3.jpg" width="18%" style="display: inline-block; margin-right: 2%;">
  <img src="assets/zero_shot_canny_edge_source_1_out_4.jpg" width="18%" style="display: inline-block;">
</div>
<p style="text-align: left; font-size: 14px;">
  <b>Explanatory Instruction:</b> 
  <code style="font-size: 14px;">"Fill in all the empty outlines with rich colors that reflect vibrant tones, while redefining the shapes with smooth textures. Add layers of depth to the flat contours by enhancing brightness gradients in the sky, shadowing in the mountains, and intricate shades among the flowers.  Reintroduce the sensation of open space and dimension by contrasting sharp objects with muted backgrounds and crisp details in the foreground."</code>
  <b>Resolution:</b> 
  <i>448×448.</i> 
</p>

#### Instruction-level Zero-shot Samples (Deraining)
<div align="center">
  <img src="assets/deraining_input.jpg" width="18%" height="120px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/deraining_output_1.jpg" width="18%" height="120px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/deraining_output_2.jpg" width="18%" height="120px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/deraining_output_3.jpg" width="18%" height="120px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/deraining_output_4.jpg" width="18%" height="120px" style="display: inline-block;">
</div>
<p style="text-align: left; font-size: 14px;">
  <b>Explanatory Instruction:</b> 
  <code style="font-size: 14px;">"Slowly remove the rain falling from the sky in the image, still maintain the state of night, and the girl on the bridge is also still holding the umbrella, but readjust the light in the distance."</code>
  <b>Limitations:</b> 
  <span style="font-size: 14px;">The model struggles to preserve smaller objects and environmental details.</span>
  <b>Resolution:</b> 
  <i>448×448.</i> 
</p>

#### Task-level & Instruction-level Zero-shot Samples (Low-light Enhancement)
<div align="center">
  <img src="assets/zs_low_light_input.jpg" width="18%" height="120px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/zs_low_light_1.jpg" width="18%" height="120px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/zs_low_light_2.jpg" width="18%" height="120px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/zs_low_light_3.jpg" width="18%" height="120px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/zs_low_light_4.jpg" width="18%" height="120px" style="display: inline-block;">
</div>
<p style="text-align: left; font-size: 14px;">
  <b>Explanatory Instruction:</b> 
  <code style="font-size: 14px;">"Increase the overall brightness to reveal details in dark areas while preserving highlights. Adjust the contrast to enhance the brightness differences between regions, making the structures and textures more distinct. Optimize color saturation to make previously dull colors more vibrant, such as the blue on the floor becoming more prominent. Apply denoising to reduce noise commonly found in low-light images, improving the overall quality. Ensure the final image appears natural while retaining the authentic style of the scene."</code>
  <b>Limitations:</b> 
  <span style="font-size: 14px;">Controlling the intensity of lighting enhancement through language instructions is challenging, often resulting in significant deviations in the output.</span>
  <b>Resolution:</b> 
  <i>448×448.</i> 
</p>

#### Instruction-level Zero-shot Samples (Desnowing)
<div align="center">
  <img src="assets/desnow_input.jpg" width="18%" height="328px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/desnow_output_1.jpg" width="18%" height="328px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/desnow_output_2.jpg" width="18%" height="328px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/desnow_output_3.jpg" width="18%" height="328px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/desnow_output_4.jpg" width="18%" height="328px" style="display: inline-block;">
</div>
<p style="text-align: left; font-size: 14px;">
  <b>Explanatory Instruction:</b> 
  <code style="font-size: 14px;">"Remove the falling snow from the sky in the image, keep the other objects and snow in the image, still keep it dark, but pay attention to the adjustment of light behind the tree."</code>
  <b>Limitations:</b> 
  <span style="font-size: 14px;">The second generated image struggles to retain nighttime details, while the third and fourth images exhibit poor performance in removing snow from the sky. Additionally, attempting to remove snow from the ground simultaneously can result in significant distortions.</span>
  <b>Resolution:</b> 
  <i>448×448.</i> 
</p>

#### Task-level & Instruction-level Zero-shot Samples (Deblurring)
<div align="center">
  <img src="assets/deblur_input.jpg" width="18%" height="240px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/deblur_output_1.jpg" width="18%" height="240px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/deblur_output_2.jpg" width="18%" height="240px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/deblur_output_3.jpg" width="18%" height="240px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/deblur_output_4.jpg" width="18%" height="240px" style="display: inline-block;">
</div>
<p style="text-align: left; font-size: 14px;">
  <b>Explanatory Instruction:</b> 
  <code style="font-size: 14px;">"The image shows noticeable multiple visual overlaps of trees and buildings. I would like to remove visual overlaps and restore a clear, sharp image without blurring. Do not alter the main content and pay attention to adjusting the light."</code>
  <b>Limitations:</b> 
  <span style="font-size: 14px;">The success rate of guiding the model's task-level zero-shot capability through language instructions is relatively low.</span>
  <b>Resolution:</b> 
  <i>448×448.</i> 
</p>

#### Instruction-level Zero-shot Samples (Dehazing)
<div align="center">
  <img src="assets/dehazing_input.jpg" width="18%" height="137px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/dehazing_output_1.jpg" width="18%" height="137px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/dehazing_output_1.jpg" width="18%" height="137px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/dehazing_output_1.jpg" width="18%" height="137px" style="display: inline-block; margin-right: 2%;">
  <img src="assets/dehazing_output_1.jpg" width="18%" height="137px" style="display: inline-block;">
</div>
<p style="text-align: left; font-size: 14px;">
  <b>Explanatory Instruction:</b> 
  <code style="font-size: 14px;">"Retain the distant clouds in the image while removing as much fog as possible. Attempt to restore the faintly visible sun in the distance, but ensure there is no strong sunlight. Focus on recovering the mountains and the nearby trees as much as possible."</code>
  <b>Limitations:</b> 
  <span style="font-size: 14px;">It will cause distortions in certain objects.</span>
  <b>Resolution:</b> 
  <i>448×448.</i> 
</p>
