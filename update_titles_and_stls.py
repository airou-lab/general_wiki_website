import os
import re

# 1. Clean titles mapping dictionary
CLEAN_TITLES = {
    # Lectures
    "CS4733_5733_F2025_3D_reconstruction_and_review.pdf": "3D Reconstruction and Review",
    "CS4733_5733_F2025_conclusion.pdf": "Conclusion",
    "CS4733_5733_F25_Estimation.pdf": "Estimation",
    "CS4733_5733_F25_Quadrotor_Control_Planning.pdf": "Quadrotor Control & Planning",
    "CS4733_5733_F25_W10_loop_closure_place_recognition.pdf": "Lecture 10 - Loop Closure & Place Recognition",
    "CS4733_5733_F25_W14_Quadrotor_Dynamics.pdf": "Lecture 14 - Quadrotor Dynamics",
    "CS4733_5733_F25_W4_5_2view_GeometryII.pdf": "Lectures 4-5 - 2-View Geometry II",
    "CS4733_5733_F25_W6_7_Ransac_correspondance.pdf": "Lectures 6-7 - RANSAC Correspondence",
    "CS4733_5733_F25_W8_9_Estimation.pdf": "Lectures 8-9 - Estimation",
    "CS4733_5733_F25__lecture5_Image_Formation_Feature_Detection.pdf": "Lecture 5 - Image Formation & Feature Detection",
    "CS4733_5733_F25_lecture1_Introduction.pdf": "Lecture 1 - Introduction",
    "CS4733_5733_F25_lecture1_Introduction.pptx": "Lecture 1 - Introduction (PPTX)",
    "CS4733_5733_Object_detection_3D_construction.pdf": "Object Detection & 3D Reconstruction",
    "CS4733_5733_W11_12_13_Pose_Graph_Optimization.pdf": "Lectures 11-13 - Pose Graph Optimization",
    "CS4733_5733_beyond_cameras.pdf": "Beyond Cameras",
    "CS4733_CS5733_F24_W1_lecture2_Coordinate_frame_Geometry.pdf": "Lecture 2 - Coordinate Frame Geometry",
    "CS4733_CS5733_F25_lecture3_3DGeometry.pdf": "Lecture 3 - 3D Geometry",
    "CS4733_CS5733_F25_lecture3_and_4_3DGeometry.pdf": "Lectures 3-4 - 3D Geometry",
    "Eight_Point_Algorithm_Explanation.pdf": "Eight-Point Algorithm Explanation",
    "Geometric_controller_steps.pdf": "Geometric Controller Steps",
    "PRO-Lecture.pdf": "PRO Lecture",

    # Misc
    "CS4733_5733_Fall2025_Syllabus.pdf": "Course Syllabus",
    "math_basics.pdf": "Math Basics",
    "quiz_sol_Pose_graph.pdf": "Quiz Solution - Pose Graph",

    # Final Project + exam
    "CS4733_5733_F25_final_exam.pdf": "Final Exam",
    "CS5733_final_project_presentation_template.pptx": "Final Project Presentation Template",
    "CS5733_final_project_proposal_template.docx": "Final Project Proposal Template",

    # Notes
    "02-03-basic3Dgeometry-notes.pdf": "02-03 - Basic 3D Geometry Notes",
    "06-Control1-notes.pdf": "06 - Control 1 Notes",
    "06-Control2-notes.pdf": "06 - Control 2 Notes (Part 1)",
    "07-Control2-notes.pdf": "07 - Control 2 Notes (Part 2)",
    "09-TrajectoryOptimization1-notes.pdf": "09 - Trajectory Optimization 1 Notes",
    "10-TrajectoryOptimization2-notes.pdf": "10 - Trajectory Optimization 2 Notes",
    "11-ImageFormation-notes.pdf": "11 - Image Formation Notes",
    "12-13-featureDetectionAndTracking-notes.pdf": "12-13 - Feature Detection & Tracking Notes",
    "14-2viewGeometry-notes.pdf": "14 - 2-View Geometry Notes",
    "15-RANSAC-notes (2).pdf": "15 - RANSAC Notes",
    "16-optimizationAndEstimation-notes (2).pdf": "16 - Optimization & Estimation Notes (Part 1)",
    "16-optimizationAndEstimation-notes.pdf": "16 - Optimization & Estimation Notes (Part 2)",
    "17-18-NonLinearLeastSquares-notes.pdf": "17-18 - Non-Linear Least Squares Notes",
    "18-19-OptimizationOnManifold-notes.pdf": "18-19 - Optimization on Manifold Notes",
    "23-SLAM1-formulationsAndSparsity-notes (2).pdf": "23 - SLAM 1 Formulations & Sparsity Notes (Part 1)",
    "23-SLAM1-formulationsAndSparsity-notes.pdf": "23 - SLAM 1 Formulations & Sparsity Notes (Part 2)",
    "Control1-notes.pdf": "Control 1 Notes",
}

