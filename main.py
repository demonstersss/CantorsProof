from manim import *

class CantorsProof(MovingCameraScene):
    def construct(self):
        title = Text("Доказательство несчётности отрезка", font_size=32)
        title.to_edge(UP)
        self.play(Write(title, run_time=2))
        self.wait(1)

        number_line = NumberLine(
            x_range=[0, 1, 0.2],
            length=10,
            include_numbers=False
        ).shift(DOWN * 2)

        labels = VGroup(
            Text("0.0", font_size=16).next_to(number_line.n2p(0), DOWN),
            Text("0.2", font_size=16).next_to(number_line.n2p(0.2), DOWN),
            Text("0.4", font_size=16).next_to(number_line.n2p(0.4), DOWN),
            Text("0.6", font_size=16).next_to(number_line.n2p(0.6), DOWN),
            Text("0.8", font_size=16).next_to(number_line.n2p(0.8), DOWN),
            Text("1.0", font_size=16).next_to(number_line.n2p(1), DOWN),
        )

        segment = Line(number_line.n2p(0), number_line.n2p(1), color=YELLOW, stroke_width=6)

        self.play(Create(number_line, run_time=2), FadeIn(labels, run_time=2))
        self.play(Create(segment, run_time=2))
        self.wait(1.5)

        assumption = Text(
            "Предположим, что все точки отрезка можно перенумеровать",
            font_size=20,
            color=BLUE
        ).next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(assumption, run_time=2))
        self.wait(2)

        list_nums = VGroup(
            Text("x1 -> 0.3 1 4 1 ...", font_size=22),
            Text("x2 -> 0.5 2 9 6 ...", font_size=22),
            Text("x3 -> 0.1 7 3 2 ...", font_size=22),
            Text("x4 -> 0.8 8 8 4 ...", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP * 0.5 + LEFT * 2)

        self.play(FadeIn(list_nums, run_time=2))
        self.wait(2)

        p1 = number_line.n2p(0.314)
        p2 = number_line.n2p(0.529)
        p3 = number_line.n2p(0.173)
        p4 = number_line.n2p(0.888)

        dots = VGroup(
            Dot(p1, color=BLUE, radius=0.06),
            Dot(p2, color=BLUE, radius=0.06),
            Dot(p3, color=BLUE, radius=0.06),
            Dot(p4, color=BLUE, radius=0.06)
        )

        dots_labels = VGroup(
            Text("x1", font_size=14).next_to(dots[0], UP, buff=0.1),
            Text("x2", font_size=14).next_to(dots[1], UP, buff=0.1),
            Text("x3", font_size=14).next_to(dots[2], UP, buff=0.1),
            Text("x4", font_size=14).next_to(dots[3], UP, buff=0.1)
        )

        self.play(FadeIn(dots, run_time=3), FadeIn(dots_labels, run_time=3))
        self.wait(2)

        diag_text = Text(
            "Возьмем новую диагональ (3, 2, 3, 4)",
            font_size=18
        ).next_to(list_nums, RIGHT, buff=0.5).shift(UP * 0.5)

        self.play(Write(diag_text, run_time=2))

        rect = SurroundingRectangle(list_nums, color=RED, buff=0.1)
        self.play(Create(rect, run_time=2))
        self.wait(1.5)

        new_num_title = Text(
            "Изменим каждую цифру. Создаем число X:",
            font_size=18
        ).next_to(diag_text, DOWN, buff=0.3)

        new_num = Text("X = 0.4 3 4 5 ...", color=GREEN, font_size=24).next_to(new_num_title, DOWN, buff=0.3)

        self.play(Write(new_num_title, run_time=2))
        self.play(Write(new_num, run_time=2))
        self.wait(2)

        self.play(
            FadeOut(list_nums, run_time=1.5),
            FadeOut(rect, run_time=1.5),
            FadeOut(diag_text, run_time=1.5),
            FadeOut(new_num_title, run_time=1.5),
            FadeOut(assumption, run_time=1.5),
            new_num.animate.to_edge(UP).shift(DOWN * 0.5)
        )

        self.play(
            number_line.animate.shift(UP * 2),
            segment.animate.shift(UP * 2),
            labels.animate.shift(UP * 2),
            dots.animate.shift(UP * 2),
            dots_labels.animate.shift(UP * 2),
            run_time=2.5
        )
        self.wait(1)

        target_point = number_line.n2p(0.434)

        dot_x = Dot(target_point, color=GREEN, radius=0.04)
        label_x = Text("X", color=GREEN, font_size=20).next_to(dot_x, DOWN, buff=0.2)

        self.play(FadeIn(dot_x, run_time=1.5), Write(label_x, run_time=1.5))
        self.wait(1)

        self.play(
            self.camera.frame.animate.scale(0.1).move_to(target_point),
            run_time=6,
            rate_func=linear
        )
        self.wait(3)

        self.play(
            self.camera.frame.animate.scale(10).move_to(ORIGIN),
            run_time=4
        )
        self.wait(1)

        conclusion = Text(
            "Число X находится на отрезке, но отсутствует в списке!\nЭто противоречит нашему предположению.",
            font_size=18,
            color=RED,
            line_spacing=1.5
        ).shift(DOWN * 2)

        self.play(Write(conclusion, run_time=3))
        self.wait(3)
