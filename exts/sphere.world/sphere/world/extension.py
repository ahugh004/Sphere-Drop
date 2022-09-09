import asyncio
import omni.ext
import omni.ui as ui
import omni.kit.commands
from pxr import Sdf, Gf
import omni.physx
import omni.usd

# """
# Extension allows the user, brand new user even, the instant gratification of painting and dropping objects in stage
# This Extension allows the user to rapidly create spheres, apply materials and physics gravity drop.
# Rest button allows user to reset and repaint new MDL on spheres for different looks
# Physics selections are preset (no user input required)
# Spheres are slightly misaligned on each stack so cascade isnt perfectly linear
# Plane is slightly tilted to allow spheres to continue to move after impact
# """


class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[sphere.world] MyExtension startup")

        self._window = ui.Window("My Window", width=300, height=300)
        self._usd_context = omni.usd.get_context()
        with self._window.frame:
            with ui.VStack():

                ui.Label("Sphere Drop Physics", alignment=ui.Alignment.CENTER)

                # from tkinter import *
                # window = Tk()
                # entry = Entry()
                # entry.config(font=("ink free", 50))
                # entry.config(bg="#111111")
                # nvidia_green = "#00FF00"
                # entry.config(fg=nvidia_green)
                # entry.insert(0, "Input Quantity for Sphere Array")
                # entry.pack()
                # window.mainloop()

                def on_click():
                    print("You Clicked It!")

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="DistantLight",
                        attributes={"angle": 1.0, "intensity": 3000},
                        select_new_prim=False,
                    )

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-50, -50, -50), (50, 50, 50)],
                        },
                        select_new_prim=False,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere"),
                        new_translation=Gf.Vec3d(0.0, 50.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(-200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-100, -100, -100), (100, 100, 100)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_01"),
                        new_translation=Gf.Vec3d(100.0, 50.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )
                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-100, -100, -100), (100, 100, 100)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_02"),
                        new_translation=Gf.Vec3d(200.0, 50.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )
                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-100, -100, -100), (100, 100, 100)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_03"),
                        new_translation=Gf.Vec3d(300, 50.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-50, -50, -50), (50, 50, 50)],
                        },
                        select_new_prim=False,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_04"),
                        new_translation=Gf.Vec3d(400.0, 50.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(-200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-100, -100, -100), (100, 100, 100)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_05"),
                        new_translation=Gf.Vec3d(0.5, 150.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )
                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-100, -100, -100), (100, 100, 100)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_06"),
                        new_translation=Gf.Vec3d(90, 150.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )
                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-100, -100, -100), (100, 100, 100)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_07"),
                        new_translation=Gf.Vec3d(205, 150.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-50, -50, -50), (50, 50, 50)],
                        },
                        select_new_prim=False,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_08"),
                        new_translation=Gf.Vec3d(295, 150.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(-200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-100, -100, -100), (100, 100, 100)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_09"),
                        new_translation=Gf.Vec3d(405, 150.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(200, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )
                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-100, -100, -100), (100, 100, 100)],
                        },
                        select_new_prim=True,
                    )
                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_10"),
                        new_translation=Gf.Vec3d(0.0, 250.0, 0.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(0, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )
                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-100, -100, -100), (100, 100, 100)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_11"),
                        new_translation=Gf.Vec3d(100, 250.0, -1.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(0, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )
                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-50, -50, -50), (50, 50, 50)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_12"),
                        new_translation=Gf.Vec3d(200, 250.0, 1.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(0, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-50, -50, -50), (50, 50, 50)],
                        },
                        select_new_prim=False,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_13"),
                        new_translation=Gf.Vec3d(300, 250.0, 1.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(0, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="Sphere",
                        attributes={
                            "radius": 25,
                            "extent": [(-50, -50, -50), (50, 50, 50)],
                        },
                        select_new_prim=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Sphere_14"),
                        new_translation=Gf.Vec3d(400, 250.0, -1.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(0, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(1.0, 1.0, 1.0),
                    )
                    omni.kit.commands.execute("CreateMeshPrimWithDefaultXform", prim_type="Plane")

                    omni.kit.commands.execute(
                        "ChangeProperty",
                        prop_path=Sdf.Path("/World/Plane.xformOp:scale"),
                        value=Gf.Vec3d(10.0, 10.0, 10.0),
                        prev=Gf.Vec3d(100.0, 100.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Plane"),
                        new_translation=Gf.Vec3d(150, 0.0, -150.0),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(10.0, 10.0, 10.0),
                        old_translation=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(10.0, 10.0, 10.0),
                    )

                    # inserted USD scene here

                    omni.kit.commands.execute(
                        "CreateReferenceCommand",
                        usd_context=omni.usd.get_context(),
                        path_to="/World/Attic_NVIDIA",
                        asset_path="omniverse://localhost/NVIDIA/Samples/OldAttic/Attic_NVIDIA.usd",
                        instanceable=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Attic_NVIDIA"),
                        new_translation=Gf.Vec3d(941.0839518762848, -3.05176e-05, 377.13446632390037),
                        new_rotation_euler=Gf.Vec3f(0, -90.0, -90.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3d(941.0839518762881, -3.05176e-05, 495.8731492201166),
                        old_rotation_euler=Gf.Vec3f(0.0, -90.0, -90.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "SelectPrimsCommand",
                        old_selected_paths=["/World/Attic_NVIDIA"],
                        new_selected_paths=["/World/Attic_NVIDIA/Geometry/Ball/ball"],
                        expand_in_stage=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Attic_NVIDIA/Geometry/Ball/ball"),
                        new_translation=Gf.Vec3f(56.8, 102.7, 49.3),
                        new_rotation_euler=Gf.Vec3d(0.0, -0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3f(24.664337158203125, 84.91767120361328, 25.34389877319336),
                        old_rotation_euler=Gf.Vec3d(0.0, -0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                    )

                    omni.kit.commands.execute(
                        "SelectPrimsCommand",
                        old_selected_paths=["/World/Attic_NVIDIA/Geometry/Ball/ball"],
                        new_selected_paths=["/World/Attic_NVIDIA/Geometry/Bear/bear"],
                        expand_in_stage=True,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/Attic_NVIDIA/Geometry/Bear/bear"),
                        new_translation=Gf.Vec3f(2.3, -0.41, 68.2),
                        new_rotation_euler=Gf.Vec3d(0.0, -0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                        old_translation=Gf.Vec3f(0, 0, 0),
                        old_rotation_euler=Gf.Vec3d(0.0, -0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                    )
                    omni.kit.commands.execute(
                        "SelectPrimsCommand",
                        old_selected_paths=["/World/Attic_NVIDIA/Geometry/Bear/bear"],
                        new_selected_paths=["/World/Attic_NVIDIA/Geometry/Books/BooksF"],
                        expand_in_stage=True,
                    )

                    omni.kit.commands.execute("CreatePrim", prim_path="/World/Camera", prim_type="Camera")

                    omni.kit.commands.execute(
                        "TransformPrim",
                        path=Sdf.Path("/World/Camera"),
                        new_transform_matrix=Gf.Matrix4d(
                            -0.6036080768538193,
                            -2.826537274338884e-07,
                            0.7972831297604912,
                            0.0,
                            -0.06580905458490746,
                            0.9965877435977037,
                            -0.04982244538430972,
                            0.0,
                            -0.7945621076184624,
                            -0.0825416302500037,
                            -0.601548071379954,
                            0.0,
                            -319.1174131237158,
                            130.84555448240013,
                            -455.18718167609984,
                            1.0,
                        ),
                    )

                    omni.kit.commands.execute(
                        "SetActiveViewportCamera", new_active_cam_path="/World/Camera", viewport_name="Viewport"
                    )

                    omni.kit.commands.execute(
                        "ChangeProperty", prop_path=Sdf.Path("/World/Camera.focalLength"), value=24.0, prev=50.0
                    )

                    # omni.kit.commands.execute(
                    #     "CreateReferenceCommand",
                    #     usd_context=omni.usd.get_context(),
                    #     path_to="/World/Pony_Cartoon",
                    #     asset_path="omniverse://localhost/Library/Pony_Cartoon.usdz",
                    #     instanceable=True,
                    # )

                    # omni.kit.commands.execute(
                    #     "TransformPrimSRT",
                    #     path=Sdf.Path("/World/Pony_Cartoon"),
                    #     new_translation=Gf.Vec3d(0.0, 0.0, -278.0879726156446),
                    #     new_rotation_euler=Gf.Vec3f(0.0, 40.791046142578125, 0.0),
                    #     new_rotation_order=Gf.Vec3i(0, 1, 2),
                    #     new_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                    #     old_translation=Gf.Vec3d(0.0, 0.0, -278.0879726156446),
                    #     old_rotation_euler=Gf.Vec3f(0.0, 0.0, 0.0),
                    #     old_rotation_order=Gf.Vec3i(0, 1, 2),
                    #     old_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                    # )
                    # omni.kit.commands.execute(
                    #     "CreateReferenceCommand",
                    #     usd_context=omni.usd.get_context(),
                    #     path_to="/World/Supermarine_Spitfire",
                    #     asset_path="omniverse://localhost/Library/Supermarine_Spitfire.usdz",
                    #     instanceable=True,
                    # )

                    # omni.kit.commands.execute(
                    #     "TransformPrimSRT",
                    #     path=Sdf.Path("/World/Supermarine_Spitfire"),
                    #     new_translation=Gf.Vec3d(56.215404820459995, 316.5051881860896, -1143.49844625089),
                    #     new_rotation_euler=Gf.Vec3f(35.7147331237793, 21.309598922729492, -26.81479263305664),
                    #     new_rotation_order=Gf.Vec3i(0, 1, 2),
                    #     new_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                    #     old_translation=Gf.Vec3d(104.69460467231677, 316.50518818609885, -1143.4984462509262),
                    #     old_rotation_euler=Gf.Vec3f(35.7147331237793, 21.309598922729492, -26.81479263305664),
                    #     old_rotation_order=Gf.Vec3i(0, 1, 2),
                    #     old_scale=Gf.Vec3f(1.0, 1.0, 1.0),
                    # )

                # omni.kit.commands.execute(
                #     "CreatePrimWithDefaultXform",
                #     prim_type="SphereLight1",
                #     attributes={"radius": 50, "intensity": 30000},
                #     select_new_prim=False,
                # )

                # omni.kit.commands.execute(
                #     "TransformPrimSRT",
                #     path=Sdf.Path("/World/SphereLight1"),
                #     new_translation=Gf.Vec3d(0.0, 105.86586048275845, -278.76257781136485),
                #     new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                #     new_rotation_order=Gf.Vec3i(0, 1, 2),
                #     new_scale=Gf.Vec3d(0.5, 0.5, 0.5),
                #     old_translation=Gf.Vec3d(0.0, 123.20213823325437, -278.76257781136485),
                #     old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                #     old_rotation_order=Gf.Vec3i(0, 1, 2),
                #     old_scale=Gf.Vec3d(0.5, 0.5, 0.5),
                # End USD

                ui.Button("Create Sphere Array", clicked_fn=lambda: on_click(), alignment=ui.Alignment.CENTER)
                ui.Button(
                    "Paint yourself or Click for Auto Paint",
                    clicked_fn=lambda: Paint_All(),
                    alignment=ui.Alignment.CENTER,
                )

                # preload material
                def Paint_All():
                    print("Painted!")

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Masonry/Adobe_Brick.mdl"
                        ),
                        mtl_name="Adobe_Brick",
                        mtl_path="/World/Looks/Adobe_Brick",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Stone/Adobe_Octagon_Dots.mdl"
                        ),
                        mtl_name="Adobe_Octagon_Dots",
                        mtl_path="/World/Looks/Adobe_Octagon_Dots",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Stone/Adobe_Octagon_Dots.mdl"
                        ),
                        mtl_name="Adobe_Octagon_Dots",
                        mtl_path="/World/Looks/Adobe_Octagon_Dots",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Metals/Aluminum_Anodized.mdl"
                        ),
                        mtl_name="Aluminum_Anodized",
                        mtl_path="/World/Looks/Aluminum_Anodized",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Metals/Aluminum_Anodized_Black.mdl"
                        ),
                        mtl_name="Aluminum_Anodized_Black",
                        mtl_path="/World/Looks/Aluminum_Anodized_Black",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Metals/Aluminum_Anodized_Blue.mdl"
                        ),
                        mtl_name="Aluminum_Anodized_Blue",
                        mtl_path="/World/Looks/Aluminum_Anodized_Blue",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Metals/Aluminum_Anodized_Charcoal.mdl"
                        ),
                        mtl_name="Aluminum_Anodized_Charcoal",
                        mtl_path="/World/Looks/Aluminum_Anodized_Charcoal",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Metals/Aluminum_Anodized_Red.mdl"
                        ),
                        mtl_name="Aluminum_Anodized_Red",
                        mtl_path="/World/Looks/Aluminum_Anodized_Red",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Metals/Aluminum_Cast.mdl"
                        ),
                        mtl_name="Aluminum_Cast",
                        mtl_path="/World/Looks/Aluminum_Cast",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Wood/Ash.mdl"
                        ),
                        mtl_name="Ash",
                        mtl_path="/World/Looks/Ash",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "Materials/Base/Wood/Bamboo_Planks.mdl"
                        ),
                        mtl_name="Bamboo_Planks",
                        mtl_path="/World/Looks/Bamboo_Planks",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Wood/Birch.mdl"
                        ),
                        mtl_name="Birch",
                        mtl_path="/World/Looks/Birch",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Carpet/Carpet_Diamond_Yellow.mdl"
                        ),
                        mtl_name="Carpet_Diamond_Yellow",
                        mtl_path="/World/Looks/Carpet_Diamond_Yellow",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Carpet/Carpet_Pattern_Squares_Multi.mdl"
                        ),
                        mtl_name="Carpet_Pattern_Squares_Multi",
                        mtl_path="/World/Looks/Carpet_Pattern_Squares_Multi",
                    )

                    omni.kit.commands.execute(
                        "CreateMdlMaterialPrimCommand",
                        mtl_url=(
                            "http://omniverse-content-production.s3-us-west-2.amazonaws.com"
                            "/Materials/Base/Textiles/Linen_Blue.mdl"
                        ),
                        mtl_name="Linen_Blue",
                        mtl_path="/World/Looks/Linen_Blue",
                    )

                    # assign material to speheres
                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_10",
                        material_path="/World/Looks/Adobe_Brick",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_11",
                        material_path="/World/Looks/Adobe_Octagon_Dots",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_12",
                        material_path="/World/Looks/Aluminum_Anodized",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_13",
                        material_path="/World/Looks/Aluminum_Anodized_Black",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_14",
                        material_path="/World/Looks/Aluminum_Anodized_Blue",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_05",
                        material_path="/World/Looks/Aluminum_Anodized_Charcoal",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_06",
                        material_path="/World/Looks/Aluminum_Anodized_Red",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_07",
                        material_path="/World/Looks/Aluminum_Cast",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_08",
                        material_path="/World/Looks/Ash",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_09",
                        material_path="/World/Looks/Bamboo_Planks",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere",
                        material_path="/World/Looks/Birch",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_02",
                        material_path="/World/Looks/Carpet_Diamond_Yellow",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_03",
                        material_path="/World/Looks/Carpet_Pattern_Squares_Multi",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "BindMaterialCommand",
                        prim_path="/World/Sphere_04",
                        material_path="/World/Looks/Linen_Blue",
                        strength="strongerThanDescendants",
                    )

                    omni.kit.commands.execute(
                        "CreatePrimWithDefaultXform",
                        prim_type="SphereLight",
                        attributes={"radius": 50, "intensity": 30000},
                        select_new_prim=False,
                    )

                    omni.kit.commands.execute(
                        "TransformPrimSRT",
                        path=Sdf.Path("/World/SphereLight"),
                        new_translation=Gf.Vec3d(324.0, 435.86586048275845, 51.76257781136485),
                        new_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        new_rotation_order=Gf.Vec3i(0, 1, 2),
                        new_scale=Gf.Vec3d(0.5, 0.5, 0.5),
                        old_translation=Gf.Vec3d(0.0, 123.20213823325437, -278.76257781136485),
                        old_rotation_euler=Gf.Vec3d(0.0, 0.0, 0.0),
                        old_rotation_order=Gf.Vec3i(0, 1, 2),
                        old_scale=Gf.Vec3d(0.5, 0.5, 0.5),
                    )

                def Reset_All():
                    print("You Reset It!")
                    stage = omni.usd.get_context().get_stage()
                    prim = stage.GetDefaultPrim()
                    removable = []
                    for child in prim.GetChildren():
                        removable.append(child.GetPath())
                    omni.kit.commands.execute("DeletePrims", paths=removable)

                # second set of spheres redundent for accidental double click (cant delet world, breaks file on reset)
                def physx_click():
                    asyncio.ensure_future(self.zerogravity())

                ui.Button("Set UP Physx", clicked_fn=lambda: physx_click())
                print("Spheres Set to Dynamic & Plane Set To Static!!!!!!!!!!!!!!!!!!!!")

                def physx_run():
                    asyncio.ensure_future(self.zerogravity2())

                ui.Button("Run Physx", clicked_fn=lambda: physx_run())

                ui.Button("Reset", clicked_fn=lambda: Reset_All())

    async def zerogravity(self):

        # DROP_WAIT_FRAMES = 280
        ENABLED_WAIT_FRAMES = 8
        ACTION_WAIT_FRAMES = 5

        omni.kit.commands.execute("ZeroGravitySetEnabled", enabled=True)

        for _ in range(ENABLED_WAIT_FRAMES):
            await omni.kit.app.get_app().next_update_async()
        self._usd_context.get_selection().set_selected_prim_paths(
            [
                "/World/Plane",
                "/World/Attic_NVIDIA/Geometry/Horse/horse",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_a_01",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_f_01",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_d_01",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_b_01",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_e_01",
                "/World/Attic_NVIDIA/Geometry/Rug",
                "/World/Attic_NVIDIA/Geometry/Horse",
                "/World/Attic_NVIDIA/Geometry/chair_01",
                "/World/Attic_NVIDIA/Geometry/Blanket_Fort/blanket_01/blanket_fort/blanket_01",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_a_02",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_f_03",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_b_02",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_f_02",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_d_03",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_b_03",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_d_02",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_e_02",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_e_03",
                "/World/Attic_NVIDIA/Geometry/Blocks/block_c_01",
                "/World/Attic_NVIDIA/Geometry/Blanket_Fort/blanket_03/blanket_fort/blanket_03",
                "/World/Attic_NVIDIA/Geometry/Blanket_Fort/pillow_03/blanket_fort/pillow_03",
                "/World/Attic_NVIDIA/Geometry/Blanket_Fort/pillow_02/blanket_fort/pillow_02",
                "/World/Attic_NVIDIA/Geometry/Blanket_Fort/blanket_02/blanket_fort/blanket_02",
                "/World/Attic_NVIDIA/Geometry/Rug/rug",
                "/World/Attic_NVIDIA/Geometry/Couch/couch_body/couch/couch_body",
                "/World/Attic_NVIDIA/Geometry/Couch/couch_pillow_02/couch/couch_pillow_2",
                "/World/Attic_NVIDIA/Geometry/Couch/couch_pillow_01/couch/couch_pillow_1",
            ],
            True,
        )

        omni.kit.commands.execute("ZeroGravitySetSelectedStatic")

        for _ in range(ACTION_WAIT_FRAMES):
            await omni.kit.app.get_app().next_update_async()
        myspheres = [
            "/World/Sphere",
            "/World/Sphere_01",
            "/World/Sphere_02",
            "/World/Sphere_03",
            "/World/Sphere_04",
            "/World/Sphere_05",
            "/World/Sphere_06",
            "/World/Sphere_07",
            "/World/Sphere_08",
            "/World/Sphere_09",
            "/World/Sphere_10",
            "/World/Sphere_11",
            "/World/Sphere_12",
            "/World/Sphere_13",
            "/World/Sphere_14",
            "/World/Attic_NVIDIA/Geometry/Ball/ball",
            "/World/Attic_NVIDIA/Geometry/Bear/bear",
        ]
        self._usd_context.get_selection().set_selected_prim_paths(
            myspheres,
            False,
        )

    async def zerogravity2(self):

        DROP_WAIT_FRAMES = 500
        # ENABLED_WAIT_FRAMES = 10
        ACTION_WAIT_FRAMES = 5

        omni.kit.commands.execute("ZeroGravitySetSelectedDynamic")

        for _ in range(ACTION_WAIT_FRAMES):
            await omni.kit.app.get_app().next_update_async()
        omni.kit.commands.execute("ZeroGravitySetDropping", dropping=True)

        for _ in range(DROP_WAIT_FRAMES):
            await omni.kit.app.get_app().next_update_async()
        omni.kit.commands.execute("ZeroGravitySetDropping", dropping=False)

        for _ in range(ACTION_WAIT_FRAMES):
            await omni.kit.app.get_app().next_update_async()

        omni.kit.commands.execute("ZeroGravityClearAll")
        omni.kit.commands.execute("ZeroGravitySetEnabled", enabled=False)

    def on_shutdown(self):
        """Shuts down program"""
        print("[sphere.world] MyExtension shutdown")


# """
# This Extension allows the user to rapidly create spheres, apply materials and physics gravity drop.
# Rest button allows user to reset and repaint new MDL on spheres for different looks
# Physics selections are preset (no user input requires)
# Spheres are slightly misaligned on each stack so cascade isnt perfectly linear
# Plane is slightly tilted to allow spheres to continue to move after impact
# """
