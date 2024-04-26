import customtkinter as ctk

root = ctk.CTk()

display_text = ctk.StringVar()  # Variable to hold the text to display

calculation = ""


def main():
    calculator()
    root.mainloop()


def calculator():
    def calculation(text):
        global calculation

        current_text = display_text.get()  # Get current text from display
        current_calculation = calculation

        # starter character
        if len(current_text) == 0:
            display_text.set(text)  # current text + another number
            calculation = text
        else:
            display_text.set(current_text + text)  # current text + another number
            calculation = current_calculation + text

            # clear display using C
            if text == "clear":
                display_text.set("")
                calculation = 0

            # Remove last character
            if text == "⌫":
                display_text.set(current_text[:-1])
                calculation = current_calculation[:-1]

            if text == "x":
                display_text.set(current_text + text)
                calculation = current_calculation + str('*')

            if text == "÷":
                display_text.set(current_text + text)
                calculation = current_calculation + str('/')

            if text == "=":
                result = eval(calculation[:-1])
                calculation = calculation[:-1]

                calculation = str(result)

                display_text.set(result)
                print(result)

        print(calculation)

    # this is where all contents are created
    # this means buttons, frame and all other
    # rendering contents

    """ rendering contents """

    # Create core custom tkinter
    # root is everything the whole container
    root.attributes('-alpha', 0.95)

    # Set title
    root.title("Calculator")

    # define frame width and height
    frame_width = 350
    frame_height = 550
    root.geometry(f"{frame_width}x{frame_height}")

    root.resizable(False, False)

    # define color scheme
    ctk.set_appearance_mode("#030303")
    ctk.set_default_color_theme("green")

    # variable colours
    primary = "#1c1c1b"
    secondary = "#0ecf68"
    white = "#fcfcfc"
    gray = "#828181"
    tertiary = "#d11d2f"

    btn_hover = "#2e2d2d"
    btn2_hover = "#0b994d"

    # each button size
    # this is width AND height
    button_size = 80

    # create rows
    row_1 = ctk.CTkFrame(root,
                         width=350,
                         height=100,
                         )
    row_1.grid(pady=10, row=1)

    row_2 = ctk.CTkFrame(root,
                         width=350,
                         height=100,
                         )
    row_2.grid(row=2)

    row_3 = ctk.CTkFrame(root,
                         width=350,
                         height=100,
                         )
    row_3.grid(row=3)

    row_4 = ctk.CTkFrame(root,
                         width=350,
                         height=100,
                         )
    row_4.grid(row=4)

    row_5 = ctk.CTkFrame(root,
                         width=350,
                         height=100,
                         )
    row_5.grid(row=5)

    row_6 = ctk.CTkFrame(root,
                         width=350,
                         height=100,
                         )
    row_6.grid(row=6)

    # label for displaying inputs and outputs
    # aka frame on top
    display = ctk.CTkLabel(row_1,
                           width=350,
                           height=100,
                           fg_color=primary,
                           corner_radius=5,
                           text="",
                           anchor="w"

                           )

    display.grid(row=1, column=1, columnspan=4, sticky="w")

    display_content = ctk.CTkLabel(root,
                                   textvariable=display_text,
                                   anchor="e",
                                   font=("arial", 40),
                                   fg_color=primary,
                                   corner_radius=0,
                                   bg_color=primary,

    )

    display_content.grid(row=1, sticky="w", padx=20)

    backspace = ctk.CTkButton(root,
                              width=50,
                              text="⌫",
                              anchor="e",
                              font=("arial", 30),
                              fg_color=primary,
                              corner_radius=0,
                              hover_color=primary,
                              border_width=0,
                              bg_color=primary,
                              command=lambda: calculation("⌫"))

    backspace.grid(row=1, sticky="e", padx=10)
    # C #
    btn_c = ctk.CTkButton(row_2,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" C ",
                          border_color=tertiary,
                          border_width=0,
                          text_color=tertiary,
                          font=("arial", 20),
                          command=lambda: calculation("clear"))

    btn_c.grid(row=2, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # () #
    btn_brackets = ctk.CTkButton(row_2,
                                 width=button_size,
                                 height=button_size,
                                 fg_color=primary,
                                 hover_color=btn_hover,
                                 text="( )",
                                 border_color=gray,
                                 border_width=0,
                                 text_color=white,
                                 font=("arial", 20),
                                 command=lambda: calculation("( )"))

    btn_brackets.grid(row=2, column=2, sticky="w", columnspan=1,  padx=2, pady=2)

    # % #
    btn_percentage = ctk.CTkButton(row_2,
                                   width=button_size,
                                   height=button_size,
                                   fg_color=primary,
                                   hover_color=btn_hover,
                                   text=" % ",
                                   border_color=gray,
                                   border_width=0,
                                   text_color=white,
                                   font=("arial", 20),
                                   command=lambda: calculation("%"))

    btn_percentage.grid(row=2, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # : #
    btn_divide = ctk.CTkButton(row_2,
                               width=button_size,
                               height=button_size,
                               fg_color=primary,
                               hover_color=btn_hover,
                               text=" ÷ ",
                               border_color=gray,
                               border_width=0,
                               text_color=white,
                               font=("arial", 20),
                               command=lambda: calculation("÷"))

    btn_divide.grid(row=2, column=4, sticky="w", columnspan=1, padx=2, pady=2)

    # 7 #
    btn_7 = ctk.CTkButton(row_3,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 7 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("7"))

    btn_7.grid(row=3, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # 8 #
    btn_8 = ctk.CTkButton(row_3,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 8 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("8"))

    btn_8.grid(row=3, column=2, sticky="w", columnspan=1, padx=2, pady=2)

    # 9 #
    btn_9 = ctk.CTkButton(row_3,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 9 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("9"))

    btn_9.grid(row=3, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # x #
    btn_x = ctk.CTkButton(row_3,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" x ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("x"))

    btn_x.grid(row=3, column=4, sticky="w", columnspan=1, padx=2, pady=2)

    # 4 #
    btn_4 = ctk.CTkButton(row_4,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 4 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("4"))

    btn_4.grid(row=4, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # 5 #
    btn_5 = ctk.CTkButton(row_4,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 5 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("5"))

    btn_5.grid(row=4, column=2, sticky="w", columnspan=1, padx=2, pady=2)

    # 6 #
    btn_6 = ctk.CTkButton(row_4,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 6 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("6"))

    btn_6.grid(row=4, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # - #
    btn_minus = ctk.CTkButton(row_4,
                              width=button_size,
                              height=button_size,
                              fg_color=primary,
                              hover_color=btn_hover,
                              text=" - ",
                              border_color=gray,
                              border_width=0,
                              text_color=white,
                              font=("arial", 20),
                              command=lambda: calculation("-"))

    btn_minus.grid(row=4, column=4, sticky="w", columnspan=1, padx=2, pady=2)

    # 1 #
    btn_1 = ctk.CTkButton(row_5,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 1 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("1"))

    btn_1.grid(row=5, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # 2 #
    btn_2 = ctk.CTkButton(row_5,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 2 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("2"))

    btn_2.grid(row=5, column=2, sticky="w", columnspan=1, padx=2, pady=2)

    # 3 #
    btn_3 = ctk.CTkButton(row_5,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 3 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("3"))

    btn_3.grid(row=5, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # + #
    btn_plus = ctk.CTkButton(row_5,
                             width=button_size,
                             height=button_size,
                             fg_color=primary,
                             hover_color=btn_hover,
                             text=" + ",
                             border_color=gray,
                             border_width=0,
                             text_color=white,
                             font=("arial", 20),
                             command=lambda: calculation("+"))

    btn_plus.grid(row=5, column=4, sticky="w", columnspan=1, padx=2, pady=2)

    # +/- #
    btn_idk = ctk.CTkButton(row_6,
                            width=button_size,
                            height=button_size,
                            fg_color=primary,
                            hover_color=btn_hover,
                            text="+/-",
                            border_color=gray,
                            border_width=0,
                            text_color=white,
                            font=("arial", 20),
                            command=lambda: calculation("-/+"))

    btn_idk.grid(row=6, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # 0 #
    btn_0 = ctk.CTkButton(row_6,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=btn_hover,
                          text=" 0 ",
                          border_color=gray,
                          border_width=0,
                          text_color=white,
                          font=("arial", 20),
                          command=lambda: calculation("0"))

    btn_0.grid(row=6, column=2, sticky="w", columnspan=1, padx=2, pady=2)

    # . #
    btn_dot = ctk.CTkButton(row_6,
                            width=button_size,
                            height=button_size,
                            fg_color=primary,
                            hover_color=btn_hover,
                            text=" . ",
                            border_color=gray,
                            border_width=0,
                            text_color=white,
                            font=("arial", 20),
                            command=lambda: calculation("."))

    btn_dot.grid(row=6, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # = #
    btn_equals = ctk.CTkButton(row_6,
                               width=button_size,
                               height=button_size,
                               fg_color=secondary,
                               hover_color=btn2_hover,
                               text=" = ",
                               border_color=secondary,
                               border_width=0,
                               text_color=white,
                               font=("arial", 20),
                               command=lambda: calculation("="))

    btn_equals.grid(row=6, column=4, sticky="w", columnspan=1, padx=2, pady=2)


if __name__ == "__main__":
    main()