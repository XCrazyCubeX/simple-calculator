import customtkinter as ctk


def render():
    """ rendering contents """
    # this is where all contents are created
    # this means buttons, frame and all other
    # rendering contents

    # Create core custom tkinter
    # root is everything the whole container
    root = ctk.CTk()
    root.attributes('-alpha', 0.95)

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
    hovers = "#2e2d2d"

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
                           )

    display.grid(row=1, column=1, columnspan=8)

    # C #
    btn_c = ctk.CTkButton(row_2,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" C ",
                          border_color=tertiary,
                          border_width=1,
                          text_color=tertiary,
                          font=("arial", 20,))

    btn_c.grid(row=2, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # () #
    btn_brackets = ctk.CTkButton(row_2,
                                 width=button_size,
                                 height=button_size,
                                 fg_color=primary,
                                 hover_color=hovers,
                                 text="( )",
                                 border_color=gray,
                                 border_width=1,
                                 text_color=white,
                                 font=("arial", 20,))

    btn_brackets.grid(row=2, column=2, sticky="w", columnspan=1,  padx=2, pady=2)

    # % #
    btn_percentage = ctk.CTkButton(row_2,
                                   width=button_size,
                                   height=button_size,
                                   fg_color=primary,
                                   hover_color=hovers,
                                   text=" % ",
                                   border_color=gray,
                                   border_width=1,
                                   text_color=white,
                                   font=("arial", 20,))

    btn_percentage.grid(row=2, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # : #
    btn_divide = ctk.CTkButton(row_2,
                               width=button_size,
                               height=button_size,
                               fg_color=primary,
                               hover_color=hovers,
                               text=" ÷ ",
                               border_color=gray,
                               border_width=1,
                               text_color=white,
                               font=("arial", 20,))

    btn_divide.grid(row=2, column=4, sticky="w", columnspan=1, padx=2, pady=2)

    # 7 #
    btn_7 = ctk.CTkButton(row_3,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 7 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_7.grid(row=3, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # 8 #
    btn_8 = ctk.CTkButton(row_3,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 8 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_8.grid(row=3, column=2, sticky="w", columnspan=1, padx=2, pady=2)

    # 9 #
    btn_9 = ctk.CTkButton(row_3,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 9 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_9.grid(row=3, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # x #
    btn_x = ctk.CTkButton(row_3,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" x ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_x.grid(row=3, column=4, sticky="w", columnspan=1, padx=2, pady=2)

    # 4 #
    btn_4 = ctk.CTkButton(row_4,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 4 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_4.grid(row=4, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # 5 #
    btn_5 = ctk.CTkButton(row_4,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 5 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_5.grid(row=4, column=2, sticky="w", columnspan=1, padx=2, pady=2)

    # 6 #
    btn_6 = ctk.CTkButton(row_4,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 6 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_6.grid(row=4, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # - #
    btn_minus = ctk.CTkButton(row_4,
                              width=button_size,
                              height=button_size,
                              fg_color=primary,
                              hover_color=hovers,
                              text=" - ",
                              border_color=gray,
                              border_width=1,
                              text_color=white,
                              font=("arial", 20,))

    btn_minus.grid(row=4, column=4, sticky="w", columnspan=1, padx=2, pady=2)

    # 1 #
    btn_1 = ctk.CTkButton(row_5,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 1 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_1.grid(row=5, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # 2 #
    btn_2 = ctk.CTkButton(row_5,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 2 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_2.grid(row=5, column=2, sticky="w", columnspan=1, padx=2, pady=2)

    # 3 #
    btn_3 = ctk.CTkButton(row_5,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 3 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_3.grid(row=5, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # + #
    btn_plus = ctk.CTkButton(row_5,
                             width=button_size,
                             height=button_size,
                             fg_color=primary,
                             hover_color=hovers,
                             text=" + ",
                             border_color=gray,
                             border_width=1,
                             text_color=white,
                             font=("arial", 20,))

    btn_plus.grid(row=5, column=4, sticky="w", columnspan=1, padx=2, pady=2)

    # +/- #
    btn_idk = ctk.CTkButton(row_6,
                            width=button_size,
                            height=button_size,
                            fg_color=primary,
                            hover_color=hovers,
                            text="+/-",
                            border_color=gray,
                            border_width=1,
                            text_color=white,
                            font=("arial", 20,))

    btn_idk.grid(row=6, column=1, sticky="w", columnspan=1, padx=2, pady=2)

    # 0 #
    btn_0 = ctk.CTkButton(row_6,
                          width=button_size,
                          height=button_size,
                          fg_color=primary,
                          hover_color=hovers,
                          text=" 0 ",
                          border_color=gray,
                          border_width=1,
                          text_color=white,
                          font=("arial", 20,))

    btn_0.grid(row=6, column=2, sticky="w", columnspan=1, padx=2, pady=2)

    # . #
    btn_dot = ctk.CTkButton(row_6,
                            width=button_size,
                            height=button_size,
                            fg_color=primary,
                            hover_color=hovers,
                            text=" . ",
                            border_color=gray,
                            border_width=1,
                            text_color=white,
                            font=("arial", 20,))

    btn_dot.grid(row=6, column=3, sticky="w", columnspan=1, padx=2, pady=2)

    # = #
    btn_equals = ctk.CTkButton(row_6,
                               width=button_size,
                               height=button_size,
                               fg_color=secondary,
                               hover_color=hovers,
                               text=" = ",
                               border_color=secondary,
                               border_width=1,
                               text_color=white,
                               font=("arial", 20,))

    btn_equals.grid(row=6, column=4, sticky="w", columnspan=1, padx=2, pady=2)

    return root


if __name__ == '__main__':
    root = render()
    root.mainloop()
