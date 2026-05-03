from manim import *


class CantorsProof(MovingCameraScene):
    def construct(self):
        intro_title = Text("Счётные и несчётные множества", font_size=32).to_edge(UP)
        self.play(Write(intro_title))

        definition = Text(
            "Множество называется счётным, если его элементы\nможно пронумеровать натуральными числами.",
            font_size=20,
            line_spacing=1.5
        ).shift(UP * 1.5)

        rational_def = MathTex(
            r"\mathbb{Q} = \left\{ \frac{m}{n} \mid m \in \mathbb{Z}, n \in \mathbb{N} \right\}",
            color=YELLOW
        ).next_to(definition, DOWN, buff=0.5)

        rational_note = Text("— это пример счётного множества.", font_size=20).next_to(rational_def, DOWN)

        self.play(FadeIn(definition))
        self.wait(1)
        self.play(Write(rational_def))
        self.play(FadeIn(rational_note))
        self.wait(2)

        self.play(FadeOut(definition, rational_def, rational_note))

        uncountable_def = Text(
            "Множество называется несчётным, если оно бесконечно\nи его нельзя сопоставить с натуральными числами.",
            font_size=20,
            line_spacing=1.5
        ).shift(UP * 1.5)

        real_def = MathTex(
            r"\mathbb{R} \in (-\infty, +\infty)",
            color=BLUE
        ).next_to(uncountable_def, DOWN, buff=0.5)

        real_note = Text("— это пример несчётного множества (континуум).", font_size=20).next_to(real_def, DOWN)

        self.play(FadeIn(uncountable_def))
        self.wait(1)
        self.play(Write(real_def))
        self.play(FadeIn(real_note))
        self.wait(2)

        self.play(FadeOut(uncountable_def, real_def, real_note, intro_title))

        title = Text("Доказательство несчётности отрезка", font_size=30).to_edge(UP)
        number_line = NumberLine(x_range=[0, 1, 0.2], length=10).shift(DOWN * 2)
        segment = Line(number_line.n2p(0), number_line.n2p(1), color=YELLOW, stroke_width=6)

        points = [0.25, 0.48, 0.15, 0.82]
        dots = VGroup(*[Dot(number_line.n2p(p), color=BLUE, radius=0.07) for p in points])
        dots_labels = VGroup(*[
            MathTex(f"x_{i + 1}", font_size=20).next_to(dots[i], UP, buff=0.1)
            for i in range(len(dots))
        ])

        self.play(Create(number_line), Create(segment), Write(title))
        self.play(FadeIn(dots, dots_labels))
        self.wait(1)

        list_nums = VGroup(
            MathTex(r"x_1 = 0.", r"a_1^{(1)}", r"a_2^{(1)}", r"a_3^{(1)}", r"a_4^{(1)}", r"\dots"),
            MathTex(r"x_2 = 0.", r"a_1^{(2)}", r"a_2^{(2)}", r"a_3^{(2)}", r"a_4^{(2)}", r"\dots"),
            MathTex(r"x_3 = 0.", r"a_1^{(3)}", r"a_2^{(3)}", r"a_3^{(3)}", r"a_4^{(3)}", r"\dots"),
            MathTex(r"x_4 = 0.", r"a_1^{(4)}", r"a_2^{(4)}", r"a_3^{(4)}", r"a_4^{(4)}", r"\dots"),
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.7).to_edge(LEFT, buff=1).shift(UP * 0.5)

        self.play(FadeIn(list_nums))

        diag_elements = VGroup(
            list_nums[0][1],  # a1(1)
            list_nums[3][4]  # a4(4)
        )

        diag_rect = SurroundingRectangle(list_nums, color=RED, buff=0.2)

        strike_line = Line(
            list_nums[0][1].get_corner(UL),
            list_nums[3][4].get_corner(DR),
            color=RED,
            stroke_width=2
        )

        diag_text = Text("Берем элементы по диагонали", font_size=16, color=RED).next_to(list_nums, DOWN, buff=0.4)

        self.play(
            Create(diag_rect),
            Create(strike_line),
            Write(diag_text)
        )
        self.wait(2)

        x_logic = VGroup(
            Text("Создадим число X:", font_size=18),
            MathTex(r"X = 0.a_1^{(1)} a_2^{(2)} a_3^{(3)} a_4^{(4)} \dots", color=GREEN),
        ).arrange(DOWN, buff=0.3).to_edge(RIGHT, buff=1).shift(UP * 0.5)

        self.play(Write(x_logic))
        self.wait(2)

        target_x = number_line.n2p(0.65)
        dot_x = Dot(target_x, color=GREEN, radius=0.08)
        label_x = MathTex("X", color=GREEN).next_to(dot_x, DOWN, buff=0.2)

        self.play(FadeIn(dot_x, label_x))
        self.play(self.camera.frame.animate.scale(0.5).move_to(target_x), run_time=1.5)
        self.wait(1)
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))

        conclusion = Text(
            "X есть на отрезке, но его нет в списке.\nОтрезок несчётен.",
            color=RED, font_size=20
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(conclusion))
        self.wait(3)
