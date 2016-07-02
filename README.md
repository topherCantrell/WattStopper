Hacking the WattStopper
======

*WARNING: Electrical mains are dangerous. They will KILL you – dead. You MUST disconnect power to your light switch before tampering with it.*

## Saving Power

The Watt Stopper PW-100 is the light switch you have in your office here at Synapse. It uses a passive IR sensor to determine if anyone is in the room. 
If no one is there it turns the lights off thus "stopping" the wasted "watts".

See the product description at the URL below. Click on the "resources" tab to download the installation/user guide for your light switch.

[Watt Stopper Manual](http://www.wattstopper.com/products/sensors/wall-switch-occupancy-and-vacancy-sensors/pw-100.aspx#.U_o08_mwL7J)

The switch is highly configurable through DIP switch settings accessible to the owner. Use a small flathead screwdriver to pry off the 
button to access the switches beneath. The user guide describes all the various modes and settings. If you set the first three switches 
to ON (up) then the switch goes into "service" mode. You have to manually turn the switch on and off just like a regular light switch.

![](https://github.com/topherCantrell/WattStopper/blob/master/Art/photo4.jpg)

## Out of the Box

You can buy the Watt Stopper from Amazon for $35. I bought one to experiment with before hacking into the company's property.

![](https://git.synapse-wireless.com/chris.cantrell/office/blob/master/WattStopper/Art/photo7.jpg)

When you disassemble the switch you'll find two circuit boards. The "high voltage" board (shown on the right) holds the latching 
relay to control the lights. It also includes a 5V power regulator for the processor board (on the left).

The pink cable is a scrap piece of cat-5 cable I used for wire in this project.

## The Processor Board

The Watt Stopper uses the Atmega88 microcontroller (shown below) to read the IR sensor and control the relay. The other side of the 
board contains a small buzzer, the DIP switches, the main push-button, and two LEDs.

![](https://git.synapse-wireless.com/chris.cantrell/office/blob/master/WattStopper/Art/photo3.JPG)

I soldered wires to various contacts on the processor board. These wires expose the switch's functions to a SNAP engine, but the connections to not hinder the Watt Stopper in any way.

### The Button (Blue Wire)

When the main pushbutton is pressed it connects an input pin on the processor to ground. The blue wire in the photo above hooks to the processor's side of the switch. The SNAP engine drives this pin low to press the button.

### Occupancy (Brown Wire)

There is an LED on the front of the switch that blinks to show occupancy detection. The processor lights this LED by driving an input pin low. The brown wire in the photo hooks to the processor's output pin (Pin 7 on the Atmega). The output is normally high. When the brown wire goes low the SNAP node registers the occupancy detection.

### Relay Coils (Green and Green/White Wires)

The relay in the Watt Stopper is a latching relay. The coils only consume power when the latch is moved from one side to the other. The processor controls the coils with two pins on the 12-pin connector. I tapped into these lines with the green and green/white wires.

To turn the light on the processor momentarily drives green/white high and green low. To turn the light off the processor momentarily drives green/white low and green high. The SNAP node watches these two lines to detect when the lights are turned on and off.

### Common Ground (Orange/White Wire)

The orange/white wire in the photo above shows the connection to ground. The SNAP node needs this common ground.

The following photo shows my test setup. I made sure everything was working before tampering with the wiring in my office.

![](https://git.synapse-wireless.com/chris.cantrell/office/blob/master/WattStopper/Art/photo.JPG)

## Powering the SNAP Engine

The 5V power supply inside the Watt Stopper does not provide enough current to run the SNAP node (I tried). The easiest solution is to run your SNAP node from a standard wall wart plugged into an outlet near the light switch.

I chose to hack a 5V USB charger and mount the extra supply inside the wall. The little Apple USB charger cube is very tiny. I broke it out of its case and soldered on wires for the mains and wires for the 5V output. I wrapped it in a cardboard insulator before putting it in the wall.

![](https://git.synapse-wireless.com/chris.cantrell/office/blob/master/WattStopper/Art/photo8.jpg)

## Final Assembly

I used an SN171 protoboard for this project. I bought a large faceplate from Home Depot so I could mount the protoboard on the wall. The screw holes on the board match perfectly with the wall plate.

I ran the wires from the Watt Stopper to the screw holes in the protoboard and tucked the excess wiring back into the plate.

![](https://git.synapse-wireless.com/chris.cantrell/office/blob/master/WattStopper/Art/photo5.JPG)

## All in the Wall


### RF200 Wiring ###

| RF200 Pin | RF200 Wire Color | Function  | Watt Stopper Wire Color | Code Snappy IO Number |
|-----------|------------------|-----------|-------------------------|-----------------------|
| 24        | Green            | Ground    | Orange/White            |                       |
| 23        |                  |           |                         |                       |
| 22        |                  |           |                         |                       |
| 21        | Yellow           | Vcc       |                         |                       |
| 20        | Purple           | CBS       | Green                   | 31                    |
| 19        | Gray             | CAS       | Green/White             | 30                    |
| 18        | Orange           | Occupancy | Brown                   | 29                    |
| 17        | Blue             | Button    | Blue                    | 28                    |




