import matplotlib.pyplot as plt

PANEL_THICKNESS = 18

def draw_wardrobe(wardrobe):
    fig, ax = plt.subplots(figsize=(12, 6))

    x = 0
    for bay in wardrobe.bays:
        # Bay outline
        ax.add_patch(
            plt.Rectangle(
                (x, 0),
                bay.width,
                wardrobe.height,
                fill=False,
                linewidth=1.5
            )
        )

        # Shelves
        for shelf in bay.shelves:
            ax.plot(
                [x + PANEL_THICKNESS, x + bay.width - PANEL_THICKNESS],
                [shelf.y, shelf.y],
                linewidth=2
            )

        # Hanging rails
        for h in bay.hangings:
            ax.plot(
                [x + PANEL_THICKNESS, x + bay.width - PANEL_THICKNESS],
                [h.top, h.top],
                linestyle="--",
                linewidth=2
            )

        # Drawers
        for d in bay.drawers:
            ax.add_patch(
                plt.Rectangle(
                    (x + PANEL_THICKNESS, d.y),
                    bay.width - 2 * PANEL_THICKNESS,
                    d.height,
                    fill=False
                )
            )

        x += bay.width

    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(0, wardrobe.total_width)
    ax.set_ylim(0, wardrobe.height)

    return fig
