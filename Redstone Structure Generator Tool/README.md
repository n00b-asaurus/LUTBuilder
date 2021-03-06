# Redstone Structure Generator
A tool used to procedurally generate redstone circuits. 

## Application
Used to quickly and easily generage redstone structures for fast developement and testing of complex redstone circuits.
The generation method currently supported is typing commands directly into the games chat.

The type of structures this tool can generate is infinately configurable, and each structure can request arguments needed specifically for its own generation.
The structures currently supported are the basic encoder, the properinglish19 decoder, and the stenodyon decoder.


## Making and Understanding Encoder Files
With the following table saved as encoder.txt
* 000101001
* 010010100
* 011101001
* 110101011
* 001111001

We can produce an encoder with 5 active low inputs and 9 active high output.
Every line in encoder.txt is 1 input on the decoder, and every column of bits 1 output.
A 1 in any position means that output will be active when that input is active. Otherwise, that output is inactive.
The width of the encoder is determined by the number of bits in each line. It is important that all lines have the same number of bits.
The length of the encoder is determined by the number of lines in the file.
As far as physical positions are concerned, the output bits on the encoder will appear as they do in encoder.txt.
I.e. the left-most bits in encoder.txt will appear on the lefthand side of the encoder.
The top line (first input) of the encoder will appear in front, with every subsequent input appearing further back.


## Making and Understanding Decoder Files
With the following table saved as decoder.txt
* 00X10X001
* X100X01XX
* 0XX101X01
* 11X101011
* XXX111X01

We can produce a decoder with 9 active high inputs and 5 active low outputs.
Every column of bits is 1 input, and every line of bits is 1 output.
A 1 in any position means that output is active only if that input is active.
A 0 in any position means that output is active only if that input is inactive.
An X in any position means that the outputs state is not dependant in that inputs state.
All inputs must match the outputs required state in order for that output to be active, otherwise it's inactive.
E.g. an output looking for a 101X1 must have inputs 1, 3, and 5 active, and input 2 inactive in order for that output to be active.
The state of input 4 does not affect that output.
The width of the decoder is determined by the number of bits in each line. It is important that all lines have the same number of bits.
The length of the decoder is determined by the number of lines in the file.
With physical locations, like the encoder, the bits on the lefthand side in the file will appear on the lefthand side on the circuit.
The top line (first output) of the decoder will appear in front, with every subsequent output appearing further back.


## Usage

Double click `Redstone Structure Generator` and a command terminal will open.

The terminal will then ask you to provide various arguments, which are as follows:

#### structure
Selects what kind of structure to generate.

Current structures include:
* basic_encoder - generates a basic horizontal encoder
* properinglish19_decoder - generates a compact decoder, generation is kinda slow.
* stenodyon_decoder - generates a slightly less compact decoder, generation works much faster

Further arguments depend entirely on the type of structure selected. Scroll down to the appropriate structures arguments list for more information.

### starting the generation process
Once you've entered all your arguments, the program will get to work compiling all the commands needed to be run to generate that structure.
It will prompt you when it's done with the following message:

`Structure ready, press Enter to begin building...`

BEFORE PRESSING ENTER make sure you have your game running, and you are standing in position. Remember the structure is built relative to your position, and you cannot stop it once it starts.

Press enter and a count down will begin. You will have 5 seconds to tab into your game, and get out of any pause screens or GUI's you were in.
Once the generator starts, you will see commands being typed into your console, and the structure will slowly start to take shape.
While this happens, it is important that you do not tab out of your game. Doing so will cause the commands to be typed elseware.
Wait for the generator to finish typing, once it's done you can press 'Enter' to exit the console.


## Structure Arguments

### basic_encoder

#### file
The path of the .txt file used to generate the structure. Can be relative or absolute. See Making and Understanding Encoder Files.

#### facing
The structure generated will always generate in front of you, top line closest to you, bottom line furthest away. Encoder outputs will always face you.
In order for this to work correctly, you need to tell the generator what direction you're facing.
Valid inputs are north, south, east, and west. No quotations needed.

#### input_side
For an encoder, the outputs will always face you. However, the inputs can either go on the left side or the right side.
It's important to specify which side your inputs are coming from as this affects the direction of the repeaters.
Use this argument to specify what side the inputs come from. Valid inputs are left, or right. No quotations needed.

