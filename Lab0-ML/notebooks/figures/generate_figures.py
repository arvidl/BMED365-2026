"""
Module for generating and saving figures used in BMED365 notebooks.

Usage:
    from figures.generate_figures import generate_all_figures
    generate_all_figures()  # Generates and saves all figures

Or for individual figures:
    from figures.generate_figures import plot_dataset_split
    fig = plot_dataset_split(save=True)
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for servers/scripts
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

# Find the directory where this script is located
FIGURE_DIR = Path(__file__).parent


def plot_training_test_split(figsize=(10, 3), save=False, filename="training_test_split.png"):
    """
    Visualizes simple dataset split into training and test sets.
    
    This is the basic split before we introduce the validation set.
    The figure shows two boxes: Training set (light gray) and Test set (dark gray),
    with "All available data" as the header.
    
    Parameters:
    -----------
    figsize : tuple
        Size of the figure (width, height)
    save : bool
        Whether the figure should be saved to file
    filename : str
        Filename for saving
        
    Returns:
    -----------
    fig, ax : matplotlib figure and axis
    """
    from matplotlib.patches import FancyBboxPatch
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # =========================================================================
    # COLORS AND DIMENSIONS
    # =========================================================================
    # Colors matching the original figure
    training_color = '#E5E5E5'      # Light gray
    test_color = '#808080'           # Dark gray
    border_color = '#666666'         # Gray border
    text_color = '#333333'           # Dark text
    
    # Dimensions
    total_width = 10
    training_ratio = 0.75            # 75% for training
    test_ratio = 0.25                # 25% for test
    height = 1.2
    y_pos = 1
    
    training_width = total_width * training_ratio
    test_width = total_width * test_ratio
    
    # =========================================================================
    # DRAW OUTER FRAME (ENTIRE DATASET)
    # =========================================================================
    outer_frame = FancyBboxPatch(
        (0, y_pos), total_width, height,
        boxstyle="round,pad=0,rounding_size=0.15",
        facecolor='none',
        edgecolor=border_color,
        linewidth=2
    )
    ax.add_patch(outer_frame)
    
    # =========================================================================
    # DRAW TRAINING SET (left part)
    # =========================================================================
    training_box = FancyBboxPatch(
        (0, y_pos), training_width, height,
        boxstyle="round,pad=0,rounding_size=0.15",
        facecolor=training_color,
        edgecolor=border_color,
        linewidth=1.5
    )
    ax.add_patch(training_box)
    
    # Training set label
    ax.text(training_width / 2, y_pos + height / 2, 'Training set',
           ha='center', va='center', fontsize=14, fontweight='normal',
           color=text_color)
    
    # =========================================================================
    # DRAW TEST SET (right part)
    # =========================================================================
    test_box = FancyBboxPatch(
        (training_width, y_pos), test_width, height,
        boxstyle="round,pad=0,rounding_size=0.15",
        facecolor=test_color,
        edgecolor=border_color,
        linewidth=1.5
    )
    ax.add_patch(test_box)
    
    # Test set label (white text on dark background)
    ax.text(training_width + test_width / 2, y_pos + height / 2, 'Test set',
           ha='center', va='center', fontsize=14, fontweight='normal',
           color='white')
    
    # =========================================================================
    # DRAW "ALL AVAILABLE DATA" LINE AND LABEL
    # =========================================================================
    line_y = y_pos - 0.4
    
    # Horizontal line
    ax.plot([0, total_width], [line_y, line_y], 
           color=text_color, linewidth=1.5)
    
    # Vertical end caps
    ax.plot([0, 0], [line_y - 0.1, line_y + 0.1], 
           color=text_color, linewidth=1.5)
    ax.plot([total_width, total_width], [line_y - 0.1, line_y + 0.1], 
           color=text_color, linewidth=1.5)
    
    # Label
    ax.text(total_width / 2, line_y - 0.35, 'All available data',
           ha='center', va='top', fontsize=12, fontweight='bold',
           color=text_color)
    
    # =========================================================================
    # ADJUST AXES AND LAYOUT
    # =========================================================================
    ax.set_xlim(-0.5, total_width + 0.5)
    ax.set_ylim(-0.2, y_pos + height + 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if save:
        filepath = FIGURE_DIR / filename
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figure saved: {filepath}")
    
    return fig, ax


def plot_dataset_split(figsize=(10, 4), save=False, filename="dataset_split.png"):
    """
    Visualizes dataset split into training, validation, and test sets.
    
    Parameters:
    -----------
    figsize : tuple
        Size of the figure (width, height)
    save : bool
        Whether the figure should be saved to file
    filename : str
        Filename for saving
        
    Returns:
    -----------
    fig, ax : matplotlib figure and axis
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Proportions: Training set (3 parts), Validation (1 part), Test (1 part)
    height = 1
    gap = 0.3  # Space between main set and test set
    
    # Colors (matching the original figure)
    training_color = '#FFFFFF'      # White
    border_color = '#2C3E50'        # Dark border
    val_color = '#F5B7B1'           # Light pink
    test_color = '#CD6155'          # Darker pink/red
    
    # Draw training set (3 white boxes with internal lines)
    for i in range(3):
        rect = plt.Rectangle((i, 0), 1, height, 
                            facecolor=training_color, 
                            edgecolor=border_color, 
                            linewidth=2)
        ax.add_patch(rect)
    
    # Draw validation set (1 light pink box)
    rect_val = plt.Rectangle((3, 0), 1, height,
                             facecolor=val_color,
                             edgecolor=border_color,
                             linewidth=2)
    ax.add_patch(rect_val)
    
    # Draw test set (1 dark pink box, separated with gap)
    rect_test = plt.Rectangle((4 + gap, 0), 1, height,
                              facecolor=test_color,
                              edgecolor=border_color,
                              linewidth=2.5)
    ax.add_patch(rect_test)
    
    # Draw outer frame around training+validation set
    outer_rect = plt.Rectangle((0, 0), 4, height,
                               facecolor='none',
                               edgecolor=border_color,
                               linewidth=3)
    ax.add_patch(outer_rect)
    
    # Upper brace for "Dataset D"
    brace_y = height + 0.15
    ax.plot([0, 0], [brace_y, brace_y + 0.15], 'k-', lw=1.5)
    ax.plot([0, 5.3], [brace_y + 0.15, brace_y + 0.15], 'k-', lw=1.5)
    ax.plot([5.3, 5.3], [brace_y, brace_y + 0.15], 'k-', lw=1.5)
    ax.text(2.65, brace_y + 0.35, r'Dataset $\mathcal{D}$', 
            ha='center', va='bottom', fontsize=14, fontstyle='italic')
    
    # Lower braces and labels
    brace_y_low = -0.15
    
    # Training set braces
    ax.plot([0.1, 0.1], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([0.1, 2.9], [brace_y_low - 0.1, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([2.9, 2.9], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.text(1.5, brace_y_low - 0.25, 'Training set', ha='center', va='top', fontsize=11)
    
    # Validation set braces
    ax.plot([3.1, 3.1], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([3.1, 3.9], [brace_y_low - 0.1, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([3.9, 3.9], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.text(3.5, brace_y_low - 0.25, 'Validation\nset', ha='center', va='top', fontsize=10)
    
    # Test set braces
    test_start = 4 + gap
    ax.plot([test_start + 0.1, test_start + 0.1], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([test_start + 0.1, test_start + 0.9], [brace_y_low - 0.1, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([test_start + 0.9, test_start + 0.9], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.text(test_start + 0.5, brace_y_low - 0.25, 'Test set', ha='center', va='top', fontsize=11)
    
    # Adjust axes
    ax.set_xlim(-0.3, 6)
    ax.set_ylim(-0.75, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if save:
        filepath = FIGURE_DIR / filename
        fig.savefig(filepath, dpi=150, bbox_inches='tight', 
                    facecolor='white', edgecolor='none')
        print(f"✓ Figure saved: {filepath}")
    
    return fig, ax


def plot_kfold_cross_validation(k=5, figsize=(12, 4), save=False, 
                                filename="kfold_cross_validation.png"):
    """
    Visualizes K-fold cross-validation (simple version with boxes).
    See plot_kfold_cross_validation_balls() for version with colored balls.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Colors
    training_color = '#AED6F1'      # Light blue
    val_color = '#E74C3C'           # Red
    border_color = '#2C3E50'        # Dark border
    
    box_height = 0.6
    row_spacing = 0.9
    
    for fold in range(k):
        y_pos = (k - 1 - fold) * row_spacing
        
        for i in range(k):
            if i == fold:
                color = val_color
            else:
                color = training_color
            
            rect = plt.Rectangle((i, y_pos), 1, box_height,
                                 facecolor=color,
                                 edgecolor=border_color,
                                 linewidth=1.5)
            ax.add_patch(rect)
        
        ax.text(-0.5, y_pos + box_height/2, f'Fold {fold + 1}',
               ha='right', va='center', fontsize=10, fontweight='bold')
    
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=training_color, edgecolor=border_color, label='Training data'),
        Patch(facecolor=val_color, edgecolor=border_color, label='Validation data')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
    ax.set_title(f'{k}-fold cross-validation', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(-1, k + 0.5)
    ax.set_ylim(-0.3, k * row_spacing + 0.3)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    
    if save:
        filepath = FIGURE_DIR / filename
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figure saved: {filepath}")
    
    return fig, ax


def plot_kfold_cross_validation_balls(k=4, n_datapoints=20, figsize=(14, 8), 
                                      save=False, filename="kfold_balls.png"):
    """
    Visualizes K-fold cross-validation with colored balls representing data points.
    
    This figure shows:
    - Each row represents one iteration/fold
    - Colored balls represent individual data points
    - A frame marks the test/validation fold
    - Arrows and labels explain the split
    
    Parameters:
    -----------
    k : int
        Number of folds (default: 4)
    n_datapoints : int
        Total number of data points to show (default: 20)
    figsize : tuple
        Size of the figure
    save : bool
        Whether the figure should be saved
    filename : str
        Filename for saving
    """
    from matplotlib.patches import FancyBboxPatch, Circle
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.patches as mpatches
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # =========================================================================
    # COLOR PALETTE - Matches the original figure
    # =========================================================================
    # Two main colors for the data points (alternating between them)
    color_red = '#E74C3C'          # Red/coral
    color_teal = '#1ABC9C'         # Teal/turquoise
    
    # Lighter versions for test data section (to show they are "selected")
    color_red_light = '#F5B7B1'    # Light red/pink
    color_teal_light = '#A3E4D7'   # Light teal
    
    # Frame and text colors
    frame_color = '#2C3E50'        # Dark blue/gray for frames
    text_color = '#3498DB'         # Blue for text boxes
    background_color = '#EBF5FB'   # Light blue background
    
    # =========================================================================
    # DIMENSIONS AND LAYOUT
    # =========================================================================
    ball_radius = 0.35
    ball_spacing = 0.9              # Distance between balls (center to center)
    row_height = 1.8                # Vertical distance between rows
    start_x = 3                     # X position where balls start
    
    # Calculate number of balls per fold
    balls_per_fold = n_datapoints // k
    
    # Total width of all balls
    total_width = n_datapoints * ball_spacing
    
    # =========================================================================
    # DRAW BACKGROUND
    # =========================================================================
    background = FancyBboxPatch(
        (start_x - 1, -0.5), 
        total_width + 1.5, 
        (k + 2) * row_height,
        boxstyle="round,pad=0.1,rounding_size=0.3",
        facecolor=background_color,
        edgecolor=frame_color,
        linewidth=2
    )
    ax.add_patch(background)
    
    # =========================================================================
    # FUNCTION TO DRAW A 3D-LIKE BALL
    # =========================================================================
    def draw_ball(ax, x, y, radius, color, alpha=1.0):
        """
        Draws a ball with 3D effect (gradient/shadow).
        """
        # Main circle
        circle = Circle((x, y), radius, 
                        facecolor=color, 
                        edgecolor='white',
                        linewidth=0.5,
                        alpha=alpha)
        ax.add_patch(circle)
        
        # Light reflection (small white circle at top left)
        reflection_x = x - radius * 0.3
        reflection_y = y + radius * 0.3
        reflection = Circle((reflection_x, reflection_y), radius * 0.2,
                         facecolor='white',
                         edgecolor='none',
                         alpha=0.6 * alpha)
        ax.add_patch(reflection)
        
        # Shadow (darker arc at bottom)
        from matplotlib.patches import Arc
        shadow = Arc((x, y), radius * 1.8, radius * 1.8,
                    angle=0, theta1=200, theta2=340,
                    color='black', alpha=0.15 * alpha, linewidth=radius * 8)
        ax.add_patch(shadow)
    
    # =========================================================================
    # FUNCTION TO DRAW TEXT BOX
    # =========================================================================
    def draw_text_box(ax, x, y, text, color=text_color, fontsize=11):
        """
        Draws a text box with frame.
        """
        bbox_props = dict(
            boxstyle="round,pad=0.3,rounding_size=0.2",
            facecolor='white',
            edgecolor=color,
            linewidth=1.5
        )
        ax.text(x, y, text, ha='center', va='center',
               fontsize=fontsize, color=color, fontweight='bold',
               bbox=bbox_props)
    
    # =========================================================================
    # DRAW HEADERS AND ARROWS
    # =========================================================================
    top_y = (k + 0.5) * row_height
    
    # "Test data" arrow and label (above first fold position)
    test_start_x = start_x + balls_per_fold * ball_spacing * 0.5
    draw_text_box(ax, start_x + balls_per_fold * ball_spacing / 2, top_y + 0.8, 
                   'Test data', color=text_color)
    
    # Arrow down from "Test data"
    ax.annotate('', xy=(start_x + balls_per_fold * ball_spacing / 2, top_y - 0.3),
                xytext=(start_x + balls_per_fold * ball_spacing / 2, top_y + 0.4),
                arrowprops=dict(arrowstyle='->', color=text_color, lw=2))
    
    # "Training data" arrow and label
    training_start_x = start_x + balls_per_fold * ball_spacing
    training_end_x = start_x + n_datapoints * ball_spacing
    training_mid_x = (training_start_x + training_end_x) / 2
    
    draw_text_box(ax, training_mid_x, top_y + 0.8, 'Training data', color=text_color)
    
    # Arrow for training data (horizontal with end arrows)
    ax.annotate('', xy=(training_end_x - 0.5, top_y - 0.3),
                xytext=(training_start_x + 0.5, top_y - 0.3),
                arrowprops=dict(arrowstyle='<->', color=text_color, lw=2))
    
    # =========================================================================
    # DRAW ITERATIONS (ROWS WITH BALLS)
    # =========================================================================
    for iteration in range(k):
        # Y position for this row (top row first)
        y = (k - iteration) * row_height
        
        # Iteration label
        if iteration < k - 1:
            iteration_text = f'Iteration {iteration + 1}'
        else:
            iteration_text = f'Iteration k={k}'
        
        draw_text_box(ax, 1.2, y, iteration_text, color=text_color, fontsize=10)
        
        # Arrow from text box to balls
        ax.annotate('', xy=(start_x - 0.8, y),
                    xytext=(2.2, y),
                    arrowprops=dict(arrowstyle='->', color=text_color, lw=1.5))
        
        # Calculate which balls are in the test fold for this iteration
        test_start_idx = iteration * balls_per_fold
        test_end_idx = test_start_idx + balls_per_fold
        
        # Draw all balls for this iteration
        for i in range(n_datapoints):
            x = start_x + i * ball_spacing
            
            # Choose color based on position (alternates between red and teal)
            if i % 2 == 0:
                base_color = color_red
                light_color = color_red_light
            else:
                base_color = color_teal
                light_color = color_teal_light
            
            # Use lighter color for test data
            if test_start_idx <= i < test_end_idx:
                ball_color = light_color
            else:
                ball_color = base_color
            
            draw_ball(ax, x, y, ball_radius, ball_color)
        
        # Draw frame around test fold
        frame_x = start_x + test_start_idx * ball_spacing - ball_radius - 0.15
        frame_width = balls_per_fold * ball_spacing + 0.1
        frame_y = y - ball_radius - 0.2
        frame_height = ball_radius * 2 + 0.4
        
        test_frame = FancyBboxPatch(
            (frame_x, frame_y), frame_width, frame_height,
            boxstyle="round,pad=0.02,rounding_size=0.1",
            facecolor='none',
            edgecolor=frame_color,
            linewidth=2.5
        )
        ax.add_patch(test_frame)
        
        # Add vertical dotted line after row 3 (for "...")
        if iteration == 2:  # After iteration 3
            for dot_y in [y - row_height * 0.3, y - row_height * 0.5, y - row_height * 0.7]:
                ax.plot(1.2, dot_y, 'o', color=text_color, markersize=4)
                for dot_x in [start_x + n_datapoints * ball_spacing / 3,
                             start_x + n_datapoints * ball_spacing * 2 / 3]:
                    ax.plot(dot_x, dot_y, 'o', color=text_color, markersize=3)
    
    # =========================================================================
    # DRAW "ALL DATA" ARROWS AND LABEL AT BOTTOM
    # =========================================================================
    bottom_y = 0.3
    
    # Horizontal arrow for "All data"
    ax.annotate('', xy=(start_x + n_datapoints * ball_spacing - 0.3, bottom_y),
                xytext=(start_x - 0.3, bottom_y),
                arrowprops=dict(arrowstyle='<->', color=text_color, lw=2))
    
    draw_text_box(ax, start_x + n_datapoints * ball_spacing / 2, bottom_y - 0.7, 
                   'All data', color=text_color)
    
    # =========================================================================
    # ADJUST AXES AND LAYOUT
    # =========================================================================
    ax.set_xlim(-0.5, start_x + n_datapoints * ball_spacing + 1)
    ax.set_ylim(-1.5, (k + 2) * row_height)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if save:
        filepath = FIGURE_DIR / filename
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figure saved: {filepath}")
    
    return fig, ax


def plot_confusion_matrix_explanation(figsize=(8, 6), save=False,
                                        filename="confusion_matrix_explanation.png"):
    """
    Visualizes the structure of a confusion matrix with explanations.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Colors
    tp_color = '#27AE60'   # Green (good)
    tn_color = '#27AE60'   # Green (good)
    fp_color = '#E74C3C'   # Red (error)
    fn_color = '#E74C3C'   # Red (error)
    
    # Draw 2x2 matrix
    colors = [[tn_color, fp_color], [fn_color, tp_color]]
    labels = [['True\nNegative\n(TN)', 'False\nPositive\n(FP)'],
              ['False\nNegative\n(FN)', 'True\nPositive\n(TP)']]
    
    for i in range(2):
        for j in range(2):
            rect = plt.Rectangle((j, 1-i), 1, 1,
                                 facecolor=colors[i][j],
                                 edgecolor='white',
                                 linewidth=3,
                                 alpha=0.7)
            ax.add_patch(rect)
            ax.text(j + 0.5, 1.5 - i, labels[i][j],
                   ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Axis labels
    ax.text(1, -0.15, 'Predicted', ha='center', va='top', fontsize=12, fontweight='bold')
    ax.text(0.5, -0.35, 'Negative', ha='center', va='top', fontsize=10)
    ax.text(1.5, -0.35, 'Positive', ha='center', va='top', fontsize=10)
    
    ax.text(-0.15, 1, 'Actual', ha='right', va='center', fontsize=12, 
            fontweight='bold', rotation=90)
    ax.text(-0.3, 1.5, 'Negative', ha='right', va='center', fontsize=10)
    ax.text(-0.3, 0.5, 'Positive', ha='right', va='center', fontsize=10)
    
    ax.set_xlim(-0.6, 2.5)
    ax.set_ylim(-0.6, 2.3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if save:
        filepath = FIGURE_DIR / filename
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figure saved: {filepath}")
    
    return fig, ax


def plot_sensitivity_specificity(figsize=(10, 14), save=False,
                                    filename="sensitivity_specificity.png"):
    """
    Visualizes sensitivity and specificity with a Venn-like diagram.
    
    The figure shows:
    - Left half (green): Relevant elements (actually positive/sick)
    - Right half (gray): Non-relevant elements (actually negative/healthy)
    - Oval in the middle: Selected elements (predicted positive)
    - Four regions: True positive (TP), False positive (FP), 
                    False negative (FN), True negative (TN)
    - Formulas for sensitivity and specificity at the bottom
    """
    from matplotlib.patches import Ellipse, Circle, FancyBboxPatch, Rectangle
    from matplotlib.lines import Line2D
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # =========================================================================
    # COLORS
    # =========================================================================
    green_light = '#C8E6C9'          # Light green (relevant background)
    green_dark = '#81C784'           # Darker green (TP region)
    gray_light = '#E0E0E0'           # Light gray (non-relevant background)
    red_light = '#FFCDD2'            # Light red/pink (FP region)
    text_color = '#333333'           # Dark text
    frame_color = '#666666'          # Gray frame
    
    # =========================================================================
    # DIMENSIONS
    # =========================================================================
    # Main rectangle
    rect_x, rect_y = 0, 4
    rect_width, rect_height = 10, 8
    
    # Ellipse (selected elements)
    ellipse_cx = rect_x + rect_width / 2
    ellipse_cy = rect_y + rect_height * 0.55
    ellipse_width = rect_width * 0.7
    ellipse_height = rect_height * 0.55
    
    # =========================================================================
    # DRAW BACKGROUND RECTANGLES (left: green, right: gray)
    # =========================================================================
    # Left half (green - actually positive)
    left_rect = FancyBboxPatch(
        (rect_x, rect_y), rect_width / 2, rect_height,
        boxstyle="round,pad=0,rounding_size=0.3",
        facecolor=green_light,
        edgecolor=frame_color,
        linewidth=2
    )
    ax.add_patch(left_rect)
    
    # Right half (gray - actually negative)
    right_rect = FancyBboxPatch(
        (rect_x + rect_width / 2, rect_y), rect_width / 2, rect_height,
        boxstyle="round,pad=0,rounding_size=0.3",
        facecolor=gray_light,
        edgecolor=frame_color,
        linewidth=2
    )
    ax.add_patch(right_rect)
    
    # Outer frame
    outer_frame = FancyBboxPatch(
        (rect_x, rect_y), rect_width, rect_height,
        boxstyle="round,pad=0,rounding_size=0.3",
        facecolor='none',
        edgecolor=frame_color,
        linewidth=2.5
    )
    ax.add_patch(outer_frame)
    
    # =========================================================================
    # DRAW ELLIPSE (SELECTED ELEMENTS) WITH TWO COLORS
    # =========================================================================
    # Generate ellipse points
    theta = np.linspace(0, 2*np.pi, 200)
    ellipse_x = ellipse_cx + (ellipse_width/2) * np.cos(theta)
    ellipse_y = ellipse_cy + (ellipse_height/2) * np.sin(theta)
    
    # Left half (green - true positives): theta from pi/2 to 3pi/2
    theta_left = np.linspace(np.pi/2, 3*np.pi/2, 100)
    x_left = ellipse_cx + (ellipse_width/2) * np.cos(theta_left)
    y_left = ellipse_cy + (ellipse_height/2) * np.sin(theta_left)
    # Close the shape
    x_left = np.append(x_left, x_left[0])
    y_left = np.append(y_left, y_left[0])
    ax.fill(x_left, y_left, color=green_dark, alpha=0.8)
    
    # Right half (red - false positives): theta from -pi/2 to pi/2
    theta_right = np.linspace(-np.pi/2, np.pi/2, 100)
    x_right = ellipse_cx + (ellipse_width/2) * np.cos(theta_right)
    y_right = ellipse_cy + (ellipse_height/2) * np.sin(theta_right)
    # Close the shape
    x_right = np.append(x_right, x_right[0])
    y_right = np.append(y_right, y_right[0])
    ax.fill(x_right, y_right, color=red_light, alpha=0.9)
    
    # Draw ellipse outline
    ax.plot(ellipse_x, ellipse_y, color=frame_color, linewidth=2)
    
    # =========================================================================
    # DRAW DATA POINTS (DOTS)
    # =========================================================================
    np.random.seed(42)  # For reproducibility
    
    def draw_filled_dot(x, y, radius=0.18):
        """Draw filled dot (actually positive)"""
        circle = Circle((x, y), radius, facecolor='#555555', edgecolor='#333333', linewidth=1)
        ax.add_patch(circle)
    
    def draw_empty_dot(x, y, radius=0.18):
        """Draw empty dot (actually negative)"""
        circle = Circle((x, y), radius, facecolor='white', edgecolor='#555555', linewidth=1.5)
        ax.add_patch(circle)
    
    # True positives (filled dots inside ellipse, left side)
    tp_positions = [(2.5, 9.5), (3.2, 8.5), (2.8, 7.5), (3.5, 8.0), (4.0, 9.0), (3.0, 8.8)]
    for x, y in tp_positions:
        draw_filled_dot(x, y)
    
    # False negatives (filled dots outside ellipse, left side)
    fn_positions = [(1.0, 10.5), (0.8, 9.0), (1.5, 7.0), (2.0, 5.5), (0.5, 6.5), 
                     (1.2, 11.0), (2.5, 5.0), (1.8, 10.8)]
    for x, y in fn_positions:
        draw_filled_dot(x, y)
    
    # False positives (empty dots inside ellipse, right side)
    fp_positions = [(6.0, 9.0), (6.5, 8.0), (7.0, 8.8), (5.8, 7.5)]
    for x, y in fp_positions:
        draw_empty_dot(x, y)
    
    # True negatives (empty dots outside ellipse, right side)
    tn_positions = [(8.0, 10.5), (9.0, 9.5), (8.5, 6.0), (9.5, 8.0), 
                     (8.2, 11.0), (9.2, 7.0), (7.5, 5.5), (9.0, 5.0)]
    for x, y in tn_positions:
        draw_empty_dot(x, y)
    
    # =========================================================================
    # LABELS FOR THE REGIONS
    # =========================================================================
    # Upper labels
    ax.text(rect_width / 4, rect_y + rect_height - 0.6, 'false negatives',
           ha='center', va='center', fontsize=14, fontstyle='italic', color=text_color)
    ax.text(3 * rect_width / 4, rect_y + rect_height - 0.6, 'true negatives',
           ha='center', va='center', fontsize=14, fontstyle='italic', color=text_color)
    
    # Labels inside ellipse
    ax.text(3.0, 8.2, 'true\npositives',
           ha='center', va='center', fontsize=14, fontstyle='italic', color=text_color)
    ax.text(6.5, 8.2, 'false\npositives',
           ha='center', va='center', fontsize=14, fontstyle='italic', color=text_color)
    
    # =========================================================================
    # HEADERS WITH BRACES
    # =========================================================================
    # "relevant elements" (top, above left half)
    brace_y_top = rect_y + rect_height + 0.3
    ax.plot([rect_x + 0.2, rect_x + 0.2], [brace_y_top, brace_y_top + 0.2], 'k-', lw=1.5)
    ax.plot([rect_x + 0.2, rect_x + rect_width/2 - 0.2], [brace_y_top + 0.2, brace_y_top + 0.2], 'k-', lw=1.5)
    ax.plot([rect_x + rect_width/2 - 0.2, rect_x + rect_width/2 - 0.2], [brace_y_top, brace_y_top + 0.2], 'k-', lw=1.5)
    ax.text(rect_width / 4, brace_y_top + 0.6, 'relevant elements',
           ha='center', va='bottom', fontsize=15, fontweight='bold', color=text_color)
    
    # "selected elements" (bottom, below ellipse)
    brace_y_bottom = rect_y - 0.3
    # Arrow down from ellipse to label
    ax.annotate('', xy=(ellipse_cx, brace_y_bottom - 0.5),
                xytext=(ellipse_cx, rect_y + 0.5),
                arrowprops=dict(arrowstyle='-', color='black', lw=1.5))
    ax.plot([ellipse_cx - 0.1, ellipse_cx + 0.1], [brace_y_bottom - 0.5, brace_y_bottom - 0.5], 'k-', lw=1.5)
    ax.text(ellipse_cx, brace_y_bottom - 0.9, 'selected elements',
           ha='center', va='top', fontsize=15, fontweight='bold', color=text_color)
    
    # =========================================================================
    # EXPLANATIONS AT BOTTOM
    # =========================================================================
    explanation_y = 1.5
    
    # Left explanation (Sensitivity)
    ax.text(2.5, explanation_y + 0.8, 'How many relevant\nelements are selected?',
           ha='center', va='top', fontsize=13, color=text_color, linespacing=1.3)
    ax.text(2.5, explanation_y - 0.3, 'E.g. How many sick\nare correctly identified\nas sick.',
           ha='center', va='top', fontsize=11, color='#666666', fontstyle='italic', linespacing=1.3)
    
    # Right explanation (Specificity)
    ax.text(7.5, explanation_y + 0.8, 'How many non-selected\nelements are actually negative?',
           ha='center', va='top', fontsize=13, color=text_color, linespacing=1.3)
    ax.text(7.5, explanation_y - 0.3, 'E.g. How many healthy\nare correctly identified\nas healthy.',
           ha='center', va='top', fontsize=11, color='#666666', fontstyle='italic', linespacing=1.3)
    
    # =========================================================================
    # FORMULAS FOR SENSITIVITY AND SPECIFICITY
    # =========================================================================
    formula_y = -1.0
    
    # Sensitivity
    ax.text(2.5, formula_y, 'Sensitivity =',
           ha='right', va='center', fontsize=16, fontweight='bold', color=text_color)
    
    # Fraction bar and mini-diagrams for sensitivity
    # Numerator: green half of circle (TP)
    sens_numerator_x = 3.3
    from matplotlib.patches import Wedge
    
    # Green half-circle (right side = TP in selected)
    wedge_tp = Wedge((sens_numerator_x, formula_y + 0.35), 0.25, -90, 90, 
                     facecolor=green_dark, edgecolor=frame_color, linewidth=1)
    ax.add_patch(wedge_tp)
    # White half-circle (left side)
    wedge_white1 = Wedge((sens_numerator_x, formula_y + 0.35), 0.25, 90, 270,
                         facecolor='white', edgecolor=frame_color, linewidth=1)
    ax.add_patch(wedge_white1)
    
    # Fraction bar
    ax.plot([sens_numerator_x - 0.4, sens_numerator_x + 0.4], [formula_y, formula_y], 'k-', lw=2)
    
    # Denominator: entire green circle (all positives)
    circle_all_pos = Circle((sens_numerator_x, formula_y - 0.35), 0.25,
                            facecolor=green_dark, edgecolor=frame_color, linewidth=1)
    ax.add_patch(circle_all_pos)
    
    # Specificity
    ax.text(7.0, formula_y, 'Specificity =',
           ha='right', va='center', fontsize=16, fontweight='bold', color=text_color)
    
    # Mini-diagrams for specificity
    spec_numerator_x = 7.8
    
    # Numerator: gray half-circle (TN - non-selected that are negative)
    wedge_tn = Wedge((spec_numerator_x, formula_y + 0.35), 0.25, 90, 270,
                     facecolor=gray_light, edgecolor=frame_color, linewidth=1)
    ax.add_patch(wedge_tn)
    # White half-circle (right side)
    wedge_white2 = Wedge((spec_numerator_x, formula_y + 0.35), 0.25, -90, 90,
                         facecolor='white', edgecolor=frame_color, linewidth=1)
    ax.add_patch(wedge_white2)
    
    # Fraction bar
    ax.plot([spec_numerator_x - 0.4, spec_numerator_x + 0.4], [formula_y, formula_y], 'k-', lw=2)
    
    # Denominator: gray + red (all negatives) - show as rectangle with two colors
    from matplotlib.patches import Rectangle
    # Gray half
    rect_neg = Rectangle((spec_numerator_x - 0.3, formula_y - 0.55), 0.3, 0.4,
                         facecolor=gray_light, edgecolor=frame_color, linewidth=1)
    ax.add_patch(rect_neg)
    # Red half  
    rect_fp = Rectangle((spec_numerator_x, formula_y - 0.55), 0.3, 0.4,
                        facecolor=red_light, edgecolor=frame_color, linewidth=1)
    ax.add_patch(rect_fp)
    
    # =========================================================================
    # ADJUST AXES
    # =========================================================================
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2.5, 14)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if save:
        filepath = FIGURE_DIR / filename
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figure saved: {filepath}")
    
    return fig, ax


def generate_all_figures():
    """
    Generates and saves all figures to the figures/ directory.
    Run this function to update all figures.
    """
    print("Generating figures for BMED365 notebooks...")
    print("=" * 50)
    
    # Simple training/test set split (Figure 3)
    fig, ax = plot_training_test_split(save=True)
    plt.close(fig)
    
    # Dataset split with validation (Figure 4)
    fig, ax = plot_dataset_split(save=True)
    plt.close(fig)
    
    # K-fold cross-validation (simple version)
    fig, ax = plot_kfold_cross_validation(save=True)
    plt.close(fig)
    
    # K-fold cross-validation with balls (detailed version)
    fig, ax = plot_kfold_cross_validation_balls(save=True)
    plt.close(fig)
    
    # Confusion matrix explanation
    fig, ax = plot_confusion_matrix_explanation(save=True)
    plt.close(fig)
    
    # Sensitivity and specificity
    fig, ax = plot_sensitivity_specificity(save=True)
    plt.close(fig)
    
    print("=" * 50)
    print("✓ All figures generated!")


if __name__ == "__main__":
    generate_all_figures()
