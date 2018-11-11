def play():
    from ipywidgets import fixed, interact
    from matplotlib.colors import LinearSegmentedColormap      
    from numpy import meshgrid, linspace    
    cm = LinearSegmentedColormap.from_list("rb", [(1,0,0), (0,0,1)], N=2)

    x1, x2 = [0,0,1,1], [0,1,0,1]
    color = {"and": [0,0,0,1], "or": [0,1,1,1], "not": [1,0,1,0]}
    x,y = meshgrid(linspace(-0.05,1.05,100), linspace(-0.05,1.05,100))
    
    def plot_not(w1=0.5, w2=0.5, b=-0.7, logic="or"):
        from numpy import zeros
        import matplotlib.pyplot as plt
        from mpl_toolkits import mplot3d

        z = w1*x+w2*y+b

        fig = plt.figure(figsize=(16,16))
        ax1 = fig.add_subplot(2,2,1)
        ax1.contourf(x, y, z, 1, cmap=cm, vmin=-1, vmax=1)    
        ax1.scatter(x1, x2, c=color[logic], s=150, cmap=cm, zorder=1, vmin=0, vmax=1, linewidths=2, edgecolors='w')
        ax1.axis('equal')
        ax1.set(xlim=(-0.05,1.05), ylim=(-0.05,1.05))
        ax1.set_title(f"logic: {logic.upper()}", fontsize=14)

        ax2 = fig.add_subplot(2,2,2, projection='3d')
        ax2.plot_wireframe(x, y, zeros((100,100)), color='w', alpha=0.2)
        ax2.plot_surface(x, y, z, cmap=cm, vmin=-1, vmax=1, zorder=1)
        ax2.set(xlim=(-0.05,1.05), ylim=(-0.05,1.05), zlim=(-1,1), xlabel="x1", ylabel='x2')
        ax2.view_init(elev=30, azim=-90)
        
    interact(plot_not, w1=(-1, 1, 0.1), w2=(-1, 1, 0.1), b=(-1, 1, 0.1), logic=["and", "or", "not"]);
