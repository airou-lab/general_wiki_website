import os
import re

# ==========================================
# 1. LABS CONFIGURATION
# ==========================================
LABS_INFO = [
    {
        "filename": "Lab 1 - Exercises.md",
        "title": "Lab 1: Git, Environment Setup & Shells",
        "related": [
            "[[CS4733_5733_F25_lecture1_Introduction.pdf_viewer|Lecture 1 - Introduction]]",
            "[[CS4733_5733_Fall2025_Syllabus.pdf_viewer|Course Syllabus]]"
        ],
        "prev": None,
        "next": ("Lab 2 - Exercises.md", "Lab 2: ROS 2 Basics, Coordinate Frames & TF")
    },
    {
        "filename": "Lab 2 - Exercises.md",
        "title": "Lab 2: ROS 2 Basics, Coordinate Frames & TF",
        "related": [
            "[[CS4733_CS5733_F24_W1_lecture2_Coordinate_frame_Geometry.pdf_viewer|Lecture 2 - Coordinate Frame Geometry]]",
            "[[CS4733_CS5733_F25_lecture3_3DGeometry.pdf_viewer|Lecture 3 - 3D Geometry]]",
            "[[02-03-basic3Dgeometry-notes.pdf_viewer|02-03 Basic 3D Geometry Notes]]"
        ],
        "prev": ("Lab 1 - Exercises.md", "Lab 1: Git & Environment Setup"),
        "next": ("Lab 3 - Exercises.md", "Lab 3: Perspective Projection & Harris Corners")
    },
    {
        "filename": "Lab 3 - Exercises.md",
        "title": "Lab 3: Perspective Projection, Vanishing Points & Harris Corners",
        "related": [
            "[[CS4733_5733_F25__lecture5_Image_Formation_Feature_Detection.pdf_viewer|Lecture 5 - Image Formation & Feature Detection]]",
            "[[CS4733_CS5733_F25_lecture3_and_4_3DGeometry.pdf_viewer|Lectures 3-4 - 3D Geometry]]",
            "[[11-ImageFormation-notes.pdf_viewer|11 Image Formation Notes]]",
            "[[12-13-featureDetectionAndTracking-notes.pdf_viewer|12-13 Feature Detection & Tracking Notes]]"
        ],
        "prev": ("Lab 2 - Exercises.md", "Lab 2: ROS 2 Basics & TF"),
        "next": ("Lab 4 - Exercises.md", "Lab 4: Relative Pose & 5-Point Algorithm")
    },
    {
        "filename": "Lab 4 - Exercises.md",
        "title": "Lab 4: Relative Pose Estimation & 5-Point Algorithm",
        "related": [
            "[[CS4733_5733_F25_W4_5_2view_GeometryII.pdf_viewer|Lectures 4-5 - 2-View Geometry II]]",
            "[[CS4733_5733_F25_W6_7_Ransac_correspondance.pdf_viewer|Lectures 6-7 - RANSAC Correspondence]]",
            "[[Eight_Point_Algorithm_Explanation.pdf_viewer|Eight-Point Algorithm Explanation]]",
            "[[14-2viewGeometry-notes.pdf_viewer|14 2-View Geometry Notes]]",
            "[[15-RANSAC-notes (2).pdf_viewer|15 RANSAC Notes]]"
        ],
        "prev": ("Lab 3 - Exercises.md", "Lab 3: Perspective Projection & Features"),
        "next": ("Lab 5 - Exercises.md", "Lab 5: Bundle Adjustment & Factor Graphs")
    },
    {
        "filename": "Lab 5 - Exercises.md",
        "title": "Lab 5: Bundle Adjustment & Factor Graphs",
        "related": [
            "[[CS4733_5733_F25_W8_9_Estimation.pdf_viewer|Lectures 8-9 - Estimation]]",
            "[[CS4733_5733_W11_12_13_Pose_Graph_Optimization.pdf_viewer|Lectures 11-13 - Pose Graph Optimization]]",
            "[[CS4733_5733_F2025_3D_reconstruction_and_review.pdf_viewer|3D Reconstruction and Review]]",
            "[[16-optimizationAndEstimation-notes (2).pdf_viewer|16 Optimization & Estimation Notes]]",
            "[[17-18-NonLinearLeastSquares-notes.pdf_viewer|17-18 Non-Linear Least Squares Notes]]",
            "[[18-19-OptimizationOnManifold-notes.pdf_viewer|18-19 Optimization on Manifold Notes]]"
        ],
        "prev": ("Lab 4 - Exercises.md", "Lab 4: Relative Pose Estimation"),
        "next": ("Lab 6 - Exercises.md", "Lab 6: Object Detection & YOLO")
    },
    {
        "filename": "Lab 6 - Exercises.md",
        "title": "Lab 6: Object Detection & YOLO",
        "related": [
            "[[CS4733_5733_Object_detection_3D_construction.pdf_viewer|Object Detection & 3D Reconstruction]]",
            "[[CS4733_5733_beyond_cameras.pdf_viewer|Beyond Cameras]]"
        ],
        "prev": ("Lab 5 - Exercises.md", "Lab 5: Bundle Adjustment"),
        "next": ("Lab 7 - Exercises.md", "Lab 7: Quadrotor Control & Trajectory Tracking")
    },
    {
        "filename": "Lab 7 - Exercises.md",
        "title": "Lab 7: Quadrotor Control & Trajectory Tracking",
        "related": [
            "[[CS4733_5733_F25_W14_Quadrotor_Dynamics.pdf_viewer|Lecture 14 - Quadrotor Dynamics]]",
            "[[CS4733_5733_F25_Quadrotor_Control_Planning.pdf_viewer|Quadrotor Control & Planning]]",
            "[[Geometric_controller_steps.pdf_viewer|Geometric Controller Steps]]",
            "[[06-Control1-notes.pdf_viewer|06 Control 1 Notes]]",
            "[[09-TrajectoryOptimization1-notes.pdf_viewer|09 Trajectory Optimization 1 Notes]]"
        ],
        "prev": ("Lab 6 - Exercises.md", "Lab 6: Object Detection"),
        "next": ("Final Project + exam/index", "Final Project & Exam")
    }
]

