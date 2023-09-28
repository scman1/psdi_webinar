import manage_athena as athenamgr

from matplotlib import pyplot as plt
import matplotlib.cm as cm

# individaul LCF plots
def make_subplot(a_subplt, group1, group2):
    a_subplt.plot(group1.energy, group1.norm, label=group1.filename, linewidth=4,color='blue')
    a_subplt.plot(group2.energy, group2.norm, label=group2.filename, linewidth=2, color='orange',linestyle='--')
    a_subplt.grid(color='black', linestyle=':', linewidth=1) #show and format grid
    a_subplt.set_title(group2.arrayname, fontsize=8)
    a_subplt.legend() # show legend
     
    a_subplt.set_xlim([29180, 29230])
    #a_subplt.set_ylim([0, 1.5])
    #a_subplt.tick_params(axis='both', which='major', labelsize=9)
    #xlabels = a_subplt.get_xticklabels()
    #a_subplt.set_xticks(xlabels, rotation = 90)
    return a_subplt

# compare LCF plots
def compare_lcf_plot(result_list):
    components = len(result_list)
    fig = plt.figure(figsize=(8, 2))
    fig, axes = plt.subplots(1,components, constrained_layout=True)
    for i in range(0,components):
        axes[i] = make_subplot(axes[i], result_list[i][0], result_list[i][1])
    return fig


#chik plots
# using markers
def plot_markers(data_set,rmin,rmax,kmin,kmax, datalabel="data"):
    fig = plt.figure()#figsize=(10, 8))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    # Creating the chifit plot from scratch
    #from .xlarch.wxlibafsplots import plot_chifit
    #plot_chifit(dset, _larch=session)
    
    ax1.plot(data_set.data.k, data_set.data.chi*data_set.data.k**2, marker='$\u25CC$', markerfacecolor='b', 
                markeredgecolor='b', markersize=4, linestyle='none', label=datalabel)
    
    ax1.plot(data_set.model.k, data_set.model.chi*data_set.data.k**2 , color='r', label='fit')
    ax1.set_xlim(kmin, kmax)
    ax1.set_ylim(-1, 2)
    ax1.set_xlabel("$k (\mathrm{\AA})^{-1}$")
    ax1.set_ylabel("$k^2$ $\chi (k)(\mathrm{\AA})^{-2}$")
    ax1.legend()
    
    ax2.plot(data_set.data.r, data_set.data.chir_mag, marker='$\u25CC$', markerfacecolor='b', 
                markeredgecolor='b', markersize=4, linestyle='none', label=datalabel)
 
    ax2.plot(data_set.model.r, data_set.model.chir_mag, color='r', label='fit')
    ax2.set_xlim(rmin,rmax)
    ax2.set_xlabel("$R(\mathrm{\AA})$")
    ax2.set_ylabel("$|\chi(R)|(\mathrm{\AA}^{-3})$")
    ax2.legend(loc='upper right')

    return plt

# using lines
def plot_fit(data_set,rmin,rmax,kmin,kmax, datalabel="data"):
    fig = plt.figure()#figsize=(10, 8))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    # Creating the chifit plot from scratch
    #from .xlarch.wxlibafsplots import plot_chifit
    #plot_chifit(dset, _larch=session)
    ax1.plot(data_set.data.k, data_set.data.chi*data_set.data.k**2, color='b', label=datalabel)
    ax1.plot(data_set.model.k, data_set.model.chi*data_set.data.k**2 , color='r', label='fit')
    ax1.set_xlim(kmin, kmax)
    ax1.set_ylim(-1, 2)
    ax1.set_xlabel("$k (\mathrm{\AA})^{-1}$")
    ax1.set_ylabel("$k^2$ $\chi (k)(\mathrm{\AA})^{-2}$")
    ax1.legend()

    ax2.plot(data_set.data.r, data_set.data.chir_mag, color='b', label=datalabel)
    ax2.plot(data_set.model.r, data_set.model.chir_mag, color='r', label='fit')
    ax2.set_xlim(rmin,rmax)
    ax2.set_xlabel("$R(\mathrm{\AA})$")
    ax2.set_ylabel("$|\chi(R)|(\mathrm{\AA}^{-3})$")
    ax2.legend(loc='upper right')

    return plt

# using circles
def plot_circles(data_set,rmin,rmax,kmin,kmax, datalabel="data"):
    fig = plt.figure()#figsize=(10, 8))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    # Creating the chifit plot from scratch
    #from .xlarch.wxlibafsplots import plot_chifit
    #plot_chifit(dset, _larch=session)
    
    ax1.plot(data_set.data.k, data_set.data.chi*data_set.data.k**2, color='cyan', label=datalabel)
    c_size = 0.07
    for a, b, in zip(data_set.data.k, data_set.data.chi*data_set.data.k**2):
        circle = plt.Circle((a, b), c_size, fill=False)
        ax1.add_artist(circle)
    
    ax1.plot(data_set.model.k, data_set.model.chi*data_set.data.k**2 , color='r', label='fit')
    ax1.set_xlim(kmin, kmax)
    ax1.set_ylim(-1, 2)
    ax1.set_xlabel("$k (\mathrm{\AA})^{-1}$")
    ax1.set_ylabel("$k^2$ $\chi (k)(\mathrm{\AA})^{-2}$")
    ax1.legend()
    
    ax2.plot(data_set.data.r, data_set.data.chir_mag, color='cyan', label=datalabel)
    c_size = 0.025
    for a, b, in zip(data_set.data.r, data_set.data.chir_mag):
        circle = plt.Circle((a, b), c_size, fill=False)
        ax2.add_artist(circle)
    ax2.plot(data_set.model.r, data_set.model.chir_mag, color='r', label='fit')
    ax2.set_xlim(rmin,rmax)
    ax2.set_xlabel("$R(\mathrm{\AA})$")
    ax2.set_ylabel("$|\chi(R)|(\mathrm{\AA}^{-3})$")
    ax2.legend(loc='upper right')

    return plt

def get_groups(data_file, data_mappings):
    data_prj = athenamgr.read_project(data_file)
    data_groups = {}
    for a_mapping in data_mappings:
        data_groups[a_mapping] = athenamgr.calc_with_defaults(athenamgr.get_group(data_prj, data_mappings[a_mapping]))
        data_groups[a_mapping].filename =  a_mapping
    return data_groups

# plot normalised spectrum wir custom colors and line styles
def plot_normalised(athena_groups = {}, include_groups = {}, aspect = (6,8), xlim=[],ylim=[]):
    plt.figure(figsize=aspect)
    for g_indx, a_group in enumerate(include_groups):
        if athena_groups[a_group].filename in include_groups:
                plt.plot(athena_groups[a_group].energy, 
                         athena_groups[a_group].norm, 
                         label=athena_groups[a_group].filename,
                         color = include_groups[a_group][0],
                         linestyle = include_groups[a_group][1]
                        ) 

    frame1 = plt.gca()
    #frame1.axes.yaxis.set_ticklabels([])
    #frame1.axes.yaxis.set_ticklabels([])
    plt.ylabel("Normalized XANES (a.u.)")
    plt.xlabel("Energy (eV)")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.legend()
    plt.show()

    return plt