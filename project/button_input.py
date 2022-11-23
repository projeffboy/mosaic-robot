from time import sleep

def button_input(
    draw_0_btn,
    draw_1_btn,
    num_pixels,
    reverse_drawing=False,
    polling_rate=0.5,
    debug=False
):
    drawing = ""

    while True:
        if len(drawing) > num_pixels:
            break
        elif draw_0_btn.is_pressed() and draw_1_btn.is_pressed():
            drawing = input(
                "Please enter the array of 1s and 0s for the canvas:"
            )
            break
        elif draw_0_btn.is_pressed() and not draw_1_btn.is_pressed():
            drawing += "1"
        elif draw_1_btn.is_pressed():
            drawing += "0"
        
        if debug:
            print(drawing)

        sleep(polling_rate)

    number_of_cubes = drawing.count("1")
    if number_of_cubes > 15:
        raise Exception("Maximum number of cubes is 15. Please try again")

    if reverse_drawing:
        drawing = drawing[::-1]
    
    return drawing