labs_dir = "content/SP2026-VNAV-CourseContent/labs"

for item in LABS_INFO:
    lab_path = os.path.join(labs_dir, item["filename"])
    if not os.path.exists(lab_path):
        print(f"Warning: {lab_path} not found")
        continue
        
    with open(lab_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Clean out existing related block if present
    content = re.sub(r'> \[!info\] Related Lectures & Notes\n(?:> - .*\n)*\n?', '', content)
    # Clean out existing navigation block at the end if present
    content = re.sub(r'\n---\n(?:\*\*Previous\*\*.*|\*\*Next Lab\*\*.*|\*\*Next\*\*.*)\n*$', '', content)

    # 2. Build Related Lectures block
    related_bullets = "\n".join([f"> - {r}" for r in item["related"]])
    related_block = f"> [!info] Related Lectures & Notes\n{related_bullets}\n\n"

    # Insert Related Lectures block after the # Heading
    if re.search(r'^# .*\n', content, flags=re.MULTILINE):
        content = re.sub(r'(^# .*\n+)', r'\1' + related_block, content, count=1, flags=re.MULTILINE)
    else:
        content = related_block + content

    # 3. Build Bottom Navigation
    nav_parts = []
    if item["prev"]:
        prev_file, prev_label = item["prev"]
        prev_link = prev_file.replace(".md", "")
        nav_parts.append(f"**Previous**: [[{prev_link}|⬅ {prev_label}]]")
    if item["next"]:
        next_file, next_label = item["next"]
        next_link = next_file.replace(".md", "")
        nav_parts.append(f"**Next**: [[{next_link}|{next_label} ➔]]")

    nav_line = " | ".join(nav_parts)
    bottom_nav = f"\n\n---\n\n{nav_line}\n"
    content = content.rstrip() + bottom_nav

    with open(lab_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated Lab: {lab_path}")


# ==========================================
# 2. LECTURES SEQUENTIAL NAVIGATION
# ==========================================
LECTURE_SEQUENCE = [
    ("CS4733_5733_F25_lecture1_Introduction.pdf_viewer.md", "Lecture 1 - Introduction", "Lab 1 - Exercises", "Lab 1: Git & Environment Setup"),
    ("CS4733_CS5733_F24_W1_lecture2_Coordinate_frame_Geometry.pdf_viewer.md", "Lecture 2 - Coordinate Frame Geometry", "Lab 2 - Exercises", "Lab 2: ROS 2 Basics & TF"),
    ("CS4733_CS5733_F25_lecture3_3DGeometry.pdf_viewer.md", "Lecture 3 - 3D Geometry", "Lab 2 - Exercises", "Lab 2: ROS 2 Basics & TF"),
    ("CS4733_CS5733_F25_lecture3_and_4_3DGeometry.pdf_viewer.md", "Lectures 3-4 - 3D Geometry", "Lab 3 - Exercises", "Lab 3: Perspective Projection & Features"),
    ("CS4733_5733_F25_W4_5_2view_GeometryII.pdf_viewer.md", "Lectures 4-5 - 2-View Geometry II", "Lab 4 - Exercises", "Lab 4: Relative Pose Estimation"),
    ("CS4733_5733_F25__lecture5_Image_Formation_Feature_Detection.pdf_viewer.md", "Lecture 5 - Image Formation & Feature Detection", "Lab 3 - Exercises", "Lab 3: Perspective Projection & Features"),
    ("CS4733_5733_F25_W6_7_Ransac_correspondance.pdf_viewer.md", "Lectures 6-7 - RANSAC Correspondence", "Lab 4 - Exercises", "Lab 4: Relative Pose & 5-Point"),
    ("Eight_Point_Algorithm_Explanation.pdf_viewer.md", "Eight-Point Algorithm Explanation", "Lab 4 - Exercises", "Lab 4: Relative Pose & 5-Point"),
    ("CS4733_5733_F25_W8_9_Estimation.pdf_viewer.md", "Lectures 8-9 - Estimation", "Lab 5 - Exercises", "Lab 5: Bundle Adjustment & Factor Graphs"),
    ("CS4733_5733_F25_Estimation.pdf_viewer.md", "Estimation", "Lab 5 - Exercises", "Lab 5: Bundle Adjustment & Factor Graphs"),
    ("CS4733_5733_F25_W10_loop_closure_place_recognition.pdf_viewer.md", "Lecture 10 - Loop Closure & Place Recognition", None, None),
    ("CS4733_5733_W11_12_13_Pose_Graph_Optimization.pdf_viewer.md", "Lectures 11-13 - Pose Graph Optimization", "Lab 5 - Exercises", "Lab 5: Bundle Adjustment & Factor Graphs"),
    ("CS4733_5733_Object_detection_3D_construction.pdf_viewer.md", "Object Detection & 3D Reconstruction", "Lab 6 - Exercises", "Lab 6: Object Detection & YOLO"),
    ("CS4733_5733_beyond_cameras.pdf_viewer.md", "Beyond Cameras", "Lab 6 - Exercises", "Lab 6: Object Detection & YOLO"),
    ("CS4733_5733_F2025_3D_reconstruction_and_review.pdf_viewer.md", "3D Reconstruction and Review", "Lab 5 - Exercises", "Lab 5: Bundle Adjustment"),
    ("CS4733_5733_F25_W14_Quadrotor_Dynamics.pdf_viewer.md", "Lecture 14 - Quadrotor Dynamics", "Lab 7 - Exercises", "Lab 7: Quadrotor Control & Trajectory Tracking"),
    ("CS4733_5733_F25_Quadrotor_Control_Planning.pdf_viewer.md", "Quadrotor Control & Planning", "Lab 7 - Exercises", "Lab 7: Quadrotor Control & Trajectory Tracking"),
    ("Geometric_controller_steps.pdf_viewer.md", "Geometric Controller Steps", "Lab 7 - Exercises", "Lab 7: Quadrotor Control & Trajectory Tracking"),
    ("PRO-Lecture.pdf_viewer.md", "PRO Lecture", None, None),
    ("CS4733_5733_F2025_conclusion.pdf_viewer.md", "Conclusion", None, None),
]

lectures_dir = "content/SP2026-VNAV-CourseContent/lectures"

for i, (filename, title, lab_link, lab_title) in enumerate(LECTURE_SEQUENCE):
    lec_path = os.path.join(lectures_dir, filename)
    if not os.path.exists(lec_path):
        print(f"Warning: {lec_path} not found")
        continue

    with open(lec_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean existing bottom navigation
    content = re.sub(r'\n---\n(?:\*\*Previous\*\*.*|\*\*Next Lecture\*\*.*|\*\*Next\*\*.*|\*\*Related Lab\*\*.*)\n*$', '', content)

    # Previous and Next lectures
    nav_parts = []
    if i > 0:
        prev_file, prev_title, _, _ = LECTURE_SEQUENCE[i-1]
        prev_link = prev_file.replace(".md", "")
        nav_parts.append(f"**Previous**: [[{prev_link}|⬅ {prev_title}]]")
    
    if i < len(LECTURE_SEQUENCE) - 1:
        next_file, next_title, _, _ = LECTURE_SEQUENCE[i+1]
        next_link = next_file.replace(".md", "")
        nav_parts.append(f"**Next Lecture**: [[{next_link}|{next_title} ➔]]")
    else:
        nav_parts.append(f"**Next**: [[Final Project + exam/index|Final Project & Exam ➔]]")

    nav_line = " | ".join(nav_parts)

    related_lab_line = ""
    if lab_link:
        related_lab_line = f"\n**Related Lab**: [[{lab_link}|{lab_title}]]\n\n"

    bottom_nav = f"\n\n---\n{related_lab_line}\n{nav_line}\n"
    content = content.rstrip() + bottom_nav

    with open(lec_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated Lecture: {lec_path}")

# Also update PPTX viewer for lecture 1
pptx_path = os.path.join(lectures_dir, "CS4733_5733_F25_lecture1_Introduction.pptx_viewer.md")
if os.path.exists(pptx_path):
    with open(pptx_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r'\n---\n(?:\*\*Previous\*\*.*|\*\*Next Lecture\*\*.*|\*\*Next\*\*.*|\*\*Related Lab\*\*.*)\n*$', '', content)
    bottom_nav = "\n\n---\n\n**Related Lab**: [[Lab 1 - Exercises|Lab 1: Git & Environment Setup]]\n\n**Next Lecture**: [[CS4733_CS5733_F24_W1_lecture2_Coordinate_frame_Geometry.pdf_viewer|Lecture 2 - Coordinate Frame Geometry ➔]]\n"
    content = content.rstrip() + bottom_nav
    with open(pptx_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated PPTX Lecture: {pptx_path}")

print("Successfully updated all labs and lecture files!")
