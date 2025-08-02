
import 'package:flutter/material.dart';
import 'package:flutter_app/exercise/exercise_card.dart';
import 'package:go_router/go_router.dart';

class ExerciseListView extends StatefulWidget {
  const ExerciseListView({super.key});

  @override
  State<StatefulWidget> createState() => _ExerciseListViewState();
  
}

class _ExerciseListViewState extends State {

  @override
  Widget build(BuildContext context) => Scaffold(
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
  );
  
}