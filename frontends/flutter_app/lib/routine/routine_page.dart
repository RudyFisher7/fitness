
import 'package:flutter/material.dart';
import 'package:flutter_app/exercise/exercise_form.dart';
import 'package:flutter_app/exercise/exercise_list_popup_button.dart';
import 'package:go_router/go_router.dart';

class RoutinePage extends StatefulWidget {
  const RoutinePage({super.key});

  @override
  State<StatefulWidget> createState() => _RoutinePageState();
  
}

class _RoutinePageState extends State {
  void _onItemTapped(int value) {
    if (value == 1) {
      final overlayContext = Overlay.of(context).context;
      final size = MediaQuery.of(overlayContext).size;
      showMenu(
        context: overlayContext,
        position: RelativeRect.fromLTRB(
          size.width / 2,
          size.height / 2,
          size.width / 2,
          size.height / 2,
        ),
        items: [
          PopupMenuItem(
            value: 0,
            child: Text('Cancel'),
          ),
          PopupMenuItem(
            value: 1,
            child: Text('Confirm'),
          ),
        ],
      ).then((value) {
        if (value == 1) {
          //TODO:: abort workout
        } else {
          //TODO:: save working and keep in-progress
        }
      });
    }

    context.pop();
  }

  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(),
    bottomNavigationBar: BottomNavigationBar(
      items: [
        BottomNavigationBarItem(icon: Icon(Icons.arrow_back), label: 'Back'),
        BottomNavigationBarItem(icon: Icon(Icons.cancel), label: 'Abort'),
        BottomNavigationBarItem(icon: Icon(Icons.check), label: 'Finish'),
      ],
      onTap: _onItemTapped,
    ),
    body: Padding(
      padding: EdgeInsetsGeometry.only(left: 40.0, right: 40.0),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // ExerciseForm(),
            ExerciseListPopupButton(),
          ],
        ),
      ),
    ),
  );
  
}