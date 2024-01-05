def rating_mapping(rating):
  rating_colors = {
    "A": "#16B13D",
    "B": "#7BB11B",
    "C": "#B19719",
    "D": "#B1671E",
    "E": "#B12B1D"
  }
  return rating_colors.get(rating.strip(), "default_color")