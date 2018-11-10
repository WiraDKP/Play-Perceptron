def play():
    from ipywidgets import fixed, interact
    from matplotlib.colors import LinearSegmentedColormap            
    cm = LinearSegmentedColormap.from_list("rb", [(1,0,0), (0,0,1)], N=2)
    def plot_not(w1=0.5, w2=0.5, b=-0.7, logic="or"):
        from numpy import meshgrid, linspace
        import matplotlib.pyplot as plt

        x1, x2 = [0,0,1,1], [0,1,0,1]
        color = {"and": [0,0,0,1], "or": [0,1,1,1], "not": [1,0,1,0]}

        x,y = meshgrid(linspace(-0.5,1.5,50), linspace(-0.5,1.5,50))
        z = w1*x+w2*y+b

        plt.figure(figsize=(8,8))
        plt.contourf(x, y, z, 1, cmap=cm, vmin=-1, vmax=1)    
        plt.scatter(x1, x2, c=color[logic], s=150, cmap=cm, zorder=1, vmin=0, vmax=1, linewidths=2, edgecolors='w')
        plt.axis('equal')
        plt.xlim(-0.05,1.05)
        plt.ylim(-0.05,1.05)
        plt.title(f"logic: {logic.upper()}", fontsize=14)
    interact(plot_not, w1=(-1, 1, 0.1), w2=(-1, 1, 0.1), b=(-1, 1, 0.1), logic=["and", "or", "not"]);
