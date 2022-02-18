# Cat drinking automation project

This is my project of automatic tap water dispenser for our beloved bengal breed cat. These cats are very picky when it comes to water consumption. They jump on sinks and open the faucet just to get access to fresh tap water. Obviously this is not something I want to see once we are out of the home. 

Yes, there are cheap water fountain solutions on the market. Those are not reliable and require regular maintenance. They mix limited amount of stale water with dust in the air. Not something our cat is interested in. There is another IR sensing solution on the market but that requires mounting on the sink. 

With this project, I wanted to create a safe and flexible system that allows autonomous water feed for the cat without any intervention and the ability to track the usage. 
I am usiang Homeassistant platform for my smart home control so I connected the GPIO pins usage for monitoring purposes. 

**Electrical parts used:**
- IR sensor: SR505
- 2x Relay module (5V in, LOW trigger): KY-019
- rPi Zero W
- Level Shifter module 
- Switch with 12V LED ring 
- Short LED strip 12V
- Power Socket splitter

**Water parts used:**
- Angle Stop Valve: John Guest ASV9
- Solenoid 12V valve: Puro-xd-12
- 2x Angled tubing elbow: John Guest PI0308S
- 2meters 1/4" tube: John Guest PE-08-BI-0500F

The relay module had difficulty with 3.3V input from GPIO pin. I found **[this article](https://www.raspberrypi-spy.co.uk/2018/09/using-a-level-shifter-with-the-raspberry-pi-gpio/)** that gave me idea to use the level switcher module. 

Here is a work in progress **[Python script](/automation.py)** that drives the logic for scenarios explained below. 

In case you want to monitor the system here are **[Homeassistant settings](/configuration.yaml)**, you need to enter these in configuration.yaml file. 

**Scenarios explanation:**

- Switch OFF: power to the IR sensor is cut by main switch, main and switch light relays are turned off, x variable is turned on
- Switch ON first time: power to the IR sensor is restored by main switch, x variable and main relay is turned off, switch light relay is on > time delay before sensing (I had to add this delay because IR sensor gets into HIGH output state after it recieves power) > continue to other scenarios
- Switch ON movement OFF: power to the IR sensor is cut by main switch, main relay is turned off
- Switch ON movement ON: power to the IR sensor is cut by main switch, main relay is turned on > time for drinking > main relay is turned off > sensing stopped to avoid repetitive motion detection

Basic schematics showing all parts used: 