#### build_to
The structure is built relative to your position, with you being one corner.
You can either be the left corner, which means the structure builds off to the right, or you can be the right corner, which means the structure builds off to the left.
You can specify which direction the structure builds off to with this argument. Valid inputs are left, or right. No quotations needed.

#### offset
With you're position being one of the corners, it's possible that a block can be placed where you stand and push you out of your position.
This is not ideal. To prevent this, it's a good idea to add an offset to your position.
This offset will shift the entire structure over to that position, so an offset of -4,0,0 will shift the structure back 4 meters on the X axis, while an offset of 0,1,3 will shift the structure up 1 meter on the y axis and over 3 meters on the z axis.
This transformation is applied after all rotations, so the direction you face will not affect these coordinates.

Formatting for the offset argument is 3 whole integers separated by commas, no spaces or quotations.

Examples: 
* -4,1,7 
* 5,0,2 
* 0,1,-3 
* 0,-3,0

### properinglish19_decoder

#### file
The path of the .txt file used to generate the structure. Can be relative or absolute. See Making and Understanding Decoder Files.

#### facing
The structure generated will always generate in front of you, top line closest to you, bottom line furthest away. Decoders inputs will always face you.
In order for this to work correctly, you need to tell the generator what direction you're facing.
Valid inputs are north, south, east, and west. No quotations needed.

#### output_side
For a decoder, the inputs will always face you. But the outputs can go to the left or right.
It's important to specify which side your outputs are going to as this affects the direction of the repeaters.
Use this argument to specify what side the outputs go to. Valid inputs are left, or right. No quotations needed.

#### build_to
The structure is built relative to your position, with you being one corner.
You can either be the left corner, which means the structure builds off to the right, or you can be the right corner, which means the structure builds off to the left.
You can specify which direction the structure builds off to with this argument. Valid inputs are left, or right. No quotations needed.

#### offset
With you're position being one of the corners, it's possible that a block can be placed where you stand and push you out of your position.
This is not ideal. To prevent this, it's a good idea to add an offset to your position.
This offset will shift the entire structure over to that position, so an offset of -4,0,0 will shift the structure back 4 meters on the X axis, while an offset of 0,1,3 will shift the structure up 1 meter on the y axis and over 3 meters on the z axis.
This transformation is applied after all rotations, so the direction you face will not affect these coordinates.

Formatting for the offset argument is 3 whole integers separated by commas, no spaces or quotations.

Examples: 
* -4,1,7 
* 5,0,2 
* 0,1,-3 
* 0,-3,0

### stenodyon_decoder

#### file
The path of the .txt file used to generate the structure. Can be relative or absolute. See Making and Understanding Decoder Files.

#### facing
The structure generated will always generate in front of you, top line closest to you, bottom line furthest away. Decoders inputs will always face you.
In order for this to work correctly, you need to tell the generator what direction you're facing.
Valid inputs are north, south, east, and west. No quotations needed.

#### output_side
For a decoder, the inputs will always face you. But the outputs can go to the left or right.
It's important to specify which side your outputs are going to as this affects the direction of the repeaters.
Use this argument to specify what side the outputs go to. Valid inputs are left, or right. No quotations needed.

#### build_to
The structure is built relative to your position, with you being one corner.
You can either be the left corner, which means the structure builds off to the right, or you can be the right corner, which means the structure builds off to the left.
You can specify which direction the structure builds off to with this argument. Valid inputs are left, or right. No quotations needed.

#### offset
With you're position being one of the corners, it's possible that a block can be placed where you stand and push you out of your position.
This is not ideal. To prevent this, it's a good idea to add an offset to your position.
This offset will shift the entire structure over to that position, so an offset of -4,0,0 will shift the structure back 4 meters on the X axis, while an offset of 0,1,3 will shift the structure up 1 meter on the y axis and over 3 meters on the z axis.
This transformation is applied after all rotations, so the direction you face will not affect these coordinates.

Formatting for the offset argument is 3 whole integers separated by commas, no spaces or quotations.

Examples: 
* -4,1,7 
* 5,0,2 
* 0,1,-3 
* 0,-3,0