def clean_name_fallback(filename):
    name = filename
    for ext in [".pdf", ".pptx", ".ppt", ".docx", ".STL", ".stl"]:
        if name.endswith(ext):
            name = name[:-len(ext)]
    name = re.sub(r'^CS4733_CS5733_F\d+_', '', name)
    name = re.sub(r'^CS4733_5733_F\d+__?', '', name)
    name = re.sub(r'^CS4733_5733_', '', name)
    name = re.sub(r'^CS5733_', '', name)
    name = name.replace("_", " ").strip()
    return name

# --- STEP 1: Update Viewer Markdown files with Clean Titles ---
base_vnav = "content/SP2026-VNAV-CourseContent"
for root, dirs, files in os.walk(base_vnav):
    for file in files:
        if not file.endswith("_viewer.md"):
            continue
        
        orig_file = file[:-len("_viewer.md")]
        clean_title = CLEAN_TITLES.get(orig_file, clean_name_fallback(orig_file))
        
        filepath = os.path.join(root, file)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Update title frontmatter and H1 heading
        content = re.sub(r'^---\ntitle: .*?\n---', f'---\ntitle: "{clean_title}"\n---', content, flags=re.MULTILINE)
        content = re.sub(r'# .*?\n', f'# {clean_title}\n', content, count=1)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated viewer title: {filepath} -> {clean_title}")

# --- STEP 2: Update index.md files for Course Content ---
folders_to_update = ["lectures", "notes", " misc", "Final Project + exam"]
for folder in folders_to_update:
    folder_path = os.path.join(base_vnav, folder)
    index_path = os.path.join(folder_path, "index.md")
    if not os.path.exists(index_path):
        continue
        
    with open(index_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    new_lines = []
    for line in lines:
        m = re.match(r'^## (.*)', line)
        if m:
            raw_title = m.group(1).strip()
            clean_title = CLEAN_TITLES.get(raw_title, clean_name_fallback(raw_title))
            new_lines.append(f"## {clean_title}\n")
        else:
            new_lines.append(line)
            
    with open(index_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Updated index: {index_path}")

# --- STEP 3: Create STL pages in content/archived_material/lionn/stl ---
stl_dir = "content/archived_material/lionn/stl"
stl_files = [
    ("Casing Pin.STL", "casing-pin.STL", "Casing Pin"),
    ("Couple Base.STL", "couple-base.STL", "Couple Base"),
    ("Couple.STL", "couple.STL", "Couple"),
    ("Landing Gear.STL", "landing-gear.STL", "Landing Gear"),
    ("Pin for Camera (no Camera).STL", "pin-for-camera-(no-camera).STL", "Pin for Camera (No Camera)"),
    ("Pin for Camera.STL", "pin-for-camera.STL", "Pin for Camera"),
    ("Platform for Camera Pin.STL", "platform-for-camera-pin.STL", "Platform for Camera Pin"),
    ("AIROU-Drone-STLs.zip", "airou-drone-stls.zip", "All Drone STLs (ZIP Package)")
]

# Create individual viewer/download pages
for orig_name, slug_asset, display_title in stl_files:
    page_name = orig_name + "_viewer.md"
    page_path = os.path.join(stl_dir, page_name)
    asset_url = f"/archived_material/lionn/stl/{slug_asset}"
    
    is_zip = orig_name.endswith(".zip")
    icon = "📦" if is_zip else "📐"
    
    md_content = f"""---
title: "{display_title}"
---

# {icon} {display_title}

Click the button below to download the **{orig_name}** file:

<p style="margin: 30px 0;">
  <a id="download-btn" href="{asset_url}" download="{orig_name}" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 24px; background-color: var(--secondary); color: var(--light); text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 1.1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.15);">
    📥 Download {orig_name}
  </a>
</p>

<script>
  // Trigger automatic download when visiting this page
  (function() {{
    const btn = document.getElementById('download-btn');
    if (btn) {{
      btn.click();
    }}
  }})();
</script>
"""
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Created STL page: {page_path}")

# Create index.md for STL folder
stl_index_path = os.path.join(stl_dir, "index.md")
stl_index_content = """---
title: "3D Printable STL Files"
---

# 3D Printable STL Files

This section contains 3D printable STL models and hardware components for the AIROU drone.

## 📦 Complete Package
- [**All Drone STLs (ZIP Package)**](./AIROU-Drone-STLs.zip_viewer) — Full archive containing all components.

## 📐 Individual STL Models
- [Casing Pin](./Casing%20Pin.STL_viewer)
- [Couple Base](./Couple%20Base.STL_viewer)
- [Couple](./Couple.STL_viewer)
- [Landing Gear](./Landing%20Gear.STL_viewer)
- [Pin for Camera (No Camera)](./Pin%20for%20Camera%20(no%20Camera).STL_viewer)
- [Pin for Camera](./Pin%20for%20Camera.STL_viewer)
- [Platform for Camera Pin](./Platform%20for%20Camera%20Pin.STL_viewer)
"""

with open(stl_index_path, "w", encoding="utf-8") as f:
    f.write(stl_index_content)
print(f"Created STL index: {stl_index_path}")
