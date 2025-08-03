
import 'package:flutter/material.dart';
import 'package:flutter_app/exercise/exercise_card.dart';

class ExerciseListPopupButton extends StatefulWidget {
  const ExerciseListPopupButton({super.key});

  @override
  State<StatefulWidget> createState() => _ExerciseListPopupButtonState();
  
}

class _ExerciseListPopupButtonState extends State {

  @override
  Widget build(BuildContext context) => PopupMenuButton(
    position: PopupMenuPosition.over,
    icon: Icon(Icons.add),
    onSelected: (value) {
      final snackBar = SnackBar(
        content: Text('$value'),
        duration: Duration(seconds: 4),
      );

      ScaffoldMessenger.of(context).showSnackBar(snackBar);
    },
    itemBuilder: (context) => [
      for (int i = 0; i < 100; ++i) PopupMenuItem(
        value: i,
        child: ExerciseCard(),
      )
    ],
  );
  
  
  /*Scaffold(
    bottomNavigationBar: BottomNavigationBar(
      items: [
        BottomNavigationBarItem(icon: Icon(Icons.arrow_back), label: 'Back'),
        BottomNavigationBarItem(icon: Icon(Icons.check), label: 'Confirm'),
      ],
      onTap: (int value) {
        if (value > 0) {
          //TODO:: confirmed
        }

        context.pop();
      },
    ),
    body: Center(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [for (int i = 0; i < 100; ++i) ExerciseCard()],
        ),
      ),
    ),
  );*/
  
}